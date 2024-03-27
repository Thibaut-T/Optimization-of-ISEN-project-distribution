import tkinter as tk

class CustomFrame(tk.Frame):
    def __init__(self, parent):
        pass

    def reload(self, parent, controller):
        CustomFrame.__init__(self, parent, controller)