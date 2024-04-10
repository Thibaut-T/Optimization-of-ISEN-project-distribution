import customtkinter as ctk
from exportStudentDistribution import exportStudentDistribution
from exportToMoodle import exportToMoodle
from menu import menu
from projectCreation import projectCreation
from projectManagment import projectManagment
from solverInputFile import solverInputFile
from solverProcess import solverProcess
from solverOutputManagment import solverOutputManagment
from topBar import topBar
import traceback

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title("My Window")

        # Set the window size
        self.minsize(width=800, height=600)

        self.allFrames = {
            "projectCreation": projectCreation.ProjectCreation(self, self),
            "projectManagment": projectManagment.ProjectManagment(self, self),
            "exportToMoodle": exportToMoodle.exportToMoodle(self, self),
            "solverInputFile": solverInputFile.SolverInputFile(self, self),
            "solverProcess": solverProcess.SolverProcess(self, self),
            "solverOutputManagment": solverOutputManagment.SolverOutputManagment(self, self),
            "exportStudentDistribution": exportStudentDistribution.ExportStudentDistribution(self, self),
        }
                
        self.mainFrame = self.allFrames["projectManagment"]

        # Create a frame for the top bar
        self.topBarFrame = topBar.TopBar(self, self)

        # Create a frame for the menu
        self.menuFrame = menu.Menu(self, self)

        self.mainFrame.pack(fill="both", expand=True)

        try:
            self.mainloop()
        except RecursionError:
            traceback.print_exc()
            
        
    def show_frame(self, page_name):
        self.mainFrame.pack_forget()
        self.mainFrame = self.allFrames[page_name]
        self.mainFrame.pack(fill="both", expand=True)
        self.mainFrame.reload()
        self.topBarFrame.reload()
        self.menuFrame.reload()
        self.mainFrame.tkraise()

    def show_next_frame(self):
        self.show_frame(self.mainFrame.next_frame)

    def show_previous_frame(self):
        self.show_frame(self.mainFrame.previous_frame)

    def get_np(self):
        return self.mainFrame.next_frame, self.mainFrame.previous_frame, self.mainFrame.objective_fulfilled

MainApp().mainloop()