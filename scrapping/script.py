import pandas as pd
import random
from collections import Counter

file_path = 'TEST3.xlsx'
data = pd.read_excel(file_path)

column_names = data.columns
project_columns = [col for col in column_names if col.startswith('Projet')]

text_content = ""

for index, row in data.iterrows():
    name = row['Adresse de messagerie']
    text_content += f'{name}\n'

    assigned_projects = set(project for project in project_columns if pd.notnull(row[project]))
    projects_to_assign = 5 - len(assigned_projects)
    
    graded_projects = []
    random_assigned_projects = []

    for project in project_columns:
        if projects_to_assign > 0 and project not in assigned_projects:
            random_project_grade = 0
            project_number = project.split()[-1]
            random_assigned_projects.append(f"Project {project_number}: {int(random_project_grade)} [Randomly Assigned]")
            projects_to_assign -= 1
        else:
            if pd.notnull(row[project]):
                grade_value = row[project]
                project_number = project.split()[-1]
                graded_projects.append(f"Project {project_number}: {int(grade_value)}")

    grade_counts = Counter(graded_projects)
    sorted_projects = sorted(graded_projects, key=lambda x: grade_counts[x], reverse=True)
    sorted_projects = sorted_projects[:5] + random_assigned_projects

    for project in sorted_projects:
        text_content += f"{project}\n"

    text_content += '\n'

text_file = 'outputFinal2.txt'
print("Analysis")
with open(text_file, 'w') as file:
    file.write(text_content)
