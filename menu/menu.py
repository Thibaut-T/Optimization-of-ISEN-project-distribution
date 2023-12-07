import tkinter as tk
from tkinter import ttk

class Menu(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, width=100, bg="blue")
        self.pack(side="left", fill="y")
        
        self.controller = controller
        
        # label of frame Menu
        label = ttk.Label(self, text ="Menu")
        
        label.grid(row=1, column=1, padx=10, pady=10)
        
        
        button1 = ttk.Button(self, text="manage projects",
                            command=lambda: controller.show_frame("projectManagement"))
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        button1 = ttk.Button(self, text="manage projects",
                            command=lambda: controller.show_frame("projectManagement"))
        button1.grid(row = 3, column = 1, padx = 10)
        
        button1 = ttk.Button(self, text="manage projects",
                            command=lambda: controller.show_frame("projectManagement"))
        button1.grid(row = 4, column = 1, padx = 10, pady = 10)
