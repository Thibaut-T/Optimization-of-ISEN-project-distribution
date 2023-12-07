import tkinter as tk
from menu import menu
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
            "projectManagement": tk.Frame(window, bg="red"),
            "projectDistribution": tk.Frame(window, bg="blue"),
            "projectEvaluation": tk.Frame(window, bg="green")            
        }

        # Create a frame for the main content
        main_frame = tk.Frame(window, bg="white")
        main_frame.pack(side="right", fill="both", expand=True)
        
        

        # Start the main loop
        window.mainloop()

    def show_frame(self, page_name):
        frame = self.mainFrames[page_name]
        frame.tkraise()

mainApp().mainloop()