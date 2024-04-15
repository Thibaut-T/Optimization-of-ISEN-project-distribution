import tkinter as tk
from customtkinter import CTkButton, CTkFrame, CTkLabel
from tkinter import filedialog
import shutil
import os
import pandas as pd
class SolverInputFile(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent)
                
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
        label = CTkLabel(self, text = "SolverInputFile")
        label.pack()

        centered_frame = CTkFrame(self)
        centered_frame.pack()

        open_file_button = CTkButton(centered_frame, text="Open File", command=self.open_file)
        open_file_button.grid(row=1, column=0, padx=10, pady=10)
  
    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

        # copy the file to the common folder
        if filename:
            if os.path.exists(f"./common/{os.path.basename(filename)}"):
                os.remove(f"./common/{os.path.basename(filename)}")

            if os.path.exists("./common/answerProjects.xlsx"):
                os.remove(f"./common/answerProjects.xlsx")

            shutil.copy(filename, "./common")

            # rename the file to answerProjects.xlsx
            os.rename(f"./common/{os.path.basename(filename)}", f"./common/answerProjects.xlsx")
        self.controller.show_frame("solverInputFile")


