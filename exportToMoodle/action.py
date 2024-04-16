import os
from tkinter import filedialog
import pandas as pd
from projectCreation.action import generate_pdf_with_values

# Create the XML file
def create_xml_file(filename, moodle_folder):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    with open(filename, 'x', encoding='utf-8') as file:
        file.write(r"""<?xml version="1.0" encoding="utf-8"?>
        <quiz>

        <question type="category">
        <category>
        <text>$course$/top/""" + moodle_folder + r"""</text>
        </category>
        </question>

        <question type="multichoice">
        <name format="html">
        <text><![CDATA[Présence]]></text>
        </name>
        <questiontext format="html">
        <text><![CDATA[<p>Êtes-vous présent.e.s au semestre 2 ?<BR/><em>Are you present in semester 2 ?</em></p>]]></text>
        </questiontext>
        <defaultgrade>0</defaultgrade>
        <generalfeedback format="html"><text/></generalfeedback>
        <single>true</single>
        <shuffleanswers>1</shuffleanswers>
        <answernumbering>none</answernumbering>
        <answer fraction="0" format="html">
        <text><![CDATA[<p>Oui<BR/>Yes</p>]]></text>
        </answer>
        <answer fraction="0" format="html">
        <text><![CDATA[<p>Non<BR/>No</p>]]></text>
        </answer>
        </question>
        <question type="multichoice">
        <name format="html">
        <text><![CDATA[Informatique et Finance]]></text>
        </name>
        <questiontext format="html">
        <text><![CDATA[<p>Êtes-vous en spécialité Informatique et Finance ?<BR/><em>Are you specialized in Information Technology and Finance ?</em></p>]]></text>
        </questiontext>
        <defaultgrade>0</defaultgrade>
        <generalfeedback format="html"><text/></generalfeedback>
        <single>true</single>
        <shuffleanswers>1</shuffleanswers>
        <answernumbering>none</answernumbering>
        <answer fraction="0" format="html">
        <text><![CDATA[<p>Oui<BR/>Yes</p>]]></text>
        </answer>
        <answer fraction="0" format="html">
        <text><![CDATA[<p>Non<BR/>No</p>]]></text>
        </answer>
        </question>
        """)
        
        # Open the Excel file with pandas
        df = pd.read_excel('common/dataProjects.xlsx')

        # Loop over df to create a question for each project
        for i in range(len(df)):
            project_number = df.loc[i, 'Project number']
            file.write(r"""<question type="multichoice">
            <name format="html">
            <text><![CDATA[Projet {:02d}]]></text>
            </name>
            <questiontext format="html">
            <text><![CDATA[<p>Évaluez le projet """ + str(project_number) + """ : """ + str(df.loc[i, "Project name"]) + """ de 1 à 10 (10 = votre projet préféré)<BR/><em>Rate the project """ + str(project_number) + """ : """ + str(df.loc[i, "Project name"]) + """ from 1 to 10 (10 = your favorite project)</em></p>]]></text>
            </questiontext>
            <defaultgrade>0</defaultgrade>
            <generalfeedback format="html"><text/></generalfeedback>
            <single>true</single>
            <shuffleanswers>1</shuffleanswers>
            <answernumbering>none</answernumbering>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>10</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>9</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>8</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>7</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>6</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>5</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>4</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>3</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>2</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>1</p>]]></text>
            </answer>
            </question>
            """.format(project_number, project_number, project_number))

def save(entry):
    # save xml
    filename = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
    create_xml_file(filename, entry.get())

def getAllProjects():
    # try to get all projects 
    directory = 'common'
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        df = pd.read_excel('common/dataProjects.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Project number', 'Project name', 'Person in charge', 'Team emails', 'Phone number', 'Mail', 'Description', 'Minimum students', 'Maximum students', 'Company'])
        df.to_excel('common/dataProjects.xlsx', index=False)
    return df
    
def savePdf():
    # save the pdf
    projects = getAllProjects()
    projects = projects.astype(str)  
    projects_dict = projects.to_dict('records') 
    generate_pdf_with_values(projects_dict)