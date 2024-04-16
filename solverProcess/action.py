from pulp import LpProblem, LpMaximize, LpVariable, LpBinary, lpSum, LpAffineExpression
import pandas as pd
from numpy import transpose
from math import isnan
import random
import pandas as pd
import os


def solve(controller):
    # get data from the responses or the projects
    students_projects_array_with_mails, students_projects_info_finance_array_with_mails, students_projects_only_one_semester_array_with_mails, data_project = get_data()

    students_projects_info_finance_array = pd.DataFrame([row[1:] for row in students_projects_info_finance_array_with_mails]).to_numpy()
    students_projects_array = pd.DataFrame([row[1:] for row in students_projects_array_with_mails]).to_numpy()
    students_projects_only_one_semester_array = pd.DataFrame([row[1:] for row in students_projects_only_one_semester_array_with_mails]).to_numpy()

    if not students_projects_array.any():
        print("No data")
        return


    ##################################################################

    # define the variables used in the solver

    lp_file = 'common/solver.lp'
    projects_students_array = transpose(students_projects_array)
    projects_students_info_finance_array = transpose(students_projects_info_finance_array)
    projects_students_only_one_semester_array = transpose(students_projects_only_one_semester_array)
    number_of_projects = len(projects_students_array)
    bigM = 99999

    already_assigned = []

    ##################################################################

    # try:
    model = LpProblem(name="assign_students_to_projects", sense=LpMaximize)

    # all the variables
    variables_normal = {(i, j): LpVariable(name=f"s{i+1}p{j+1}N?{students_projects_array_with_mails[i][0]}", cat=LpBinary) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))}
    variables_info_finance = {(i, j): LpVariable(name=f"s{i+1}p{j+1}IF?{students_projects_info_finance_array_with_mails[i][0]}", cat=LpBinary) for i in range(len(students_projects_info_finance_array)) for j in range(len(students_projects_info_finance_array[i]))}
    variables_only_one_semester = {(i, j): LpVariable(name=f"s{i+1}p{j+1}OS?{students_projects_only_one_semester_array_with_mails[i][0]}", cat=LpBinary) for i in range(len(students_projects_only_one_semester_array)) for j in range(len(students_projects_only_one_semester_array[i]))}

    binary_variables = {j: LpVariable(name=f"b{j}", cat=LpBinary) for j in range(len(projects_students_array))}
    
    # add the objective function
    tmp = [(variables_normal[i, j],students_projects_array[i][j]) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))]
    tmp += [(variables_info_finance[i, j],students_projects_info_finance_array[i][j]) for i in range(len(students_projects_info_finance_array)) for j in range(len(students_projects_info_finance_array[i]))]
    tmp += [(variables_only_one_semester[i, j],students_projects_only_one_semester_array[i][j]) for i in range(len(students_projects_only_one_semester_array)) for j in range(len(students_projects_only_one_semester_array[i]))]

    # disable the projects multipliers
    for i in range(number_of_projects):
        for email in data_project[i][0]:
            for j in range(len(students_projects_array_with_mails)):
                if students_projects_array_with_mails[j][0] == email:
                    for lp_var in tmp:
                        if lp_var[0].name.split("?")[0] == f"s{j+1}p{i+1}N":
                            tmp[tmp.index(lp_var)] = (lp_var[0], 1)
                            break
                    if j not in already_assigned:
                        already_assigned.append(j)
                    else:
                        return f"Error: Student {j}, already assigned to a project"
            for j in range(len(students_projects_info_finance_array_with_mails)):
                if students_projects_info_finance_array_with_mails[j][0] == email:
                    for lp_var in tmp:
                        if lp_var[0].name.split("?")[0] == f"s{j+1}p{i+1}IF":
                            tmp[tmp.index(lp_var)] = (lp_var[0], 1)
                            break
                    if j not in already_assigned:
                        already_assigned.append(j)
                    else:
                        return f"Error: Student {j}, already assigned to a project"
            for j in range(len(students_projects_only_one_semester_array_with_mails)):
                if students_projects_only_one_semester_array_with_mails[j][0] == email:
                    for lp_var in tmp:
                        if lp_var[0].name.split("?")[0] == f"s{j+1}p{i+1}OS":
                            tmp[tmp.index(lp_var)] = (lp_var[0], 1)
                            break
                    if j not in already_assigned:
                        already_assigned.append(j)
                    else:
                        return f"Error: Student {j}, already assigned to a project"        

    model += LpAffineExpression(tmp)

    # add the constraints

    # each student can only be assigned to one project
    for i in range(len(students_projects_array)):
        model += lpSum(variables_normal[i, j] for j in range(len(students_projects_array[i]))) <= 1
    
    # each student in the info finance can only be assigned to one project
    for i in range(len(students_projects_info_finance_array)):
        model += lpSum(variables_info_finance[i, j] for j in range(len(students_projects_info_finance_array[i]))) <= 1

    # each student in the only one semester can only be assigned to one project
    for i in range(len(students_projects_only_one_semester_array)):
        model += lpSum(variables_only_one_semester[i, j] for j in range(len(students_projects_only_one_semester_array[i]))) <= 1

    # each project must have a maximum number of students
    for j in range(number_of_projects):
        tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))

        if len(projects_students_info_finance_array) > 0:
            tmp2 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_info_finance_array[j])))
        else:
            tmp2 = 0

        if len(projects_students_only_one_semester_array) > 0:
            tmp3 = lpSum(variables_only_one_semester[i, j] for i in range(len(projects_students_only_one_semester_array[j])))
        else:
            tmp3 = 0

        model += tmp1 + tmp2 + tmp3 <= data_project[j][2]

    # each project must have a minimum number of students 1
    for j in range(number_of_projects):
        tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))

        if len(projects_students_info_finance_array) > 0:
            tmp2 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_info_finance_array[j])))
        else:
            tmp2 = 0

        if len(projects_students_only_one_semester_array) > 0:
            tmp3 = lpSum(variables_only_one_semester[i, j] for i in range(len(projects_students_only_one_semester_array[j])))
        else:
            tmp3 = 0

        model += tmp1 + tmp2 + tmp3 <= bigM * binary_variables[j]

    # each project must have a minimum number of students 2
    for j in range(number_of_projects):
        tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))

        if len(projects_students_info_finance_array) > 0:
            tmp2 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_info_finance_array[j])))
        else:
            tmp2 = 0

        if len(projects_students_only_one_semester_array) > 0:
            tmp3 = lpSum(variables_only_one_semester[i, j] for i in range(len(projects_students_only_one_semester_array[j])))
        else:
            tmp3 = 0

        model += tmp1 + tmp2 + tmp3 >= data_project[j][1] * binary_variables[j]

    # each project must have a maximum number of students in info finance
    

    if len(projects_students_only_one_semester_array) > 0 and len(projects_students_info_finance_array) > 0:
        for j in range(number_of_projects):
            tmp1 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_info_finance_array[j])))
            tmp2 = lpSum(variables_only_one_semester[i, j] for i in range(len(projects_students_only_one_semester_array[j])))
            model += tmp1 + tmp2 <= 2

    elif len(projects_students_info_finance_array) > 0:
        for j in range(number_of_projects):
            tmp1 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_info_finance_array[j])))
            model += tmp1 <= 2

    elif len(projects_students_only_one_semester_array) > 0:
        for j in range(number_of_projects):
            tmp1 = lpSum(variables_only_one_semester[i, j] for i in range(len(projects_students_only_one_semester_array[j])))
            model += tmp1 <= 2

    # student already assigned to a project
    for i in range(number_of_projects):
        for email in data_project[i][0]:
            for j in range(len(students_projects_array_with_mails)):
                if students_projects_array_with_mails[j][0] == email:
                    model += variables_normal[j, i] == 1
            for j in range(len(students_projects_info_finance_array_with_mails)):
                if students_projects_info_finance_array_with_mails[j][0] == email:
                    model += variables_info_finance[j, i] == 1
            for j in range(len(students_projects_only_one_semester_array_with_mails)):
                if students_projects_only_one_semester_array_with_mails[j][0] == email:
                    model += variables_only_one_semester[j, i] == 1
    
    model.solve()
    model.writeLP(lp_file)


    result_array = []
    for i in range(len(students_projects_array)):
        tmp = []
        tmp.append(variables_normal[i, 0].name)
        for j in range(len(students_projects_array[i])):
            tmp.append(variables_normal[i, j].varValue)
        result_array.append(tmp)
        
    for i in range(len(students_projects_info_finance_array)):
        tmp = []
        tmp.append(variables_info_finance[i, 0].name)
        for j in range(len(students_projects_info_finance_array[i])):
            tmp.append(variables_info_finance[i, j].varValue)
        result_array.append(tmp)

    for i in range(len(students_projects_only_one_semester_array)):
        tmp = []
        tmp.append(variables_only_one_semester[i, 0].name)
        for j in range(len(students_projects_only_one_semester_array[i])):
            tmp.append(variables_only_one_semester[i, j].varValue)
        result_array.append(tmp)

    result_df = pd.DataFrame(result_array)

    if(model.status == 1):
        result_df.to_csv('common/resultSolver.csv', index=False)
    else:
        return "No optimal solution found"

    # delete ./common/recap.xlsx
    try:
        os.remove('./common/recap.xlsx')
    except FileNotFoundError:
        pass

    controller.show_frame("solverProcess")

    # except Exception as e:
    #     return str(e)

