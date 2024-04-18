import tkinter as tk
from customtkinter import CTkButton, CTkLabel, CTkFrame
from tkinter import filedialog
from fpdf import FPDF
import pandas as pd
import re
import shutil


def generate_pdf2(dataframe, filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(195, 10, txt="Liste d'attribution", ln=True, align="C")
    pdf.ln(10)

    for index, row in dataframe.iterrows():
        number = row['number']
        name = row['name']
        person_in_charge = row['person_in_charge']
        min_student = row['min_student']
        max_student = row['max_student']
        eleves = row['students']
        emails = re.findall(r'<Student>\s*([\w.-]+@[a-zA-Z.-]+\.[a-zA-Z]+)', eleves)
        eleves_cleaned = '\n'.join(emails)
        
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f'Number: {number} - Name: {name}', ln=True)
        pdf.cell(0, 10, f'Person in charge: {person_in_charge} (Min Students: {min_student}, Max Students: {max_student})', ln=True)
        pdf.cell(0, 10, 'Students', ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, eleves_cleaned)  
        pdf.ln(10) 

    pdf.output(filename)


def read_excel_file():
    df = pd.read_excel('common/recap.xlsx')
    return df   


def extract_name(email):
    match = re.search(r'([^@]+)@', email) 
    if match:
        name = match.group(1)
        name_parts = re.findall(r'\b\w+\b', name)
        name = ' '.join(name_parts)
        return name
    else:
        return email 



class ExportStudentDistribution(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent)        
        self.previous_frame = "solverOutputManagement"
        self.next_frame = ""
        self.objective_fulfilled = True

        self.controller = controller
        self.reload()
    
    def reload(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.show()
    
    def show(self):
        
        label = CTkLabel(self, text="ExportStudentDistribution")
        label.pack()
    
        download_pdf_button = CTkButton(self, text="Download PDF file", command=self.download_pdf)
        download_pdf_button.pack(pady=20)
        
        download_excel_button = CTkButton(self, text="Download Excel file", command=self.download_excel)
        download_excel_button.pack()

    def download_pdf(self):
        df = read_excel_file()
        if df is not None:
            filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if filename:
                generate_pdf2(df, filename)
    
    def download_excel(self):
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], initialfile="recap.xlsx")
        if filename:
            shutil.copy('common/recap.xlsx', filename)
