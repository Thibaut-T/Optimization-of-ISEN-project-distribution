import pandas as pd
from tkinter import filedialog
import os
import subprocess

def help():
    pdf_file_path = "help.pdf"

    # Vérifie si le fichier PDF existe
    os.path.exists(pdf_file_path)
        # Ouvre le fichier PDF avec le programme associé
    os.startfile(pdf_file_path)
    