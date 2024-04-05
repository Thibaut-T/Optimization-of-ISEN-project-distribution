import os
from tkinter import filedialog
import pandas as pd

def create_xml_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    with open(filename, 'x', encoding='utf-8') as file:
        file.write(r"""<?xml version="1.0" encoding="utf-8"?>
        <quiz>

        <question type="category">
        <category>
        <text>$course$/top/MoodleOfficieltest</text>
        </category>
        </question>

        <question type="multichoice">
        <name format="html">
        <text><![CDATA[Présence]]></text>
        </name>
        <questiontext format="html">
        <text><![CDATA[<p>Êtes-vous présent.e.s au semestre 2 ?<BR/>Are you present in semester 2 ?</p>]]></text>
        </questiontext>
        <defaultgrade>0</defaultgrade>
        <generalfeedback format="html"><text/></generalfeedback>
        <hidden>0</hidden>
        <single>true</single>
        <shuffleanswers>1</shuffleanswers>
        <answernumbering>abc</answernumbering>
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
        <text><![CDATA[<p>Êtes-vous en spécialité Informatique et Finance ?<BR/>Are you specialized in Information Technology and Finance ?</p>]]></text>
        </questiontext>
        <defaultgrade>0</defaultgrade>
        <generalfeedback format="html"><text/></generalfeedback>
        <hidden>0</hidden>
        <single>true</single>
        <shuffleanswers>1</shuffleanswers>
        <answernumbering>abc</answernumbering>
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
            project_number = df.loc[i, 'Numéro du projet']
            file.write(r"""<question type="multichoice">
            <name format="html">
            <text><![CDATA[Projet {:02d}]]></text>
            </name>
            <questiontext format="html">
            <text><![CDATA[<p>Évaluez le projet {:02d} : temp de 1 à 10 (10 = votre projet préféré)<BR/><em>Rate the project {:02d} : temp from 1 to 10 (10 = your favorite project)</em></p>]]></text>
            </questiontext>
            <defaultgrade>0</defaultgrade>
            <generalfeedback format="html"><text/></generalfeedback>
            <hidden>0</hidden>
            <single>true</single>
            <shuffleanswers>1</shuffleanswers>
            <answernumbering>123</answernumbering>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>1</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>2</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>3</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>4</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>5</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>6</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>7</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>8</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>9</p>]]></text>
            </answer>
            <answer fraction="0" format="html">
            <text><![CDATA[<p>10</p>]]></text>
            </answer>
            </question>
            """.format(project_number, project_number, project_number))

def save():
    filename = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
    create_xml_file(filename)