def formated_table(data):
    data = pd.DataFrame(data[1:], columns=data[0])

    tmp_data = data.iloc[:, 0]
    tmp_data = pd.concat([tmp_data, data.iloc[:, 1:]], axis=1)

    tmp_data = tmp_data.to_numpy()

    return tmp_data

def get_data():
    table_normal = []
    table_info_finance = []

    traduction_ = {
        'response' : {
            'fr' : 'Réponse',
            'en' : 'Response',
        },
        'email' : {
            'fr' : 'Adresse de courriel',
            'en' : 'Email address',
        }
    }

    try:
        data = pd.read_excel("./common/answerProjects.xlsx")
        if not data.empty:
            data_array_norm = []
            data_array_info_finance = []
            data_array_only_one_semester = []

            language = 'fr' if data.columns[0] == "Nom de famille" else 'en'
            
            num_projects = len([col for col in data.columns if traduction_['response'][language] in col]) - 2

            project_numbers = ["Project number"] + [f"Project {i}" for i in range(1, num_projects + 1)]

            data_array_norm.append(project_numbers)
            data_array_info_finance.append(project_numbers)
            data_array_only_one_semester.append(project_numbers)
            
            for index, row in data.iterrows():
                student_data = [f"{row[traduction_['email'][language]]}"]
                grades = []

                # vérifier si la personne est en informatique et finance
                if row[f'{traduction_["response"][language]} 1'] == "Oui   Yes":
                    for i in range(1, num_projects + 1):
                        try:
                            grade = int(row[f'{traduction_["response"][language]} {i+1}'])
                        except ValueError:
                            grade = 0  
                        grades.append(grade)

                    non_zero_grades = [grade for grade in grades if grade != 0]
                    zero_indices = [i for i, grade in enumerate(grades) if grade == 0]

                    # ajouter des notes aléatoires pour les projets non notés
                    while len(non_zero_grades) <= 5:
                        random_index = random.choice(zero_indices)
                        grades[random_index] = 5
                        non_zero_grades.append(5)

                    # normaliser les notes
                    normalized_grades = [int((grade / max(non_zero_grades))*5) if grade != 0 else 0 for grade in grades]
                    student_data += normalized_grades

                    data_array_info_finance.append(student_data)

                elif row[f'{traduction_["response"][language]} 2'] == "Non   No":
                    for i in range(1, num_projects + 1):
                        try:
                            grade = int(row[f'{traduction_["response"][language]} {i+1}'])
                        except ValueError:
                            grade = 0  
                        grades.append(grade)

                    non_zero_grades = [grade for grade in grades if grade != 0]
                    zero_indices = [i for i, grade in enumerate(grades) if grade == 0]

                    # ajouter des notes aléatoires pour les projets non notés
                    while len(non_zero_grades) <= 5:
                        random_index = random.choice(zero_indices)
                        grades[random_index] = 5
                        non_zero_grades.append(5)

                    # normaliser les notes
                    normalized_grades = [int((grade / max(non_zero_grades))*5) if grade != 0 else 0 for grade in grades]
                    student_data += normalized_grades

                    data_array_only_one_semester.append(student_data)

                elif row[f'{traduction_["response"][language]} 1'] == "Non   No" and row[f'{traduction_["response"][language]} 2'] == "Oui   Yes":
                    for i in range(1, num_projects + 1):
                        try:
                            grade = int(row[f'{traduction_["response"][language]} {i+1}'])
                        except ValueError:
                            grade = 0  
                        grades.append(grade)

                    non_zero_grades = [grade for grade in grades if grade != 0]
                    zero_indices = [i for i, grade in enumerate(grades) if grade == 0]

                    # ajouter des notes aléatoires pour les projets non notés
                    while len(non_zero_grades) <= 5:
                        random_index = random.choice(zero_indices)
                        grades[random_index] = 5
                        non_zero_grades.append(5)

                    # normaliser les notes
                    normalized_grades = [int((grade / max(non_zero_grades))*5) if grade != 0 else 0 for grade in grades]
                    student_data += normalized_grades

                    data_array_norm.append(student_data)

                else:
                    for i in range(1, num_projects + 1):
                        grade = 0
                        grades.append(grade)

                    non_zero_grades = [grade for grade in grades if grade != 0]
                    zero_indices = [i for i, grade in enumerate(grades) if grade == 0]

                    # ajouter des notes aléatoires pour les projets non notés
                    while len(non_zero_grades) <= 5:
                        random_index = random.choice(zero_indices)
                        grades[random_index] = 5
                        non_zero_grades.append(5)

                    # normaliser les notes
                    normalized_grades = [int((grade / max(non_zero_grades))*5) if grade != 0 else 0 for grade in grades]
                    student_data += normalized_grades

                    data_array_norm.append(student_data)

            table_normal = formated_table(data_array_norm)
            table_info_finance = formated_table(data_array_info_finance)
            table_only_one_semester = formated_table(data_array_only_one_semester)

            df = pd.DataFrame(table_normal)
            df.to_excel('./common/table_normal.xlsx', index=False)

            df = pd.DataFrame(table_info_finance)
            df.to_excel('./common/table_info_finance.xlsx', index=False)

            df = pd.DataFrame(table_only_one_semester)
            df.to_excel('./common/table_only_one_semester.xlsx', index=False)

    except FileNotFoundError:
        print("No data")

    data_project = []
    try:
        data = pd.read_excel("./common/dataProjects.xlsx")
        if not data.empty:
            data_array_norm = []
            for index, row in data.iterrows():
                project_data = [row['Team emails'], row["Minimum students"], row["Maximum students"]]

                if isinstance(project_data[0], str):
                    project_data[0] = [data for data in project_data[0].split(";")]
                else:
                    project_data[0] = []

                if not isnan(project_data[1]):
                    project_data[1] = int(project_data[1])
                else:
                    project_data[1] = 3

                if not isnan(project_data[2]):
                    project_data[2] = int(project_data[2])
                else:
                    project_data[2] = 7

                data_array_norm.append(project_data)
            
            data_project = data_array_norm
    except FileNotFoundError:
        print("No data")

    return table_normal, table_info_finance, table_only_one_semester, data_project

    #passer avec deux contrainte
    # somme de tous le projet
    # somme de tous les projets info finance <= 0.33 * dernière somme