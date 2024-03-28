import tkinter as tk
from tkinter import ttk
from solverProcess.action import solve

class SolverProcess(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")

        self.previous_frame = "solverInputFile"
        self.next_frame = "solverOutputManagment"
                        
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
        label = ttk.Label(self, text ="SolverProcess")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        # button to trigger solverProcess.action.solve
        button = ttk.Button(self, text ="Solve", command = lambda : solve([],[]))
        button.grid(row = 1, column = 0, padx = 10, pady = 10)
