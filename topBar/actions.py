import os
import subprocess
import platform

def help():
    pdf_file_path = "Help.pdf"

    if not os.path.exists(pdf_file_path):
        return
    
    if platform.system() == 'Windows':
        os.startfile(pdf_file_path)
    elif platform.system() == 'Darwin':  # MacOS vraiment pas sûr
        subprocess.call(('open', pdf_file_path))
    elif platform.system() == 'Linux':
        subprocess.call(('xdg-open', pdf_file_path))