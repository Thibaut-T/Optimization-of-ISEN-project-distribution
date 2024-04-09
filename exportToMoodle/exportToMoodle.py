import tkinter as tk
from tkinter import ttk
from exportToMoodle.action import save

class exportToMoodle(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")
                
        self.previous_frame = "projectManagment"
        self.next_frame = "solverInputFile"
        self.objective_fulfilled = True

        self.controller = controller
        self.reload()
    
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
        folder_name = tk.Label(self, text="Nom de la banque de questions:")
        folder_name.grid(row = 2, column = 0)
        entry = tk.Entry(self)
        entry.grid()
        save_button = ttk.Button(self, text="Download Moodle initialisation file", command=lambda moodle_folder=entry: save(moodle_folder))
        save_button.grid(row = 1, column = 0, padx = 10, pady = 10)