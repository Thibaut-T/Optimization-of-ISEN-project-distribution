import tkinter as tk
from fpdf import FPDF
import sys


input_values = []

def generate_pdf_with_values(input_values):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    middle_point = pdf.h / 2
    text_height = 3 * pdf.font_size 
    pdf.set_y(middle_point - text_height / 2)
    pdf.cell(200, 10, txt="Cover Page", ln=True, align="C")
    pdf.ln(pdf.font_size)
    pdf.cell(200, 10, txt="JUNIA PROJECTS", ln=True, align="C")
    pdf.ln(pdf.font_size)
    pdf.cell(200, 10, txt="2024/2025", ln=True, align="C")

    for input_set in input_values:
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for key, value in input_set.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.output("output.pdf")

def generate_pdf():
    global entry1, entry2, entry3, entry4, entry5, entry6, entry7

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

root = tk.Tk()
root.title("PDF Generator")

label1 = tk.Label(root, text="Numéro du projet:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Intitulé:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Proposé par :")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="Equipe:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

label5 = tk.Label(root, text="Tél:")
label5.pack()
entry5 = tk.Entry(root)
entry5.pack()

label6 = tk.Label(root, text="Mail:")
label6.pack()
entry6 = tk.Entry(root)
entry6.pack()

label7 = tk.Label(root, text="Description:")
label7.pack()
entry7 = tk.Text(root, height=5)
entry7.pack()

generate_button = tk.Button(root, text="Add Project", command=generate_pdf)
generate_button.pack()

finish_button = tk.Button(root, text="Finish PDF", command=finish_pdf)
finish_button.pack()

root.mainloop()
