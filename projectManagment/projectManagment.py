import tkinter as tk
from customtkinter import CTkButton, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar, CTkScrollableFrame
import pandas as pd
from projectManagment.actions import modifyProject, createProject, deleteProject, getAllProjects, savePdf

class ProjectManagment(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent)

        self.previous_frame = ""
        self.next_frame = "exportToMoodle"
        self.projects = pd.DataFrame()
        self.controller = controller
        self.objective_fulfilled = False

        self.reload()

    def recursive_destroy(self, item):
        if item.winfo_children():
            for item2 in item.winfo_children():
                self.recursive_destroy(item2)
        item.destroy()
    
    def reload(self):
        children = self.winfo_children()
        
        for child in children:
            self.recursive_destroy(child)

        try:
            self.projects = getAllProjects()[['Numéro du projet','Intitulé', 'Proposé par']]
        except FileNotFoundError:
            self.projects = pd.DataFrame()
        
        self.objective_fulfilled = len(self.projects)>0

        self.show()
    
    def show(self):        
        # label of frame ProjectManagment
        label = CTkLabel(self, text ="ProjectManagment")
        label.pack(pady=10,padx=10)

        button1 = CTkButton(self, text="create a project", command=lambda: createProject(self.controller))
        button1.pack(pady=10,padx=10)
        button2 = CTkButton(self, text="save pdf of all projects", command=lambda: savePdf())
        button2.pack(pady=10,padx=10)

        # Cadre droit avec un poids de 1
        sub_frame = CTkScrollableFrame(self)
        sub_frame.pack(side="bottom", fill="both", expand=True)

        # Conteneur pour les éléments dans le Canvas
        # Calcul des coordonnées au milieu de la fenêtre
        # Coordonnée x au milieu de la fenêtre

        sub_frame.grid_columnconfigure(0, weight=1)  # Colonne 0
        sub_frame.grid_columnconfigure(1, weight=1)  # Colonne 1
        sub_frame.grid_columnconfigure(2, weight=1)
        sub_frame.grid_columnconfigure(3, weight=1)  # Colonne 1
        sub_frame.grid_columnconfigure(4, weight=1)
        

        project_label_titles = CTkLabel(sub_frame, text='Numéro du projet')
        project_label_titles.grid(row = 4, column = 0, padx = 5, pady = 5)
        project_label_titles_1 = CTkLabel(sub_frame, text='Intitulé')
        project_label_titles_1.grid(row = 4, column = 1, padx = 5, pady = 5)
        project_label_titles_2 = CTkLabel(sub_frame, text='Proposé par')
        project_label_titles_2.grid(row = 4, column = 2, padx = 5, pady = 5)

        for i, project in self.projects.iterrows():
            project_label = CTkLabel(sub_frame, text=project['Numéro du projet'])
            project_label.grid(row = i+5, column = 0, padx = 5, pady = 5)
            project_label_1 = CTkLabel(sub_frame, text=project['Intitulé'])
            project_label_1.grid(row = i+5, column = 1, padx = 5, pady = 5)
            project_label_1 = CTkLabel(sub_frame, text=project['Proposé par'])
            project_label_1.grid(row = i+5, column = 2, padx = 5, pady = 5)
            project_label_2 = CTkButton(sub_frame, text="modifier", command=lambda index=project['Numéro du projet']: modifyProject(self.controller, index))
            project_label_2.grid(row = i+5, column = 3, padx = 5, pady = 5)
            project_label_3 = CTkButton(sub_frame, text="supprimer", command=lambda index=project['Numéro du projet']: deleteProject(self.controller, index))
            project_label_3.grid(row = i+5, column = 4, padx = 5, pady = 5)
        