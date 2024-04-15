import pandas as pd
from tkinter import filedialog
import os

def helptest():
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
  

def help():
    # Spécifiez le chemin du fichier PDF
    pdf_file_path = "Tuto_quiz_moodle_v1.pdf"

    # Demandez à l'utilisateur où enregistrer le fichier
    destination_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    # Copier le fichier PDF dans le répertoire de destination
    if destination_file:
        # Vérifiez si le fichier PDF existe
        if os.path.exists(pdf_file_path):
            # Copiez le fichier PDF dans le répertoire de destination
            with open(pdf_file_path, "rb") as f_read:
                with open(destination_file, "wb") as f_write:
                    f_write.write(f_read.read())