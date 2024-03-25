import tkinter as tk
from tkinter import ttk

from projectManagment.getAllProjects import getAllProjects

class ProjectManagment(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="black")
                
        self.controller = controller
        
        # label of frame ProjectManagment
        label = ttk.Label(self, text ="ProjectManagment")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        button1 = ttk.Button(self, text="create a project", command=lambda: controller.show_frame("projectCreation"))
        button1.grid(row = 2, column = 0, padx = 10, pady = 10)

        for i, project in enumerate(getAllProjects()):
            project_label = ttk.Label(self, text=project)
            project_label.grid(row = i+5, column = 0, padx = 5, pady = 5)
            project_label_2 = ttk.Button(self, text="modifier", command=lambda: controller.show_frame("projectCreation"))
            project_label_2.grid(row = i+5, column = 1, padx = 5, pady = 5)
            project_label_3 = ttk.Button(self, text="supprimer", command=lambda: controller.show_frame("projectCreation"))
            project_label_3.grid(row = i+5, column = 2, padx = 5, pady = 5)
        
