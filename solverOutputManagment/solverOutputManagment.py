import tkinter as tk
from tkinter import ttk

class SolverOutputManagment(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")

        self.previous_frame = "solverProcess"
        self.next_frame = "exportStudentDistribution"
                
        self.controller = controller
        self.show()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        self.show()
    
    def show(self):
        # label of frame SolverOutputManagment
        label = ttk.Label(self, text ="SolverOutputManagment")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
