import tkinter as tk
from tkinter import ttk

class TopBar(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, height=50, bg="red")
        self.pack(side="top", fill="x")

        self.controller = controller

        self.next, self.previous = self.controller.get_np()

        self.show()
         
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()

        print("reload topBar")

        self.next, self.previous = self.controller.get_np()

        self.show()
    
    def show(self):
        # label of frame TopBar
        label = ttk.Label(self, text ="TopBar")
        label.pack(side="left", padx = 10, pady = 10)

        next_button = ttk.Button(self, text="Next", command=self.controller.show_next_frame)
        next_button.pack(side="right", padx = 10, pady = 10)
        
        previous_button = ttk.Button(self, text="Previous", command=self.controller.show_previous_frame)
        previous_button.pack(side="right", padx = 10, pady = 10)

        if not self.previous:
            previous_button.config(state='disabled')
        if not self.next:
            next_button.config(state='disabled')
