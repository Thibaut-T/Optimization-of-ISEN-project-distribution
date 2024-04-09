import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import shutil
import os
import pandas as pd
class SolverInputFile(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")
                
        self.previous_frame = "exportToMoodle"
        self.next_frame = "solverProcess"
        self.controller = controller
        self.objective_fulfilled = False

        self.reload()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        self.objective_fulfilled = os.path.exists("./common/answerProjects.xlsx")

        self.show()
    
    def show(self):
        # label of frame SolverInputFile
        label = ttk.Label(self, text ="SolverInputFile")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        open_file_button = ttk.Button(self, text="Open File", command=self.open_file)
        open_file_button.grid(row=1, column=0, padx=10, pady=10)
  
    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

        if filename:
            if os.path.exists(f"./common/{os.path.basename(filename)}"):
                os.remove(f"./common/{os.path.basename(filename)}")
            os.remove(f"./common/answerProjects.xlsx")
            
            shutil.copy(filename, "./common")
            os.rename(f"./common/{os.path.basename(filename)}", f"./common/answerProjects.xlsx")
        self.controller.show_frame("solverInputFile")


