import tkinter as tk
from tkinter import ttk
from topBar.actions import Help

class TopBar(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, height=50, bg="red")
        self.pack(side="top", fill="x")

        self.controller = controller

        self.next, self.previous, self.objective_fulfilled = self.controller.get_np()

        self.show()
         
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()

        

        self.next, self.previous, self.objective_fulfilled = self.controller.get_np()

        self.show()
    
    def show(self):
        help_button = ttk.Button(self, text="Prise en main de l'application (tutoriel)", command=lambda: Help())
        help_button.pack(side = "left", padx = 20, pady = 20)

        next_button = ttk.Button(self, text="Next", command=self.controller.show_next_frame)
        next_button.pack(side="right", padx = 20, pady = 20)
        
        previous_button = ttk.Button(self, text="Previous", command=self.controller.show_previous_frame)
        previous_button.pack(side="right", padx = 20, pady = 20)

        if not self.previous:
            previous_button.config(state='disabled')
        if not self.next or not self.objective_fulfilled:
            next_button.config(state='disabled')
