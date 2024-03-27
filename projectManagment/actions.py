import pandas as pd
from tkinter import filedialog

def getAllProjects():
    try:
        df = pd.read_excel('output.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Numéro du projet', 'Intitulé', 'Proposé par', 'Equipe', 'Tél', 'Mail', 'Description', 'Minimum d\'étudiants', 'Maximum d\'étudiants', 'Entreprise'])
        df.to_excel('output.xlsx', index=False)
    return df

def modifyProject(controller, i):
    print("modifyProject")
    try:
        with open('./common/data.txt', 'w') as file:
            file.write(str(i))
    except FileNotFoundError:
        with open('./common/data.txt', 'x') as file:
            file.write(str(i))

    controller.show_frame("projectCreation")

def createProject(controller):
    print("createProject")
    try:
        with open('./common/data.txt', 'w') as file:
            file.write(str(-1))
    except FileNotFoundError:
        with open('./common/data.txt', 'x') as file:
            file.write(str(-1))

    controller.show_frame("projectCreation")

def deleteProject(controller, i):
    projects = getAllProjects()
    projects = projects[projects['Numéro du projet'] != i]
    projects.to_excel('output.xlsx', index=False)

    controller.show_frame("projectManagment")

def savePdf():
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    print(filename)

def saveXml():
    filename = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
    print(filename)