from pulp import LpProblem, LpMaximize, LpVariable, LpBinary, lpSum, LpAffineExpression
import pandas as pd
from numpy import transpose
from math import isnan
import random
import pandas as pd


def solve(controller):
    students_projects_array_with_mails, students_projects_info_finance_array_with_mails, data_project = get_data()

    students_projects_info_finance_array = pd.DataFrame([row[1:] for row in students_projects_info_finance_array_with_mails]).to_numpy()
    students_projects_array = pd.DataFrame([row[1:] for row in students_projects_array_with_mails]).to_numpy()


    if not students_projects_array.any():
        print("No data")
        return


    ##################################################################

    lp_file = 'common/solver.lp'
    projects_students_array = transpose(students_projects_array)
    projects_students_info_finance_array = transpose(students_projects_info_finance_array)
    number_of_projects = len(projects_students_array)
    bigM = 99999

    already_assigned = []

    ##################################################################

    try:

        model = LpProblem(name="assign_students_to_projects", sense=LpMaximize)

        variables_normal = {(i, j): LpVariable(name=f"s{i+1}p{j+1}N", cat=LpBinary) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))}
        variables_info_finance = {(i, j): LpVariable(name=f"s{i+1}p{j+1}IF", cat=LpBinary) for i in range(len(students_projects_info_finance_array)) for j in range(len(students_projects_info_finance_array[i]))}

        binary_variables = {j: LpVariable(name=f"b{j}", cat=LpBinary) for j in range(len(projects_students_array))}
        
        tmp = [(variables_normal[i, j],students_projects_array[i][j]) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))]
        tmp += [(variables_info_finance[i, j],students_projects_info_finance_array[i][j]) for i in range(len(students_projects_info_finance_array)) for j in range(len(students_projects_info_finance_array[i]))]

        for i in range(number_of_projects):
            for email in data_project[i][0]:
                for j in range(len(students_projects_array_with_mails)):
                    if students_projects_array_with_mails[j][0] == email:
                        for lp_var in tmp:
                            if lp_var[0].name == f"s{j+1}p{i+1}N":
                                tmp[tmp.index(lp_var)] = (lp_var[0], 1)
                                break
                        if j not in already_assigned:
                            already_assigned.append(j)
                        else:
                            print("Error: Student already assigned to a project")
                            return

        model += LpAffineExpression(tmp)

        for i in range(len(students_projects_array)):
            model += lpSum(variables_normal[i, j] for j in range(len(students_projects_array[i]))) <= 1
        
        for i in range(len(students_projects_info_finance_array)):
            model += lpSum(variables_info_finance[i, j] for j in range(len(students_projects_info_finance_array[i]))) <= 1

        for j in range(number_of_projects):
            tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))

            if len(projects_students_info_finance_array) > 0:
                tmp2 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_info_finance_array[j])))
            else:
                tmp2 = 0

            model += tmp1 + tmp2 <= data_project[j][2]

        for j in range(number_of_projects):
            tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))

            if len(projects_students_info_finance_array) > 0:
                tmp2 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_info_finance_array[j])))
            else:
                tmp2 = 0

            model += tmp1 + tmp2 <= bigM * binary_variables[j]

        for j in range(number_of_projects):
            tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))

            if len(projects_students_info_finance_array) > 0:
                tmp2 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_info_finance_array[j])))
            else:
                tmp2 = 0

            model += tmp1 + tmp2 >= data_project[j][1] * binary_variables[j]

        if len(projects_students_info_finance_array) > 0:
            for j in range(number_of_projects):
                tmp1 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_info_finance_array[j])))
                model += tmp1 <= 2

        for i in range(number_of_projects):
            for email in data_project[i][0]:
                for j in range(len(students_projects_array_with_mails)):
                    if students_projects_array_with_mails[j][0] == email:
                        model += variables_normal[j, i] == 1
        model.solve()
        model.writeLP(lp_file)

        result_array = [[variables_normal[i, j].varValue for j in range(len(students_projects_array[i]))] for i in range(len(students_projects_array))] + [[variables_info_finance[i, j].varValue for j in range(len(students_projects_info_finance_array[i]))] for i in range(len(students_projects_info_finance_array))]

        result_df = pd.DataFrame(result_array)

        if(model.status == 1):
            print("Optimal solution found")
            result_df.to_csv('common/resultSolver.csv', index=False)
        else:
            print("No optimal solution found")
            return "No optimal solution found"

        controller.show_frame("solverProcess")

    except Exception as e:
        return str(e)

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

            language = 'fr' if data.columns[0] == "Nom de famille" else 'en'
            
            num_projects = len([col for col in data.columns if traduction_['response'][language] in col]) - 2

            project_numbers = ["Project number"] + [f"Project {i}" for i in range(1, num_projects + 1)]

            data_array_norm.append(project_numbers)
            data_array_info_finance.append(project_numbers)
            
            for index, row in data.iterrows():
                student_data = [f"{row[traduction_['email'][language]]}"]
                grades = []

                # vérifier si la personne est en informatique et finance
                if row[f'{traduction_["response"][language]} 1'] == "Non   No":
                    for i in range(1, num_projects + 1):
                        try:
                            grade = int(row[f'{traduction_["response"][language]} {i}'])
                        except ValueError:
                            grade = 0  
                        grades.append(grade)

                    non_zero_grades = [grade for grade in grades if grade != 0]
                    zero_indices = [i for i, grade in enumerate(grades) if grade == 0]

                    while len(non_zero_grades) <= 5:
                        random_index = random.choice(zero_indices)
                        grades[random_index] = 5
                        non_zero_grades.append(5)

                    normalized_grades = [int((grade / max(non_zero_grades))*5) if grade != 0 else 0 for grade in grades]
                    student_data += normalized_grades

                    data_array_norm.append(student_data)


                elif row[f'{traduction_["response"][language]} 1'] == "Oui   Yes":
                    for i in range(1, num_projects + 1):
                        try:
                            grade = int(row[f'{traduction_["response"][language]} {i}'])
                        except ValueError:
                            grade = 0  
                        grades.append(grade)

                    non_zero_grades = [grade for grade in grades if grade != 0]
                    zero_indices = [i for i, grade in enumerate(grades) if grade == 0]

                    while len(non_zero_grades) <= 5:
                        random_index = random.choice(zero_indices)
                        grades[random_index] = 5
                        non_zero_grades.append(5)

                    normalized_grades = [int((grade / max(non_zero_grades))*5) if grade != 0 else 0 for grade in grades]
                    student_data += normalized_grades

                    data_array_info_finance.append(student_data)
                
                else:
                    for i in range(1, num_projects + 1):
                        grade = 0  
                        grades.append(grade)

                    non_zero_grades = [grade for grade in grades if grade != 0]
                    zero_indices = [i for i, grade in enumerate(grades) if grade == 0]
                    
                    while len(non_zero_grades) <= 5:
                        random_index = random.choice(zero_indices)
                        grades[random_index] = 5
                        non_zero_grades.append(5)

                    normalized_grades = [int((grade / max(non_zero_grades))*5) if grade != 0 else 0 for grade in grades]
                    student_data += normalized_grades

                    data_array_norm.append(student_data)

            table_normal = formated_table(data_array_norm)
            table_info_finance = formated_table(data_array_info_finance)
    except FileNotFoundError:
        print("No data")

    data_project = []
    try:
        data = pd.read_excel("./common/dataProjects.xlsx")
        if not data.empty:
            data_array_norm = []
            for index, row in data.iterrows():
                project_data = [row['Equipe'], row["Minimum d'étudiants"], row["Maximum d'étudiants"]]

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


    return table_normal, table_info_finance, data_project
    

    #passer avec deux contrainte
    # somme de tous le projet
    # somme de tous les projets info finance <= 0.33 * dernière somme