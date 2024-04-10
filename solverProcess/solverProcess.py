import tkinter as tk
from customtkinter import CTkButton, CTkFrame, CTkLabel
from solverProcess.action import solve
import os

class SolverProcess(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent)

        self.previous_frame = "solverInputFile"
        self.next_frame = "solverOutputManagment"
        self.objective_fulfilled = False
        self.controller = controller

        self.reload()

    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        self.objective_fulfilled = True if os.path.exists("./common/resultSolver.csv") else False
        self.show()

    def show(self):
        # label of frame SolverOutputManagment
        label = CTkLabel(self, text ="SolverProcess")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        # button to trigger solverProcess.action.solve
        button = CTkButton(self, text ="Solve", command = lambda controller = self.controller: solve(controller))
        button.grid(row = 1, column = 0, padx = 10, pady = 10)