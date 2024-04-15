import pandas as pd
import os

def getAllProjects():
    directory = 'common'
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        df = pd.read_excel('common/dataProjects.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Numéro du projet', 'Intitulé', 'Proposé par', 'Equipe', 'Tél', 'Mail', 'Description', 'Minimum d\'étudiants', 'Maximum d\'étudiants', 'Entreprise'])
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
    projects = projects[projects['Numéro du projet'] != i]

    projects['Numéro du projet'] = projects['Numéro du projet'].apply(lambda x: int(x - 1) if x > i else int(x))

    projects.to_excel('common/dataProjects.xlsx', index=False)

    controller.show_frame("projectManagement")