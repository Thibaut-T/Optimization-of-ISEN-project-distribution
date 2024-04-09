import tkinter as tk
from tkinter import ttk
import pandas as pd
from projectManagment.actions import modifyProject, createProject, deleteProject, getAllProjects, savePdf, saveXml
from tkinter import PhotoImage

image_path = "Sécurité-routière-glissière-bois-métal-TLC18-3.png"

class ProjectManagment(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="lightgrey")

        self.previous_frame = ""
        self.next_frame = "exportToMoodle"
        self.projects = pd.DataFrame()
        self.controller = controller
        self.objective_fulfilled = False

        self.reload()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()

        try:
            self.projects = getAllProjects()[['Numéro du projet','Intitulé', 'Proposé par']]
        except FileNotFoundError:
            self.projects = pd.DataFrame()
        
        self.objective_fulfilled = len(self.projects)>0

        self.show()
    
    def show(self):        
        # label of frame ProjectManagment
        label = ttk.Label(self, text ="ProjectManagment")
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="create a project", command=lambda: createProject(self.controller))
        button1.pack(pady=10,padx=10)
        button2 = ttk.Button(self, text="save pdf of all projects", command=lambda: savePdf())
        button2.pack(pady=10,padx=10)
        button3 = ttk.Button(self, text="save xml of all projects", command=lambda: saveXml())
        button3.pack(pady=10,padx=10)

        # Cadre droit avec un poids de 1
        sub_frame = tk.Frame(self, bg="green")
        sub_frame.pack(side="bottom", fill="both", expand=True)

        canvas = tk.Canvas(sub_frame, bd=0)
        scrollbary = tk.Scrollbar(sub_frame, orient="vertical", command=canvas.yview)
        scrollbary.pack(side="right", fill="y")

        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbary.set)

        # Conteneur pour les éléments dans le Canvas
        # Calcul des coordonnées au milieu de la fenêtre
        # Coordonnée x au milieu de la fenêtre
        
        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((self.winfo_width(), 0), window=scrollable_frame, anchor="nw")

        scrollable_frame.grid_columnconfigure(0, weight=1)  # Colonne 0
        scrollable_frame.grid_columnconfigure(1, weight=1)  # Colonne 1
        scrollable_frame.grid_columnconfigure(2, weight=1)
        scrollable_frame.grid_columnconfigure(3, weight=1)  # Colonne 1
        scrollable_frame.grid_columnconfigure(4, weight=1)
        

        project_label_titles = ttk.Label(scrollable_frame, text='Numéro du projet')
        project_label_titles.grid(row = 4, column = 0, padx = 5, pady = 5)
        project_label_titles_1 = ttk.Label(scrollable_frame, text='Intitulé')
        project_label_titles_1.grid(row = 4, column = 1, padx = 5, pady = 5)
        project_label_titles_2 = ttk.Label(scrollable_frame, text='Proposé par')
        project_label_titles_2.grid(row = 4, column = 2, padx = 5, pady = 5)

        for i, project in self.projects.iterrows():
            project_label = ttk.Label(scrollable_frame, text=project['Numéro du projet'])
            project_label.grid(row = i+5, column = 0, padx = 5, pady = 5)
            project_label_1 = ttk.Label(scrollable_frame, text=project['Intitulé'])
            project_label_1.grid(row = i+5, column = 1, padx = 5, pady = 5)
            project_label_1 = ttk.Label(scrollable_frame, text=project['Proposé par'])
            project_label_1.grid(row = i+5, column = 2, padx = 5, pady = 5)
            project_label_2 = ttk.Button(scrollable_frame, text="modifier", command=lambda index=project['Numéro du projet']: modifyProject(self.controller, index))
            project_label_2.grid(row = i+5, column = 3, padx = 5, pady = 5)
            project_label_3 = ttk.Button(scrollable_frame, text="supprimer", command=lambda index=project['Numéro du projet']: deleteProject(self.controller, index))
            project_label_3.grid(row = i+5, column = 4, padx = 5, pady = 5)

        # Configurer le Canvas pour le défilement
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        