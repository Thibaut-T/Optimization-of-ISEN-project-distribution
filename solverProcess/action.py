from pulp import LpProblem, LpMaximize, LpVariable, LpBinary, lpSum, LpAffineExpression
import pandas as pd
from numpy import transpose
import numpy as np
import random

def solve(students_projects_array, students_info_finance_projects_array):
    ##################################################################


    students_projects_array = pd.DataFrame(np.zeros((len(students_projects_array), number_of_projects), dtype=int))
    
    students_projects_array = np.array([[0 for i in range(number_of_projects)] for j in range(len(students_projects_array))])
                        
    lp_file = 'common/output.lp'
    projects_students_array = transpose(students_projects_array)
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
        tmp2 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_array[j])))
        model += tmp1 + tmp2 <= max_students_per_project

    for j in range(number_of_projects):
        tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))
        tmp2 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_array[j])))
        model += tmp1 + tmp2 <= bigM * binary_variables[j]

    for j in range(number_of_projects):
        tmp1 = lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j])))
        tmp2 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_array[j])))
        model += tmp1 + tmp2 >= min_students_per_project * binary_variables[j]

    for j in range(number_of_projects):
        tmp1 = lpSum(variables_info_finance[i, j] for i in range(len(projects_students_array[j])))
        model += tmp1 <= 2

    model.writeLP(lp_file)
    model.solve()

    result_array = [[variables_normal[i, j].varValue for j in range(len(students_projects_array[i]))] for i in range(len(students_projects_array))]

    print(result_array)

    result_df = pd.DataFrame(result_array)
    result_df.to_csv('common/result.csv', index=False)

def tmp_table():
    file_path = 'TEST3.xlsx'
    data = pd.read_excel(file_path)

    column_names = data.columns
    project_columns = [col for col in column_names if col.startswith('Projet')]

    max_project = max(int(project.split()[-1]) for project in project_columns)

    students_projects_array = [[0 for i in range(max_project)] for j in range(len(data))]
    name_students = [row['Nom'] for index, row in data.iterrows()]

    for index, row in data.iterrows():
        assigned_projects = set(project for project in project_columns if pd.notnull(row[project]))
        projects_to_assign = 5 - len(assigned_projects)

        for project in project_columns:
            students_projects_array[index][int(project.split()[-1])-1] = 0
            if pd.notnull(row[project]): 
                students_projects_array[index][int(project.split()[-1])-1] = int(row[project])
                    
        
        if projects_to_assign < 0:
            ordered_projects = sorted(students_projects_array[index], reverse=True)
            limit = ordered_projects[5]
        
            
            for i in range(len(students_projects_array[index])):
                if students_projects_array[index][i] <= limit and students_projects_array[index][i] > 0 and projects_to_assign < 0:
                    students_projects_array[index][i] = 0
                    projects_to_assign += 1
            ordered_projects = sorted(students_projects_array[index], reverse=True)
                            
        while projects_to_assign > 0:
            random_assigned_projects = random.sample(range(0, max_project), projects_to_assign)

            for project in random_assigned_projects:
                if students_projects_array[index][project] == 0:
                    students_projects_array[index][project] = 1
                    projects_to_assign -= 1
    return 