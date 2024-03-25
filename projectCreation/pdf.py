import tkinter as tk
from fpdf import FPDF
import sys


input_values = []

def generate_pdf_with_values(input_values):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    
    # Title
    pdf.set_y(10)
    pdf.cell(0, 10, txt="Cover Page", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(0, 10, txt="JUNIA PROJECTS", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(0, 10, txt="2024/2025", ln=True, align="C")
    
    # Iterate through input values
    for input_set in input_values:
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Display Numéro du projet
        pdf.set_text_color(0, 100, 0)  # Dark green color for Numéro du projet
        pdf.set_font("Arial", "B", 18)  # Bigger font size for "Numéro du projet"
        pdf.cell(0, 10, txt=input_set["Numéro du projet"], ln=True, align="C")
        
        # Horizontal line after Numéro du projet
        pdf.set_fill_color(0, 100, 0)  # Dark green color for lines
        pdf.set_y(pdf.get_y() + 5)  # Adjust spacing
        pdf.cell(0, 2, ln=True, fill=True)
        
        # Display the remaining inputs in dark blue
        pdf.set_text_color(0, 0, 139)  # Dark blue color for remaining text
        for key, value in input_set.items():
            if key != "Numéro du projet" and key != "Description":
                pdf.ln(2)  # Reduce space between inputs
                if key == "Intitulé":
                    pdf.set_font("Arial", "B", 14)  # Change font size and style for "Intitulé"
                else:
                    pdf.set_font("Arial", size=12)  # Reset font for other keys
                pdf.cell(50, 8, txt=f"{key}:", ln=False)
                pdf.cell(0, 8, txt=value, ln=True)
        
        # Description Title
        if "Description" in input_set:
            pdf.set_text_color(0, 0, 139)  # Dark blue color for Description title
            pdf.set_font("Arial", "BU", 12)  # Underlined and regular font size for Description title
            pdf.cell(50, 10, txt="Description:", ln=False)
            pdf.ln(8)  # Space between Description title and value
            pdf.set_draw_color(0, 100, 0)  # Dark green color for outline of rectangle
            pdf.rect(10, pdf.get_y() - 5, 190, 40)  # Rectangle around the Description
            pdf.set_font("Arial", size=12)  # Reset font size for Description value
            pdf.multi_cell(0, 8, txt=input_set["Description"])

    pdf.output("output.pdf")

def generate_pdf(entry1, entry2, entry3, entry4, entry5, entry6, entry7):
     
    input1 = entry1.get()
    input2 = entry2.get()
    input3 = entry3.get()
    input4 = entry4.get()
    input5 = entry5.get()
    input6 = entry6.get()
    input7 = entry7.get("1.0", tk.END)

    input_dict = {
        "Numéro du projet": input1,
        "Intitulé": input2,
        "Proposé par": input3,
        "Equipe": input4,
        "Tél": input5,
        "Mail": input6,
        "Description": input7
    }
    
   
    input_values.append(input_dict)
    generate_pdf_with_values(input_values)

    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)
    entry7.delete("1.0", tk.END)

def finish_pdf():
    sys.exit()  

