import pandas as pd
import os

def getAllProjects():
    # try to get all projects 
    directory = 'common'
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        df = pd.read_excel('common/dataProjects.xlsx', dtype={'Phone number': str})
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Project number', 'Project name', 'Person in charge', 'Team emails', 'Phone number', 'Mail', 'Description', 'Minimum students', 'Maximum students', 'Company'])
        df.to_excel('common/dataProjects.xlsx', index=False)
    return df

def modifyProject(controller, i):
    
    try:
        with open('./common/currentCreation.txt', 'w') as file:
            file.write(str(i))
    except FileNotFoundError:
        with open('./common/currentCreation.txt', 'x') as file:
            file.write(str(i))

    controller.show_frame("projectCreation")

def createProject(controller):
    
    try:
        with open('./common/currentCreation.txt', 'w') as file:
            file.write(str(-1))
    except FileNotFoundError:
        with open('./common/currentCreation.txt', 'x') as file:
            file.write(str(-1))

    controller.show_frame("projectCreation")

def deleteProject(controller, i):
    projects = getAllProjects()
    projects = projects[projects['Project number'] != i]

    projects['Project number'] = projects['Project number'].apply(lambda x: int(x - 1) if x > i else int(x))

    projects.to_excel('common/dataProjects.xlsx', index=False)

    controller.show_frame("projectManagement")