import tkinter.ttk as ttk
from customtkinter import CTkButton, CTkLabel, CTkFrame, CTkEntry,VERTICAL
from exportToMoodle.action import save, savePdf

class exportToMoodle(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent)
                
        self.previous_frame = "projectManagement"
        self.next_frame = "solverInputFile"
        self.objective_fulfilled = True

        self.controller = controller
        self.reload()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        self.show()
    
    def show(self):
        # label of frame exportToMoodle
        label = CTkLabel(self, text ="exportToMoodle")
        label.pack()
        
        centered_frame = CTkFrame(self)
        centered_frame.pack()

        # save button
        folder_name = CTkLabel(centered_frame, text="Nom de la banque de questions:")
        folder_name.grid(row = 2, column = 0,pady = 10)
        entry = CTkEntry(centered_frame)
        entry.grid(row = 3, column = 0, padx = 10, pady = 10)
        save_button = CTkButton(centered_frame, text="Download Moodle initialisation file", command=lambda moodle_folder=entry: save(moodle_folder))
        save_button.grid(row = 1, column = 0, padx = 10, pady = 10)

        separator = ttk.Separator(centered_frame, orient=VERTICAL)
        separator.grid(column=1, row=0, rowspan=4, sticky='ns')

        button2 = CTkButton(centered_frame, text="save pdf of all projects", command=lambda: savePdf())
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)