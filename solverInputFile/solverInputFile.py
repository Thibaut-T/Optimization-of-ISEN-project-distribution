import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import shutil
import pandas as pd
class SolverInputFile(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")
                
        self.previous_frame = "exportToMoodle"
        self.next_frame = "solverProcess"
                
        self.controller = controller
        self.show()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
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
            shutil.copy(filename, ".")
            data = pd.read_excel(filename)
            data_array = []
            num_projects = len([col for col in data.columns if 'Réponse' in col])
            project_numbers = ["Project number"] + [f"Project {i}" for i in range(1, num_projects + 1)]
            data_array.append(project_numbers)

            for index, row in data.iterrows():
                student_data = [f"{row['Nom de famille']} {row['Prénom']}"]
                grades = []
                for i in range(1, num_projects + 1):
                    try:
                        grade = int(row[f'Réponse {i}'])
                    except ValueError:
                        grade = 0  
                    grades.append(grade)
                non_zero_grades = [grade for grade in grades if grade != 0]
                while len(non_zero_grades) < 5:
                    grades.append(5)
                    non_zero_grades.append(5)

                top_grades = sorted(grades, reverse=True)[:5]
                student_data += [grade if grade in top_grades else 0 for grade in grades]

                data_array.append(student_data)

            print(data_array)



        

    
