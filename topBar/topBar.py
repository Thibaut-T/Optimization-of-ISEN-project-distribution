import tkinter as tk
from tkinter import ttk

class TopBar(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, height=50, bg="red")
        self.pack(side="top", fill="x")
                
        self.controller = controller
        
        # label of frame TopBar
        label = ttk.Label(self, text ="TopBar")
         
