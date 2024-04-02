import tkinter as tk
from tkinter import ttk
from exportToMoodle.action import save

class exportToMoodle(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")
                
        self.previous_frame = "projectManagment"
        self.next_frame = "solverInputFile"

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

        # save button
        save_button = ttk.Button(self, text="Download Moodle initialisation file", command=save)
        save_button.grid(row = 1, column = 0, padx = 10, pady = 10)