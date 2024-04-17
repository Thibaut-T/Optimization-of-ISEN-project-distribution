import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkScrollableFrame, CTkButton
import math
import pandas as pd
import os


#####################################################################################
# Définition des classes existantes

class Project:
    def __init__(self):
        self.max_student = ""
        self.min_student = ""
        self.students = []
        self.number = ""
        self.name = ""
        self.person_in_charge = ""
        self.equipe = ""
        self.phone_number = ""
        self.mail = ""
        self.description = ""
        self.company = ""

    def representation(self):
        return f"Project {self.name} :\n - Min : {int(self.min_student) if not math.isnan(self.min_student) else 3}\n - Max : {int(self.max_student) if not math.isnan(self.max_student) else 7}\n - Team emails of the {len(self.students)} students :\n" + "\n".join([f"\t- {eleve.last_name} {eleve.first_name}" for eleve in self.students]) + "\n"
    
    def __str__(self):
        return f"Project {self.name}"
    
    
    def delete(self, reload):
        print(f"Deleting project {self.name}")

        dataFrameProjets = pd.read_excel("./common/recap.xlsx", sheet_name="Project")
        dataFrameEleves = pd.read_excel("./common/recap.xlsx", sheet_name="Students")
        dataFrameAnomalies = pd.read_excel("./common/recap.xlsx", sheet_name="Anomalies")

        dataFrameProjets = dataFrameProjets[dataFrameProjets["name"] != self.name]
        dataFrameAnomalies = dataFrameAnomalies[dataFrameAnomalies["project"] != self.__str__()]

        with pd.ExcelWriter("./common/recap.xlsx") as writer:
            dataFrameProjets.to_excel(writer, sheet_name="Project", index=False)
            dataFrameEleves.to_excel(writer, sheet_name="Students", index=False)
            dataFrameAnomalies.to_excel(writer, sheet_name="Anomalies", index=False)
            
        reload()

    
    def __repr__(self):
        return f"<Project> {self.name}"

class Student:
    def __init__(self):
        self.last_name = ""
        self.first_name = ""
        self.mail = ""

    def __str__(self):
        return f"Student {self.mail}"
    
    def __repr__(self):
        return f"<Student> {self.mail}"

class Anomalies:
    def __init__(self):
        self.error = ""
    def __str__(self):
        return f"Warning : {self.error}"
    def show_label(self, frame):
        error_label = CTkLabel(frame, text=self.error, anchor="w", justify="left", fg_color="red")
        error_label.grid(row=0, column=0, padx=5, pady=(10, 2), sticky="w")

    def show_button(self, frame):
        pass

    def button_action(self):
        pass

class AnomaliesEleve(Anomalies):
    def __init__(self):
        super().__init__()
        self.student = None

    def show_button(self, frame):
        pass

    def button_action(self):
        print(f"Action pour l'élève {self.student.last_name} {self.student.first_name}")

class AnomaliesProjet(Anomalies):
    def __init__(self):
        super().__init__()
        self.project = None

    def show_button(self, frame, reload):
        print(self.error)
        if "enough" in self.error:
            solve_button = CTkButton(frame, text="Delete project", command=lambda: self.project.delete(reload))
            solve_button.grid(row=1, column=0, padx=5, pady=(2, 10), sticky="w")

            solve_button.update_idletasks()
            button_width = solve_button.winfo_reqwidth()
            button_height = solve_button.winfo_reqheight()
            solve_button.configure(width=button_width, height=button_height)    

    def button_action(self):
        print(f"Action pour le projet {self.project.name}")

def verifier_anomalies(resultSolver, projets, eleves):
        all_errors = []
        for index, row in resultSolver.iterrows():
            #skip the first column
            if sum(row.iloc[1:]) < 1:
                tmp = AnomaliesEleve()
                tmp.student = eleves[index]
                tmp.error = f"{tmp.student.last_name} {tmp.student.first_name} is not affected to any project"
                all_errors.append(tmp)

            if sum(row.iloc[1:]) > 1:
                tmp = AnomaliesEleve()
                tmp.student = eleves[index]
                tmp.error = f"{tmp.student.last_name} {tmp.student.first_name} is affected to multiple projects"
                all_errors.append(tmp)

        df_projet = pd.read_excel("./common/dataProjects.xlsx")

        for projet in projets:
            corresponding_row = df_projet[df_projet["Project number"] == projet.number]
            somme_etudiants = len(projet.students)

            if somme_etudiants < corresponding_row["Minimum students"].values[0]:
                tmp = AnomaliesProjet()
                tmp.project = projet
                tmp.error = f"{tmp.project.name} doesn't contain enough students"
                all_errors.append(tmp)

            if somme_etudiants > corresponding_row["Maximum students"].values[0]:
                tmp = AnomaliesProjet()
                tmp.project = projet
                tmp.error = f"{tmp.project.name} contains too many students"
                all_errors.append(tmp)

        return all_errors

