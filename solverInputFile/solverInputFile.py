import tkinter as tk
from tkinter import ttk

class SolverInputFile(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")
                
        self.controller = controller
        
        # label of frame SolverInputFile
        label = ttk.Label(self, text ="SolverInputFile")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
         
