import shutil
import os
import tkinter.messagebox as messagebox

def reset(controller):
    confirmation = messagebox.askyesno("Confirmation", "Warning: This action is irreversible. Are you sure you want to proceed?")
    if confirmation:
        shutil.rmtree('./common')
        os.mkdir('./common')
        messagebox.showinfo("Information", "Reset successful")
        controller.show_frame("projectManagement")