# Création de l'interface utilisateur avec tkinter
class SolverOutputManagement(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent)

        self.previous_frame = "solverProcess"
        self.next_frame = "exportStudentDistribution"
        self.objective_fulfilled = True
        self.parent = parent
        self.controller = controller

        self.projets = []
        self.eleves = []
        self.all_errors = []

        self.reload()

    def reset_all(self):
        if os.path.exists("./common/recap.xlsx"):
                os.remove("./common/recap.xlsx")
                print("Fichier recap.xlsx supprimé avec succès.")
        else:
            print("Le fichier recap.xlsx n'existe pas.")
            # Bouton Reset All

        self.reload()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()

        self.projets = []
        self.eleves = []
        self.all_errors = []

        if not os.path.exists("./common/recap.xlsx"):
            print("Fichier de récapitulatif non trouvé, chargement des données...")

            if not os.path.exists("./common/dataProjects.xlsx") or not os.path.exists("./common/answerProjects.xlsx") or not os.path.exists("./common/resultSolver.csv"):
                print("Fichiers de données non trouvés")
                return
            else:
                # Chargement des fichiers Excel
                dataProjects = pd.read_excel('./common/dataProjects.xlsx')
                answerProjects = pd.read_excel('./common/answerProjects.xlsx')
                result_solver = pd.read_csv('./common/resultSolver.csv')
                
                self.projets = [] # Liste pour stocker les objets de la classe Project
                self.eleves = [] # Liste pour stocker les objets de la classe Student
                self.all_errors = [] # Liste pour stocker les objets de la classe Anomalies

                traduction_ = {
                    'response' : {
                        'fr' : 'Réponse',
                        'en' : 'Response',
                    },
                    'email' : {
                        'fr' : 'Adresse de courriel',
                        'en' : 'Email address',
                    },
                    'first_name' : {
                        'fr' : 'Prénom',
                        'en' : 'First name',
                    },
                    'last_name' : {
                        'fr' : 'Nom de famille',
                        'en' : 'Last name',
                    },
                }
                language = "fr" if "Nom de famille" in answerProjects.columns else "en"

                for student in answerProjects.iterrows():
                    eleve = Student()
                    eleve.last_name = student[1][traduction_['last_name'][language]]
                    eleve.first_name = student[1][traduction_['first_name'][language]]
                    eleve.mail = student[1][traduction_['email'][language]]
                    self.eleves.append(eleve)

                # Parcourir toutes les colonnes
                for colonne in result_solver.columns:
                    # skip the first column
                    if colonne == "0":
                        print("Skipping first column")
                        continue
                    

    
                    # Créer une instance de la classe Project
                    projet = Project()
            
                    tmp_projet = dataProjects[dataProjects['Project number'] == int(colonne)]

                    # Affecter le last_name de la colonne au champ last_name de l'objet Project
                    projet.number = tmp_projet["Project number"].values[0]

                    if (result_solver[colonne] == 1).any():
                        # Afficher les titres de ligne avec la valeur 1 dans cette colonne
                        lignes = result_solver[result_solver[colonne] == 1].index

                        for ligne in lignes:
                            # Ajouter l'objet Student à la liste eleves de l'objet Project
                            for eleve in self.eleves:
                                if eleve.mail == result_solver.iloc[ligne, 0].split("?")[1]:
                                    projet.students.append(eleve)
                                    break
                            
                        # Ajouter l'objet Project à la liste projets

                    else:
                        print(f"Le projet {colonne} n'a pas été sélectionné")

                    self.projets.append(projet)

                # Ajouter les informations des projets dans le conteneur scrollable_frame
                # Parcourir les self.projets et compléter les informations
                for projet in self.projets:
                    # Récupérer les informations du projet correspondant à son last_name dans common/dataProjects.xlsx
                    infos_projet = dataProjects[dataProjects['Project number'] == projet.number]
                    if not infos_projet.empty:
                        infos_projet = infos_projet.iloc[0]
                        # Remplir les attributs de l'objet Project
                        projet.name = infos_projet['Project name']
                        projet.person_in_charge = infos_projet['Person in charge']
                        projet.equipe = infos_projet['Team emails']
                        projet.phone_number = infos_projet['Phone number']
                        projet.mail = infos_projet['Mail']
                        projet.description = infos_projet['Description']
                        projet.min_student = infos_projet['Minimum students']
                        projet.max_student = infos_projet['Maximum students']
                        projet.company = infos_projet['Company']
                    else:
                        print(f"Aucune information trouvée pour le projet {projet.name} dans le fichier common/dataProjects.xlsx")

                # Vérifier les anomalies
                self.all_errors = verifier_anomalies(result_solver, self.projets, self.eleves)

                

            # sauvegarde des résultats dans un fichier Excel
            # # Créer un dictionnaire pour stocker les données des projets et des élèves

            dataFrameProjets = pd.DataFrame([vars(s) for s in self.projets])
            cols = ['number', 'name', 'person_in_charge', 'students', 'phone_number', 'mail', 'description', 'min_student', 'max_student', 'company']
            dataFrameProjets = dataFrameProjets[cols]

            dataFrameEleves = pd.DataFrame([vars(s) for s in self.eleves])
            cols = ['last_name', 'first_name', 'mail']
            dataFrameEleves = dataFrameEleves[cols]
            
            dataFrameAnomalies = pd.DataFrame([vars(s) for s in self.all_errors])

            # create a excel writer object
            with pd.ExcelWriter("./common/recap.xlsx") as writer:
                # use to_excel function and specify the sheet_name and index 
                # to store the dataframe in specified sheet
                dataFrameProjets.to_excel(writer, sheet_name="Project", index=False)
                dataFrameEleves.to_excel(writer, sheet_name="Students", index=False)
                dataFrameAnomalies.to_excel(writer, sheet_name="Anomalies", index=False)

        else:
            print("Fichier de récapitulatif trouvé, chargement des données...")

            dataFrameProjets = pd.read_excel("./common/recap.xlsx", sheet_name="Project")
            dataFrameEleves = pd.read_excel("./common/recap.xlsx", sheet_name="Students")
            dataFrameAnomalies = pd.read_excel("./common/recap.xlsx", sheet_name="Anomalies")

            self.projets = [Project() for i in range(len(dataFrameProjets))]
            self.eleves = [Student() for i in range(len(dataFrameEleves))]
            self.all_errors = []

            for i, row in dataFrameEleves.iterrows():
                self.eleves[i].last_name = row["last_name"]
                self.eleves[i].first_name = row["first_name"]
                self.eleves[i].mail = row["mail"]

            for i, row in dataFrameProjets.iterrows():
                self.projets[i].number = row["number"]
                self.projets[i].name = row["name"]
                self.projets[i].person_in_charge = row["person_in_charge"]
                self.projets[i].students = [eleve for eleve in self.eleves if eleve.mail in row["students"].replace("[", "").replace("]", "").replace("<Student>","").replace(" ","").split(",")]
                self.projets[i].phone_number = row["phone_number"]
                self.projets[i].mail = row["mail"]
                self.projets[i].description = row["description"]
                self.projets[i].min_student = row["min_student"]
                self.projets[i].max_student = row["max_student"]
                self.projets[i].company = row["company"]



            for i, row in dataFrameAnomalies.iterrows():
                print(i)
                print(row)
                print(self.all_errors)
                if "student" in row:
                    print("student")
                    self.all_errors.append(AnomaliesEleve())
                    for student in self.eleves:
                        if student.mail in str(row["student"]):
                            self.all_errors[i].student = student
                            self.all_errors[i].error = row["error"]
                if "project" in row:
                    print("project")
                    self.all_errors.append(AnomaliesProjet())
                    for project in self.projets:
                        if project.name in str(row["project"]):
                            self.all_errors[i].project = project
                            self.all_errors[i].error = row["error"]

    
        self.show()

    def show(self):
        label = CTkLabel(self, text = "Solver Output Management")
        label.pack()

        centered_frame = CTkFrame(self)
        centered_frame.pack(fill="both", expand=True)

        # Cadre principal pour contenir les cadres gauche et droit
        centered_frame.grid_columnconfigure(0, weight=1)  # Colonne 0
        centered_frame.grid_columnconfigure(1, weight=1)  # Colonne 1
        centered_frame.grid_rowconfigure(0, weight=1)     # Ligne 0
        
        # Cadre gauche avec un poids de 1
        left_frame = CTkScrollableFrame(centered_frame)
        left_frame.grid(row=0, column=0, padx=5, sticky="nsew")
        
        # Cadre droit avec un poids de 1
        right_frame = CTkScrollableFrame(centered_frame)
        right_frame.grid(row=0, column=1, padx=5, sticky="nsew")

        reset_button = CTkButton(left_frame, text="Reset All", command = lambda: self.reset_all())
        reset_button.pack(padx=10, pady=10, side="top")
        
        # Ajouter les informations des self.projets dans le conteneur scrollable_frame
        for projet in self.projets:
            card = CTkFrame(right_frame)
            card.pack(padx=5, pady=5, fill="x")

            projet_label = CTkLabel(card, text=projet.representation() ,justify="left")
            projet_label.pack(padx=10, pady=10, anchor="w")

        for error in self.all_errors:
            card = CTkFrame(left_frame, fg_color="red")
            card.pack(padx=5, pady=5, fill="x")

            error.show_label(card)
            error.show_button(card, self.reload)