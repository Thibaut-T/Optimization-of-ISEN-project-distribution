from tkinter import END, filedialog
from fpdf import FPDF
import pandas as pd

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
        
        # Display Project number
        pdf.set_text_color(0, 100, 0)  # Dark green color for Project number
        pdf.set_font("Arial", "B", 18)  # Bigger font size for "Project number"
        pdf.cell(0, 10, txt=input_set["Project number"], ln=True, align="C")
        
        # Horizontal line after Project number
        pdf.set_fill_color(0, 100, 0)  # Dark green color for lines
        pdf.set_y(pdf.get_y() + 5)  # Adjust spacing
        pdf.cell(0, 2, ln=True, fill=True)
        
        # Display the remaining inputs in dark blue
        pdf.set_text_color(0, 0, 139)  # Dark blue color for remaining text
        for key, value in input_set.items():
            if key != "Project number" and key != "Description":
                pdf.ln(2)  # Reduce space between inputs
                if key == ["Minimum d'étudiants","Maximum d'étudiants","Company"]:
                    pdf.set_font("Arial", "B", 14)  
                else:
                    pdf.set_font("Arial", size=12)  # Reset font for other keys
                pdf.cell(50, 8, txt=f"{key}:".encode('latin-1', 'ignore').decode('latin-1'), ln=False)
                if pdf.get_string_width(value.encode('latin-1', 'ignore').decode('latin-1')) > (pdf.w - 2 * pdf.l_margin - 50):
                    pdf.multi_cell(0, 8, txt=value.encode('latin-1', 'ignore').decode('latin-1'), align="L")
                else:
                    pdf.cell(0, 5, txt=value.encode('latin-1', 'ignore').decode('latin-1'), ln=True)
        
        # Description Title
        if "Description" in input_set:
            pdf.set_text_color(0, 0, 139)  
            pdf.set_font("Arial", "BU", 12) 
            pdf.cell(0, 10, txt="Description:", ln=True)  
            pdf.ln(2)  
            pdf.set_font("Arial", size=10)  
            page_width = pdf.w - 2 * pdf.l_margin 
            description_text = input_set["Description"]
            pdf.multi_cell(page_width, 5, txt=description_text.encode('latin-1', 'ignore').decode('latin-1'))


    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if filename:
        pdf.output(filename, 'F')

def modify_line(id, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, controller):
    input1 = id
    input2 = entry2.get()
    input3 = entry3.get()
    input4 = entry4.get()
    input5 = entry5.get()
    input6 = entry6.get()
    input8 = entry8.get()
    input9 = entry9.get()
    input10 = entry10.get()
    input7 = entry7.get("1.0", END)
    if input10 == "":
        input10 = "N/A"

    input_dict = {
        "Project number": input1,
        "Project name": input2,
        "Person in charge": input3,
        "Team emails": input4,
        "Phone number": input5,
        "Mail": input6,
        "Description": input7,
        "Minimum students": input8,
        "Maximum students": input9,
        "Company": input10
    }

    try:
        df = pd.read_excel("common/dataProjects.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame()

    # Check if the project already exists in the DataFrame
    
    row = df[df["Project number"] == input1]

    index = row.index[0]  # Get the index of the project

    df.loc[index] = input_dict  # Update the row with new details

    df.to_excel("common/dataProjects.xlsx", index=False)

    # Clear the entry widgets
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    entry10.delete(0, END)
    entry7.delete("1.0", END)

    # Show the "projectManagement" frame
    controller.show_frame("projectManagement")



def add_line(id, entry2, entry3, entry4, entry5, entry6, entry7,entry8,entry9,entry10, controller):
    input1 = id
    input2 = entry2.get()
    input3 = entry3.get()
    input4 = entry4.get()
    input5 = entry5.get()
    input6 = entry6.get()
    input8 = entry8.get()
    input9 = entry9.get()
    input10 = entry10.get()
    input7 = entry7.get("1.0", END)
    if(input10==""):
        input10="N/A"
    
    input_dict = {
        "Project number": input1,
        "Project name": input2,
        "Person in charge": input3,
        "Team emails": input4,
        "Phone number": input5,
        "Mail": input6,
        "Description": input7,
        "Minimum d'étudiants": input8,
        "Maximum d'étudiants": input9,
        "Company": input10
    }
   
    input_values.append(input_dict)
    
  
    try:
        df = pd.read_excel("common/dataProjects.xlsx")
  
    except FileNotFoundError:
        df = pd.DataFrame()
        
    new_row = pd.DataFrame(input_dict, index=[0])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_excel("common/dataProjects.xlsx", index=False)

    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    entry10.delete(0, END)
    entry7.delete("1.0", END)

    controller.show_frame("projectManagement")
