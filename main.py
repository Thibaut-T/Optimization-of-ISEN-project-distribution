import tkinter as tk
from exportStudentDistribution import exportStudentDistribution
from exportToForms import exportToForms
from listAllProjects import listAllProjects
from menu import menu
from projectCreation import projectCreation
from projectManagment import projectManagment
from solverInputFile import solverInputFile
from solverOutputManagment import solverOutputManagment
from topBar import topBar

class mainApp(tk.Tk):
    def __init__(self):
        # Create the main window
        window = tk.Tk()

        # Set the window title
        window.title("My Window")

        # Set the window size
        window.minsize(width=800, height=600)

        # Create a frame for the top bar
        top_bar_frame = topBar.TopBar(window, self)

        # Create a frame for the menu
        menu_frame = menu.Menu(window, self)

        self.mainFrames = {
            "projectCreation": projectCreation.ProjectCreation(window, self),
            "projectManagment": projectManagment.ProjectManagment(window, self),
            "solverInputFile": solverInputFile.SolverInputFile(window, self),
            "solverOutputManagment": solverOutputManagment.SolverOutputManagment(window, self),
            "exportStudentDistribution": exportStudentDistribution.ExportStudentDistribution(window, self),
            "exportToForms": exportToForms.ExportToForms(window, self),
            "listAllProjects": listAllProjects.ListAllProjects(window, self)
        }
                
        self.main_frame = self.mainFrames["projectCreation"]
        self.main_frame.pack(fill="both", expand=True)

        # Start the main loop
        window.mainloop()

    def show_frame(self, page_name):
        self.main_frame.pack_forget()
        self.main_frame = self.mainFrames[page_name]
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.tkraise()

mainApp().mainloop()