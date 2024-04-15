import tkinter as tk
from customtkinter import CTkLabel, CTkFrame

class ExportStudentDistribution(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent)
        
        self.previous_frame = "solverOutputManagment"
        self.next_frame = ""
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
        # label of frame ExportStudentDistribution
        label = CTkLabel(self, text = "ExportStudentDistribution")
        label.pack()
        
        centered_frame = CTkFrame(self)
        centered_frame.pack()
