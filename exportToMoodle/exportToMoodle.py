import tkinter as tk
from tkinter import ttk

class exportToMoodle(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")
                
        self.previous_frame = "projectManagment"
        self.next_frame = "solverInputFile"
        self.objective_fulfilled = True

        self.controller = controller
        self.show()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        self.show()
    
    def show(self):
        # label of frame exportToMoodle
        label = ttk.Label(self, text ="exportToMoodle")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)