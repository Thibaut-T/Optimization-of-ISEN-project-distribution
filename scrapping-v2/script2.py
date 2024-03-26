import pandas as pd
import random
import itertools
from numpy import transpose
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpBinary, LpAffineExpression

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

##################################################################
                
lp_file = 'output.lp'
text_content = ''
projects_students_array = transpose(students_projects_array)
max_students_per_project = 7
min_students_per_project = 3
bigM = 99999

##################################################################

model = LpProblem(name="assign_students_to_projects", sense=LpMaximize)

variables = {(i, j): LpVariable(name=f"s{i+1}p{j+1}", cat=LpBinary) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))}
binary_variables = {j: LpVariable(name=f"b{j}", cat=LpBinary) for j in range(len(projects_students_array))}

model += LpAffineExpression([(variables[i, j],students_projects_array[i][j]) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))])

for i in range(len(students_projects_array)):
    model += lpSum(variables[i, j] for j in range(len(students_projects_array[i]))) <= 1

for j in range(len(projects_students_array)):
    model += lpSum(variables[i, j] for i in range(len(projects_students_array[j]))) <= max_students_per_project

for j in range(len(projects_students_array)):
    model += lpSum(variables[i, j] for i in range(len(projects_students_array[j]))) <= bigM * binary_variables[j]

for j in range(len(projects_students_array)):
    model += lpSum(variables[i, j] for i in range(len(projects_students_array[j]))) >= min_students_per_project * binary_variables[j]



model.writeLP(lp_file)
model.solve()

result_array = [[variables[i, j].varValue for j in range(len(students_projects_array[i]))] for i in range(len(students_projects_array))]

print(result_array)

result_df = pd.DataFrame(result_array)
result_df.to_csv('result.csv', index=False)