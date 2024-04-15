import tkinter as tk
from customtkinter import CTkButton, CTkFrame
from topBar.actions import help

class TopBar(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent, height=50)
        self.pack(side="top", fill="x")

        self.controller = controller
        self.next, self.previous, self.objective_fulfilled = None, None, False

        self.reload()
         
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()      

        self.next, self.previous, self.objective_fulfilled = self.controller.get_np()

        self.show()
    
    def show(self):
        help_button = CTkButton(self, text="Prise en main de l'application (tutoriel)", command=lambda: help())
        help_button.pack(side = "left", padx = 20, pady = 20)

        next_button = CTkButton(self, text="Next", command=self.controller.show_next_frame, corner_radius=2, hover_color="purple")
        next_button.pack(side="right", padx = 20, pady = 10)
        
        previous_button = CTkButton(self, text="Previous", command=self.controller.show_previous_frame, corner_radius=2, hover_color="purple")
        previous_button.pack(side="right", padx = 20, pady = 10)

        if not self.previous:
            previous_button.configure(state='disabled')
        if not self.next or not self.objective_fulfilled:
            next_button.configure(state='disabled')
