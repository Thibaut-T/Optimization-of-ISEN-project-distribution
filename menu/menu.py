import tkinter as tk
from tkinter import ttk

class Menu(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, width=100, bg="blue")
        self.pack(side="left", fill="y")

        self.controller = controller

        self.menu = [
            "projectManagment",
            "exportToMoodle",
            "solverInputFile",
            "solverProcess",
            "solverOutputManagment",
            "exportStudentDistribution",
        ]

        self.show()
         
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()

        self.show()
    
    def show(self):
        # label of frame Menu
        label = ttk.Label(self, text ="Menu")
        label.grid(row=1, column=1, padx=10, pady=10)

        problem = False

        for i,frame in enumerate(self.menu):
            button = ttk.Button(self, text=frame, command=lambda frame=frame: self.controller.show_frame(frame))
            button.grid(row=2 + i, column=1, padx=10, pady=(10 if i%2==0 else 0))

            if i > 0 and (not self.controller.allFrames[self.controller.allFrames[frame].previous_frame].objective_fulfilled or problem):
                button.configure(state="disabled")
                problem = True