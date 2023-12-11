import tkinter as tk
from tkinter import ttk

class ProjectManagment(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="black")
                
        self.controller = controller
        
        # label of frame ProjectManagment
        label = ttk.Label(self, text ="ProjectManagment")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        button1 = ttk.Button(self, text="manage projects", command=lambda: controller.show_frame("projectManagment"))
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)
        
         
