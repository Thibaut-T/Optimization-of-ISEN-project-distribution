from pulp import LpProblem, LpMaximize, LpVariable, LpBinary, lpSum, LpAffineExpression
import pandas as pd
from numpy import transpose
import numpy as np
import random
import pandas as pd


def solve(controller):
    students_projects_array, students_info_finance_projects_array = get_data()

    ##################################################################

    lp_file = 'common/solver.lp'
    projects_students_array = transpose(students_projects_array)
    projects_projects_info_finance_array = transpose(students_info_finance_projects_array)
    number_of_projects = len(projects_students_array)
    max_students_per_project = 7
    min_students_per_project = 3
    bigM = 99999

    ##################################################################

    model = LpProblem(name="assign_students_to_projects", sense=LpMaximize)

    variables_normal = {(i, j): LpVariable(name=f"s{i+1}p{j+1}N", cat=LpBinary) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))}
    variables_info_finance = {(i, j): LpVariable(name=f"s{i+1}p{j+1}IF", cat=LpBinary) for i in range(len(students_info_finance_projects_array)) for j in range(len(students_info_finance_projects_array[i]))}

    binary_variables = {j: LpVariable(name=f"b{j}", cat=LpBinary) for j in range(len(projects_students_array))}

    tmp = [(variables_normal[i, j],students_projects_array[i][j]) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))]
    tmp += [(variables_info_finance[i, j],students_info_finance_projects_array[i][j]) for i in range(len(students_info_finance_projects_array)) for j in range(len(students_info_finance_projects_array[i]))]

    model += LpAffineExpression(tmp)

    for i in range(len(students_projects_array)):
        model += lpSum(variables_normal[i, j] for j in range(len(students_projects_array[i]))) <= 1
    
    for i in range(len(students_info_finance_projects_array)):
        model += lpSum(variables_info_finance[i, j] for j in range(len(students_info_finance_projects_array[i]))) <= 1


    for j in range(number_of_projects):
        tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))
        tmp2 = lpSum(variables_info_finance[i, j] if i < len(students_info_finance_projects_array) else 0 for i in range(len(projects_projects_info_finance_array[j])))
        model += tmp1 + tmp2 <= max_students_per_project

    for j in range(number_of_projects):
        tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))
        tmp2 = lpSum(variables_info_finance[i, j] if i < len(students_info_finance_projects_array) else 0 for i in range(len(projects_projects_info_finance_array[j])))
        model += tmp1 + tmp2 <= bigM * binary_variables[j]

    for j in range(number_of_projects):
        tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))
        tmp2 = lpSum(variables_info_finance[i, j] if i < len(students_info_finance_projects_array) else 0 for i in range(len(projects_projects_info_finance_array[j])))
        model += tmp1 + tmp2 >= min_students_per_project * binary_variables[j]

    if len(students_info_finance_projects_array) > 0:
        for j in range(number_of_projects):
            tmp1 = lpSum(variables_info_finance[i, j] for i in range(len(projects_projects_info_finance_array[j])))
            model += tmp1 <= 2

    model.solve()
    model.writeLP(lp_file)

    result_array = [[variables_normal[i, j].varValue for j in range(len(students_projects_array[i]))] for i in range(len(students_projects_array))] + [[variables_info_finance[i, j].varValue for j in range(len(students_info_finance_projects_array[i]))] for i in range(len(students_info_finance_projects_array))]

    binaries = [binary_variables[j].varValue for j in range(len(projects_students_array))]

    result_df = pd.DataFrame(result_array)
    result_df.to_csv('common/resultSolver.csv', index=False)

    controller.show_frame("solverProcess")    

def formated_table(data):
    data = pd.DataFrame(data[1:], columns=data[0])
    
    data = data.iloc[:, 1:]
    data = data.to_numpy()

    return data

def get_data():
    data = pd.read_excel("./common/answerProjects.xlsx")
    if not data.empty:
        data_array = []
        num_projects = len([col for col in data.columns if 'Réponse' in col])
        project_numbers = ["Project number"] + [f"Project {i}" for i in range(1, num_projects + 1)]
        data_array.append(project_numbers)

        for index, row in data.iterrows():
            student_data = [f"{row['Nom de famille']} {row['Prénom']}"]
            grades = []
            for i in range(1, num_projects + 1):
                try:
                    grade = int(row[f'Réponse {i}'])
                except ValueError:
                    grade = 0  
                grades.append(grade)

            non_zero_grades = [grade for grade in grades if grade != 0]
            zero_indices = [i for i, grade in enumerate(grades) if grade == 0]
            if zero_indices:
                random_index = random.choice(zero_indices)
                grades[random_index] = 5
                non_zero_grades.append(5)

            top_grades = sorted(grades, reverse=True)[:5]
            student_data += [grade if grade in top_grades else 0 for grade in grades]

            data_array.append(student_data)
        print(data_array)
        return formated_table(data_array),[[7, 0, 9, 0, 8, 10, 0, 7, 8]]