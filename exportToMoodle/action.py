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
        <text>$course$/top/MoodleOfficiel</text>
        </category>
        </question>

        <question type="multichoice">
        <name format="html">
        <text><![CDATA[Présence]]></text>
        </name>
        <questiontext format="html">
        <text><![CDATA[<p>Êtes-vous présent.e.s au semestre 2 ? <BR/>Are you present in semester 2 ? </p>]]></text>
        </questiontext>
        <defaultgrade>1.0</defaultgrade>
        <generalfeedback format="html"><text/></generalfeedback>
        <penalty>0.10</penalty>
        <hidden>0</hidden>
        <single>true</single>
        <shuffleanswers>1</shuffleanswers>
        <answernumbering>abc</answernumbering>
        <answer fraction="0" format="html">
        <text><![CDATA[<p>Oui <BR/>Yes</p>]]></text>
        </answer>
        <answer fraction="0" format="html">
        <text><![CDATA[<p>Non <BR/>No</p>]]></text>
        </answer>
        </question>
        <question type="multichoice">
        <name format="html">
        <text><![CDATA[Informatique et finance]]></text>
        </name>
        <questiontext format="html">
        <text><![CDATA[<p>Êtes-vous en spécialité informatique et finance ? <BR/>Are you specializing in informatics and finance ? </p>]]></text>
        </questiontext>
        <defaultgrade>1.0</defaultgrade>
        <generalfeedback format="html"><text/></generalfeedback>
        <penalty>0.10</penalty>
        <hidden>0</hidden>
        <single>true</single>
        <shuffleanswers>1</shuffleanswers>
        <answernumbering>abc</answernumbering>
        <answer fraction="0" format="html">
        <text><![CDATA[<p>Oui <BR/>Yes</p>]]></text>
        </answer>
        <answer fraction="0" format="html">
        <text><![CDATA[<p>Non <BR/>No</p>]]></text>
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
            <text><![CDATA[Projet """ + str(project_number) + """ ]]></text>
            </name>
            <questiontext format="html">
            <text><![CDATA[<p>Évaluez le projet """ + str(project_number) + """ : temp de 1 à 10 (10 = votre projet préféré) <BR/>Rate the project """ + str(i) + """ : temp from 1 to 10 (10 = your favorite project) </p>]]></text>
            </questiontext>
            <defaultgrade>1.0</defaultgrade>
            <generalfeedback format="html"><text/></generalfeedback>
            <penalty>0.10</penalty>
            <hidden>0</hidden>
            <single>true</single>
            <shuffleanswers>1</shuffleanswers>
            <answernumbering>abc</answernumbering>
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
            """)

def save():
    filename = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
    create_xml_file(filename)