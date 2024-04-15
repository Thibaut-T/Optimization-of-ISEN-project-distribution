import tkinter as tk
from customtkinter import CTkButton, CTkFrame, CTkLabel
from solverProcess.action import solve
import os

class SolverProcess(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent)

        self.previous_frame = "solverInputFile"
        self.next_frame = "solverOutputManagement"
        self.objective_fulfilled = False
        self.controller = controller
        self.error = ""

        self.reload()

    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        self.objective_fulfilled = True if os.path.exists("./common/resultSolver.csv") else False
        self.show()

    def set_error(self, error):
        self.error = error
        self.reload()

    def show(self):
        label = CTkLabel(self, text ="SolverProcess")
        label.pack()

        centered_frame = CTkFrame(self)
        centered_frame.pack()

        # button to trigger solverProcess.action.solve
        button = CTkButton(centered_frame, text ="Solve", command = lambda controller = self.controller: self.set_error(solve(controller)))
        button.grid(row = 1, column = 0, padx = 10, pady = 10)

        if self.error:
            error = CTkLabel(centered_frame, text="Error: Failed to solve", fg="red")
            error.grid(row = 2, column = 0, padx = 10, pady = 10)