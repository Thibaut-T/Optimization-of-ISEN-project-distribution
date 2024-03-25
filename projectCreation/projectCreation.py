import tkinter as tk
from tkinter import ttk
from projectCreation.pdf import finish_pdf, generate_pdf, generate_pdf_with_values


class ProjectCreation(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="purple")
                
        self.controller = controller
        input_values = []
        # label of frame ProjectCreation
        label = ttk.Label(self, text ="ProjectCreation")
        label.pack()

        generate_pdf_with_values(input_values)
       

        label1 = tk.Label(self, text="Numéro du projet:")
        label1.pack()
        entry1 = tk.Entry(self)
        entry1.pack()

        label2 = tk.Label(self, text="Intitulé du sujet:")
        label2.pack()
        entry2 = tk.Entry(self)
        entry2.pack()

        label3 = tk.Label(self, text="Proposé par :")
        label3.pack()
        entry3 = tk.Entry(self)
        entry3.pack()

        label4 = tk.Label(self, text="Equipe:")
        label4.pack()
        entry4 = tk.Entry(self)
        entry4.pack()

        label5 = tk.Label(self, text="Tél:")
        label5.pack()
        entry5 = tk.Entry(self)
        entry5.pack()

        label6 = tk.Label(self, text="Mail:")
        label6.pack()
        entry6 = tk.Entry(self)
        entry6.pack()

        label7 = tk.Label(self, text="Description:")
        label7.pack()
        entry7 = tk.Text(self, height=5)
        entry7.pack()

        generate_button = tk.Button(self, text="Add Project", command=generate_pdf)
        generate_button.pack()

        finish_button = tk.Button(self, text="Finish PDF", command=finish_pdf)
        finish_button.pack()