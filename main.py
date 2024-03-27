import tkinter as tk
from exportStudentDistribution import exportStudentDistribution
from exportToMoodle import exportToMoodle
from listAllProjects import listAllProjects
from menu import menu
from projectCreation import projectCreation
from projectManagment import projectManagment
from solverInputFile import solverInputFile
from solverProcess import solverProcess
from solverOutputManagment import solverOutputManagment
from topBar import topBar
import traceback

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title("My Window")

        # Set the window size
        self.minsize(width=800, height=600)

        self.allFrames = {
            "projectCreation": projectCreation.ProjectCreation(self, self),
            "projectManagment": projectManagment.ProjectManagment(self, self),
            "solverInputFile": solverInputFile.SolverInputFile(self, self),
            "solverProcess": solverProcess.SolverProcess(self, self),
            "solverOutputManagment": solverOutputManagment.SolverOutputManagment(self, self),
            "exportStudentDistribution": exportStudentDistribution.ExportStudentDistribution(self, self),
            "exportToMoodle": exportToMoodle.exportToMoodle(self, self),
            "listAllProjects": listAllProjects.ListAllProjects(self, self)
        }
                
        self.mainFrame = self.allFrames["projectManagment"]

        # Create a frame for the top bar
        self.topBarFrame = topBar.TopBar(self, self)

        # Create a frame for the menu
        self.menu_frame = menu.Menu(self, self)

        self.mainFrame.pack(fill="both", expand=True)

        try:
            self.mainloop()
        except RecursionError:
            print(traceback.format_exc())
        
    def show_frame(self, page_name):
        self.mainFrame.pack_forget()
        self.mainFrame = self.allFrames[page_name]
        self.mainFrame.pack(fill="both", expand=True)
        self.mainFrame.reload()
        self.topBarFrame.reload()
        self.mainFrame.tkraise()

    def show_next_frame(self):
        self.mainFrame.pack_forget()
        self.mainFrame = self.allFrames[self.mainFrame.next_frame]
        self.mainFrame.pack(fill="both", expand=True)
        self.mainFrame.reload()
        self.topBarFrame.reload()
        self.mainFrame.tkraise()

    def show_previous_frame(self):
        self.mainFrame.pack_forget()
        self.mainFrame = self.allFrames[self.mainFrame.previous_frame]
        self.mainFrame.pack(fill="both", expand=True)
        self.mainFrame.reload()
        print("show previous frame")
        self.topBarFrame.reload()
        self.mainFrame.tkraise()

    def get_np(self):
        return self.mainFrame.next_frame, self.mainFrame.previous_frame

MainApp().mainloop()