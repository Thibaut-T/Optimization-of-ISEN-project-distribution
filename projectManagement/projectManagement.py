import tkinter.ttk as ttk
from customtkinter import CTkButton, CTkLabel, CTkFrame, CTkScrollableFrame, HORIZONTAL, VERTICAL
import pandas as pd
from projectManagement.actions import modifyProject, createProject, deleteProject, getAllProjects

class ProjectManagement(CTkFrame):
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
            self.projects = getAllProjects()[['Project number','Project name', 'Person in charge']]
        except FileNotFoundError:
            self.projects = pd.DataFrame()
        
        self.objective_fulfilled = len(self.projects)>0

        self.show()
    
    def show(self):        
        # label of frame ProjectManagement
        label = CTkLabel(self, text ="ProjectManagement")
        label.pack(pady=10,padx=10)

        button1 = CTkButton(self, text="create a project", command=lambda: createProject(self.controller))
        button1.pack(pady=10,padx=10)

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
        

        project_label_titles = CTkLabel(sub_frame, text='Project number')
        project_label_titles.grid(row = 4, column = 0, padx = 5, pady = 5)
        project_label_titles_1 = CTkLabel(sub_frame, text='Project name')
        project_label_titles_1.grid(row = 4, column = 1, padx = 5, pady = 5)
        project_label_titles_2 = CTkLabel(sub_frame, text='Person in charge')
        project_label_titles_2.grid(row = 4, column = 2, padx = 5, pady = 5)
        project_label_titles_3 = CTkLabel(sub_frame, text='Action')
        project_label_titles_3.grid(row = 4, column = 3, columnspan = 2, padx = 5, pady = 5)

        separator = ttk.Separator(sub_frame, orient=HORIZONTAL)
        separator.grid(column=0, row=5, columnspan=5, sticky='ew')

        for i, project in self.projects.iterrows():
            project_label = CTkLabel(sub_frame, text=project['Project number'])
            project_label.grid(row = 2*i+6, column = 0, padx = 5, pady = 5)
            project_label_1 = CTkLabel(sub_frame, text=project['Project name'])
            project_label_1.grid(row = 2*i+6, column = 1, padx = 5, pady = 5)
            project_label_1 = CTkLabel(sub_frame, text=project['Person in charge'])
            project_label_1.grid(row = 2*i+6, column = 2, padx = 5, pady = 5)
            project_label_2 = CTkButton(sub_frame, text="modify", command=lambda index=project['Project number']: modifyProject(self.controller, index))
            project_label_2.grid(row = 2*i+6, column = 3, padx = 5, pady = 5)
            project_label_3 = CTkButton(sub_frame, text="delete", command=lambda index=project['Project number']: deleteProject(self.controller, index))
            project_label_3.grid(row = 2*i+6, column = 4, padx = 5, pady = 5)
            
            separator = CTkFrame(sub_frame, bg_color="grey", height=1)
            separator.grid(row = 2*i+7, column = 0, columnspan = 5, sticky="ew")