import tkinter as tk
from tkinter import ttk
import pandas as pd
from projectCreation.pdf import finish_pdf, generate_pdf, generate_pdf_with_values

class ProjectCreation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="purple")

        self.previous_frame = ""
        self.next_frame = ""

        self.controller = controller
        self.show()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        self.show()
    
    def show(self):
        input_values = []
        # label of frame ProjectCreation
        label = ttk.Label(self, text ="ProjectCreation")
        label.pack()


        idCurrent = -1
        try:
            with open('./common/data.txt', 'r') as file:
                first_line = file.readline()
                if first_line.strip():
                    try:
                        idCurrent = int(first_line)
                    except ValueError:
                        idCurrent = first_line
        except FileNotFoundError:
            idCurrent = -1
        if idCurrent != -1:
            try:
                df = pd.read_excel('output.xlsx')
                filtered_df = df[df['Numéro du projet'] == idCurrent]

                entry1Text = filtered_df['Numéro du projet'].values[0] if not filtered_df.empty else ""
                entry2Text = filtered_df['Intitulé'].values[0] if not filtered_df.empty else ""
                entry3Text = filtered_df['Proposé par'].values[0] if not filtered_df.empty else ""
                entry4Text = filtered_df['Equipe'].values[0] if not filtered_df.empty else ""
                entry5Text = filtered_df['Tél'].values[0] if not filtered_df.empty else ""
                entry6Text = filtered_df['Mail'].values[0] if not filtered_df.empty else ""
                entry7Text = filtered_df['Description'].values[0] if not filtered_df.empty else ""
                entry8Text = filtered_df['Minimum d\'étudiants'].values[0] if not filtered_df.empty else ""
                entry9Text = filtered_df['Maximum d\'étudiants'].values[0] if not filtered_df.empty else ""
                entry10Text = filtered_df['Entreprise'].values[0] if not filtered_df.empty else ""
            except FileNotFoundError:
                entry1Text = ""
                entry2Text = ""
                entry3Text = ""
                entry4Text = ""
                entry5Text = ""
                entry6Text = ""
                entry7Text = ""
                entry8Text = ""
                entry9Text = ""
                entry10Text = ""
        else:
            entry1Text = ""
            entry2Text = ""
            entry3Text = ""
            entry4Text = ""
            entry5Text = ""
            entry6Text = ""
            entry7Text = ""
            entry8Text = ""
            entry9Text = ""
            entry10Text = ""

        
        label1 = tk.Label(self, text="Numéro du projet:")
        label1.pack()
        entry1 = tk.Entry(self)
        entry1.insert(tk.END, entry1Text)
        entry1.pack()
        label2 = tk.Label(self, text="Intitulé:")
        label2.pack()
        entry2 = tk.Entry(self)
        entry2.insert(tk.END, entry2Text)
        entry2.pack()

        label3 = tk.Label(self, text="Proposé par :")
        label3.pack()
        entry3 = tk.Entry(self)
        entry3.insert(tk.END, entry3Text)
        entry3.pack()

        label4 = tk.Label(self, text="Equipe:")
        label4.pack()
        entry4 = tk.Entry(self)
        entry4.insert(tk.END, entry4Text)
        entry4.pack()

        label5 = tk.Label(self, text="Tél:")
        label5.pack()
        entry5 = tk.Entry(self)
        entry5.insert(tk.END, entry5Text)
        entry5.pack()

        label6 = tk.Label(self, text="Mail:")
        label6.pack()
        entry6 = tk.Entry(self)
        entry6.insert(tk.END, entry6Text)
        entry6.pack()

        label8 = tk.Label(self, text="Minimum:")
        label8.pack()
        entry8 = tk.Entry(self)
        entry8.insert(tk.END, entry8Text)

        entry8.pack()

        label9 = tk.Label(self, text="Maximum:")
        label9.pack()
        entry9 = tk.Entry(self)
        entry9.insert(tk.END, entry9Text)
        entry9.pack()


        label20 = tk.Label(self, text="Entreprise:")
        label20.pack()
        entry10 = tk.Entry(self)
        entry10.insert(tk.END, entry10Text)
        entry10.pack()

        label7 = tk.Label(self, text="Description:")
        label7.pack()
        entry7 = tk.Text(self, height=5)
        entry7.insert(tk.END, entry7Text)
        entry7.pack()
        
        generate_button = tk.Button(self,text="Add Project", command=lambda: generate_pdf(entry1, entry2, entry3, entry4, entry5, entry6, entry7,entry8,entry9,entry10))
        generate_button.pack()
        
        finish_button = tk.Button(self, text="Finish PDF", command=finish_pdf)
        finish_button.pack()