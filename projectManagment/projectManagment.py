import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
from projectManagment.actions import modifyProject, createProject, deleteProject, getAllProjects, savePdf, saveXml

class ProjectManagment(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="black")

        self.previous_frame = ""
        self.next_frame = "exportToMoodle"

        self.controller = controller
        self.show()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        self.show()
    
    def show(self):        
        # label of frame ProjectManagment
        label = ttk.Label(self, text ="ProjectManagment")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        button1 = ttk.Button(self, text="create a project", command=lambda: createProject(self.controller))
        button1.grid(row = 2, column = 0, padx = 10, pady = 10)
        button2 = ttk.Button(self, text="save pdf of all projects", command=lambda: savePdf())
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text="save xml of all projects", command=lambda: saveXml())
        button2.grid(row = 2, column = 2, padx = 10, pady = 10)

        project_label_titles = ttk.Label(self, text='Numéro du projet')
        project_label_titles.grid(row = 4, column = 0, padx = 5, pady = 5)
        project_label_titles_1 = ttk.Label(self, text='Intitulé')
        project_label_titles_1.grid(row = 4, column = 1, padx = 5, pady = 5)
        project_label_titles_2 = ttk.Label(self, text='Proposé par')
        project_label_titles_2.grid(row = 4, column = 2, padx = 5, pady = 5)

        try:
            projects = getAllProjects()[['Numéro du projet','Intitulé', 'Proposé par']]
        except FileNotFoundError:
            projects = pd.DataFrame()

        for i, project in projects.iterrows():
            project_label = ttk.Label(self, text=project['Numéro du projet'])
            project_label.grid(row = i+5, column = 0, padx = 5, pady = 5)
            project_label_1 = ttk.Label(self, text=project['Intitulé'])
            project_label_1.grid(row = i+5, column = 1, padx = 5, pady = 5)
            project_label_1 = ttk.Label(self, text=project['Proposé par'])
            project_label_1.grid(row = i+5, column = 2, padx = 5, pady = 5)
            project_label_2 = ttk.Button(self, text="modifier", command=lambda index=project['Numéro du projet']: modifyProject(self.controller, index))
            project_label_2.grid(row = i+5, column = 3, padx = 5, pady = 5)
            project_label_3 = ttk.Button(self, text="supprimer", command=lambda index=project['Numéro du projet']: deleteProject(self.controller, index))
            project_label_3.grid(row = i+5, column = 4, padx = 5, pady = 5)