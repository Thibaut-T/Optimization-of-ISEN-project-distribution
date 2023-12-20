import pandas as pd
import random
import itertools
from numpy import transpose

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

for i in range(len(students_projects_array)):
    for j in range(len(students_projects_array[i])):
        text_content += f"var s{i+1}p{j+1} binary;\n"
        
for j in range(len(projects_students_array)):
    text_content += f"var b{j} binary;\n"

####à enlever : variables non utilisées

##################################################################

text_content += '\n'
text_content += 'maximize\n obj: '

for i in range(len(students_projects_array)):
    for j in range(len(students_projects_array[i])):
        if(students_projects_array[i][j] != 0):
            text_content += f"s{i+1}p{j+1} * {students_projects_array[i][j]} + "

text_content = text_content[:-3]
text_content += ';\n\n'

##################################################################

for i in range(len(students_projects_array)):
    tmp = f"subject to cst_binary_stud_{i}: "
    for j in range(len(students_projects_array[i])):
        tmp += f"s{i+1}p{j+1} + "
    tmp = tmp[:-3]
    text_content += tmp
    text_content += f" <= 1;\n"

##################################################################    
    
for j in range(len(projects_students_array)):
    tmp = f"subject to cst_max_stud_{j}: "
    for i in range(len(projects_students_array[j])):
        tmp += f"s{i+1}p{j+1} + "
    tmp = tmp[:-3]
    text_content += tmp
    text_content += f" <= {max_students_per_project};\n"
    
##################################################################
    
for j in range(len(projects_students_array)):
    tmp = f"subject to constraint_min_1_student_for_project_{j}: "
    
    tmp2 = ""
    for i in range(len(projects_students_array[j])):
        if projects_students_array[j][i] != 0:
            tmp2 += f"s{i+1}p{j+1} + "
            
    if tmp2 != "":
        tmp += tmp2
        tmp = tmp[:-3]
        tmp += f" <= {bigM} * b{j};\n"
    
        text_content += tmp
    
##################################################################

for j in range(len(projects_students_array)):
    tmp = f"subject to constraint_min_2_student_for_project_{j}: "
    
    tmp2 = ""
    for i in range(len(projects_students_array[j])):
        if projects_students_array[j][i] != 0:
            tmp2 += f"s{i+1}p{j+1} + "
            
    if tmp2 != "":
        tmp += tmp2
        tmp = tmp[:-3]
        tmp += f" <= {bigM} * b{j};\n"
    
        text_content += tmp

##################################################################

with open(lp_file, 'w') as file:
    file.write(text_content)

########################################
# plusieurs modèles liés à l'application




# conditions de base pour le minimum : >= 3b 
# avec b un composite de binaires du type "si le nombre minimal d'étudiant est assigné au projet = 1"
# cplex



# sommes des vars -(s1p1*s2p1*s3p1 + s2p1*s3p1*s4p1 + ... + s7p1*s8p1*s9p1)*(1-BIGM)