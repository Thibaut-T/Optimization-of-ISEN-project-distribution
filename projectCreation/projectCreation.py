import tkinter as tk
from tkinter import ttk
import pandas as pd
from projectCreation.action import add_line, modify_line
import re 
class ProjectCreation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="purple")

        self.previous_frame = ""
        self.next_frame = ""
        self.objective_fulfilled = True

        self.controller = controller
        self.reload()
    
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        
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

        def is_number(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        def validate_email(value):
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = value.split(";")
            valid = all(re.match(email_regex, email) is not None for email in emails)
            label6.config({"foreground": "red" if not valid else "black"})
            return True
        
        def validate_emails(value):     # For the equipe field
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = value.split(";")
            valid = all(re.match(email_regex, email.strip()) is not None for email in emails)
            label4.config({"foreground": "red" if not valid else "black"})
            return True

        def is_phone_number(value):
            return all(char.isdigit() or char == "+" for char in value)
        
        idCurrent = -1
        try:
            with open('./common/currentCreation.txt', 'r') as file:
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
                df = pd.read_excel('common/dataProjects.xlsx')
                filtered_df = df[df['Numéro du projet'] == idCurrent]

                id = filtered_df['Numéro du projet'].values[0] if not filtered_df.empty else ""
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
            try:
                id = len(pd.read_excel('common/dataProjects.xlsx'))+1
            except FileNotFoundError:
                id = 1
            entry2Text = ""
            entry3Text = ""
            entry4Text = ""
            entry5Text = ""
            entry6Text = ""
            entry7Text = ""
            entry8Text = ""
            entry9Text = ""
            entry10Text = ""

        entry1Text = id
        
        label1 = tk.Label(self, text="Numéro du projet:")
        label1.pack()
        entry1 = tk.Label(self, text=entry1Text)
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

        vcmd_mail2 = (self.register(validate_emails), '%P')
        label4 = tk.Label(self, text="Equipe:")
        label4.pack()
        entry4 = tk.Entry(self,validate='key', validatecommand=vcmd_mail2)
        entry4.insert(tk.END, entry4Text)
        entry4.pack()



        vcmd_phone = (self.register(is_phone_number), '%P')

        label5 = tk.Label(self, text="Tél:")
        label5.pack()
        entry5 = tk.Entry(self, validate='key', validatecommand=vcmd_phone)
        entry5.insert(tk.END, entry5Text)
        entry5.pack()

        vcmd_mail = (self.register(validate_email), '%P')

        label6 = tk.Label(self, text="Mail:")
        label6.pack()
        entry6 = tk.Entry(self, validate='key', validatecommand=vcmd_mail)
        entry6.insert(tk.END, entry6Text)
        entry6.pack()

        vcmd = (self.register(is_number), '%P')
        label8 = tk.Label(self, text="Minimum:")
        label8.pack()
        entry8 = tk.Entry(self, validate='key', validatecommand=vcmd)
        entry8.insert(tk.END, entry8Text)
        entry8.pack()

        label9 = tk.Label(self, text="Maximum:")
        label9.pack()
        entry9 = tk.Entry(self, validate='key', validatecommand=vcmd)
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
        
        if idCurrent == -1:
            generate_button = tk.Button(self,text="Add Project", command=lambda id = id: add_line(id, entry2, entry3, entry4, entry5, entry6, entry7,entry8,entry9,entry10, self.controller))
            generate_button.pack()
        else:
            modify_button = tk.Button(self, text="Modify Project", command=lambda id = id: modify_line(id, entry2, entry3, entry4, entry5, entry6, entry7,entry8,entry9,entry10, self.controller))
            modify_button.pack()