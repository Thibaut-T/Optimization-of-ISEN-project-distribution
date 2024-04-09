import pandas as pd
from tkinter import filedialog
from projectCreation.action import generate_pdf_with_values

def getAllProjects():
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

    projects['Numéro du projet'] = projects['Numéro du projet'].apply(lambda x: x - 1)

    projects.to_excel('common/dataProjects.xlsx', index=False)

    controller.show_frame("projectManagment")
    
def savePdf():
    projects = getAllProjects()
    projects = projects.astype(str)  
    projects_dict = projects.to_dict('records') 
    generate_pdf_with_values(projects_dict)

def saveXml():
    filename = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
    