import tkinter as tk
from tkinter import ttk

class ProjectCreation(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="purple")
                
        self.controller = controller
        
        # label of frame ProjectCreation
        label = ttk.Label(self, text ="ProjectCreation")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)