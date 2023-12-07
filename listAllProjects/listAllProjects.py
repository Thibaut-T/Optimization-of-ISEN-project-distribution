import tkinter as tk
from tkinter import ttk

class ListAllProjects(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")
        self.pack(side="right", fill="both", expand=True)
                
        self.controller = controller
        
        # label of frame ListAllProjects
        label = ttk.Label(self, text ="ListAllProjects")
         
