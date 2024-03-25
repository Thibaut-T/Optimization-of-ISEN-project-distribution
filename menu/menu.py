import tkinter as tk
from tkinter import ttk

class Menu(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, width=100, bg="blue")
        self.pack(side="left", fill="y")
        
        self.controller = controller
        
        # label of frame Menu
        label = ttk.Label(self, text ="Menu")
        
        label.grid(row=1, column=1, padx=10, pady=10)
        
        
        button1 = ttk.Button(self, text="manage projects",
                            command=lambda: controller.show_frame("projectManagment"))
        button1.grid(row = 3, column = 1, padx = 10)
        
        button2 = ttk.Button(self, text="create a project",
                            command=lambda: controller.show_frame("projectCreation"))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text="upload forms output file",
                            command=lambda: controller.show_frame("solverInputFile"))
        button3.grid(row = 4, column = 1, padx = 10, pady = 10)

        button4 = ttk.Button(self, text="Optimisation results",
                            command=lambda: controller.show_frame("solverOutputManagment"))
        button4.grid(row = 5, column = 1, padx = 10)
        
        button5 = ttk.Button(self, text="Export optimisation results to pdf",
                            command=lambda: controller.show_frame("exportStudentDistribution"))
        button5.grid(row = 6, column = 1, padx = 10, pady = 10)
        
        button6 = ttk.Button(self, text="Export project list to forms",
                            command=lambda: controller.show_frame("exportToForms"))
        button6.grid(row = 7, column = 1, padx = 10)
        
        button7 = ttk.Button(self, text="list of all students projects",
                            command=lambda: controller.show_frame("listAllProjects"))
        button7.grid(row = 8, column = 1, padx = 10, pady = 10)