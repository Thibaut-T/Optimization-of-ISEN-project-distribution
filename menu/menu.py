from customtkinter import CTkButton, CTkLabel, CTkFrame
from menu.action import reset

class Menu(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent, width=100)
        self.pack(side="left", fill="y")

        self.controller = controller

        self.menu = [
            "projectManagment",
            "exportToMoodle",
            "solverInputFile",
            "solverProcess",
            "solverOutputManagment",
            "exportStudentDistribution",
        ]

        self.reload()
         
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()

        self.show()
    
    def show(self):
        # label of frame Menu
        
        top_frame = CTkFrame(self)
        top_frame.pack()    

        bottom_frame = CTkFrame(self)
        bottom_frame.pack(side="bottom")

        label = CTkLabel(top_frame, text="Menu")
        label.grid(row=1, column=1, padx=10, pady=10)

        problem = False

        for i,frame in enumerate(self.menu):
            button = CTkButton(top_frame, text=frame, command=lambda frame=frame: self.controller.show_frame(frame))
            button.grid(row=2 + i, column=1, padx=5, pady=10)

            if i > 0 and (not self.controller.allFrames[self.controller.allFrames[frame].previous_frame].objective_fulfilled or problem):
                button.configure(state="disabled")
                problem = True

        button_reset = CTkButton(bottom_frame, text="Reset", command=lambda controller=self.controller: reset(controller))
        button_reset.pack(side="bottom", padx=10, pady=10)
