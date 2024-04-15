import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkScrollableFrame, CTkButton
import math
import pandas as pd
import os


#####################################################################################
# Définition des classes existantes

class Projet:
    def __init__(self):
        self.nbmax = ""
        self.nbmin = ""
        self.eleves = []
        self.numero_proj = ""
        self.intitule = ""
        self.par = ""
        self.equipe = ""
        self.tel = ""
        self.mail = ""
        self.description = ""
        self.entreprise = ""

    def representation(self):
        return f"Projet {self.intitule} :\n - Min : {int(self.nbmin) if not math.isnan(self.nbmin) else 3}\n - Max : {int(self.nbmax) if not math.isnan(self.nbmax) else 7}\n - Equipe de {len(self.eleves)} étudiants :\n" + "\n".join([f"\t- {eleve.nom} {eleve.prenom}" for eleve in self.eleves]) + "\n"
    
    def __str__(self):
        return f"Projet {self.intitule}"
    
    def __repr__(self):
        return f"<Projet> {self.intitule}"

class Eleve:
    def __init__(self):
        self.nom = ""
        self.prenom = ""
        self.mail = ""

    def __str__(self):
        return f"Eleve {self.mail}"
    
    def __repr__(self):
        return f"<Eleve> {self.mail}"

class Anomalies:
    def __init__(self):
        self.error = ""
    def __str__(self):
        return f"Warning : {self.error}"

class AnomaliesEleve(Anomalies):
    def __init__(self):
        super().__init__()
        self.student = None

class AnomaliesProjet(Anomalies):
    def __init__(self):
        super().__init__()
        self.projet = None    

def verifier_anomalies(resultSolver, projets, eleves):
        all_errors = []
        for index, row in resultSolver.iterrows():
            if sum(row.iloc[1:]) < 1:
                tmp = AnomaliesEleve()
                tmp.student = eleves[index]
                tmp.error = f"{tmp.student.nom} {tmp.student.prenom} n'est pas affecté à un projet"
                all_errors.append(tmp)

            if sum(row.iloc[1:]) > 1:
                tmp = AnomaliesEleve()
                tmp.student = eleves[index]
                tmp.error = f"{tmp.student.nom} {tmp.student.prenom} est affecté à plusieurs projets"
                all_errors.append(tmp)

        df_projet = pd.read_excel("./common/dataProjects.xlsx")

        for projet in projets:
            corresponding_row = df_projet[df_projet["Numéro du projet"] == projet.numero_proj]
            somme_etudiants = len(projet.eleves)

            if somme_etudiants < corresponding_row["Minimum d'étudiants"].values[0]:
                tmp = AnomaliesProjet()
                tmp.projet = projet
                tmp.error = f"{tmp.projet.intitule} n'a pas le minimum requis d'étudiants"
                all_errors.append(tmp)

            if somme_etudiants > corresponding_row["Maximum d'étudiants"].values[0]:
                tmp = AnomaliesProjet()
                tmp.projet = projet
                tmp.error = f"{tmp.projet.intitule} contient trop d'étudiants"
                all_errors.append(tmp)

        return all_errors


def solve_function():
    pass

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
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()

        if not os.path.exists("./common/recap.xlsx"):
            print("Fichier de récapitulatif non trouvé, génération des données...")

            if not os.path.exists("./common/dataProjects.xlsx") or not os.path.exists("./common/answerProjects.xlsx") or not os.path.exists("./common/resultSolver.csv"):
                print("Fichiers de données non trouvés")
                return
            else:
                # Chargement des fichiers Excel
                dataProjects = pd.read_excel('./common/dataProjects.xlsx')
                answerProjects = pd.read_excel('./common/answerProjects.xlsx')
                result_solver = pd.read_csv('./common/resultSolver.csv')
                
                self.projets = [] # Liste pour stocker les objets de la classe Projet
                self.eleves = [] # Liste pour stocker les objets de la classe Eleve
                self.all_errors = [] # Liste pour stocker les objets de la classe Anomalies

                # Parcourir toutes les colonnes
                for colonne in result_solver.columns:
                # Vérifier si la colonne contient la valeur 1
                    # Créer une instance de la classe Projet
                    projet = Projet()
            
                    tmp_projet = dataProjects[dataProjects['Numéro du projet'] == int(colonne)+1]

                    # Affecter le nom de la colonne au champ nom de l'objet Projet
                    projet.numero_proj = tmp_projet["Numéro du projet"].values[0]

                    if (result_solver[colonne] == 1).any():
                        # Afficher les titres de ligne avec la valeur 1 dans cette colonne
                        lignes = result_solver[result_solver[colonne] == 1].index
                        
                        for ligne in lignes:
                            # Créer une instance de la classe Eleve
                            eleve = Eleve()
                            # Affecter le titre de la ligne au champ nom de l'objet Eleve
                            eleve.nom = answerProjects.iloc[ligne, 0]
                            eleve.prenom = answerProjects.iloc[ligne, 1]
                            eleve.mail = answerProjects.iloc[ligne, 2]
                            # Ajouter l'objet Eleve à la liste eleves de l'objet Projet
                            projet.eleves.append(eleve)
                            self.eleves.append(eleve)
                        # Ajouter l'objet Projet à la liste projets

                    else:
                        print(f"Le projet {colonne} n'a pas été sélectionné")

                    self.projets.append(projet)

                # Ajouter les informations des projets dans le conteneur scrollable_frame
                # Parcourir les self.projets et compléter les informations
                for projet in self.projets:
                    # Récupérer les informations du projet correspondant à son nom dans common/dataProjects.xlsx
                    infos_projet = dataProjects[dataProjects['Numéro du projet'] == projet.numero_proj]
                    if not infos_projet.empty:
                        infos_projet = infos_projet.iloc[0]
                        # Remplir les attributs de l'objet Projet
                        projet.intitule = infos_projet['Intitulé']
                        projet.par = infos_projet['Proposé par']
                        projet.equipe = infos_projet['Equipe']
                        projet.tel = infos_projet['Tél']
                        projet.mail = infos_projet['Mail']
                        projet.description = infos_projet['Description']
                        projet.nbmin = infos_projet['Minimum d\'étudiants']
                        projet.nbmax = infos_projet['Maximum d\'étudiants']
                        projet.entreprise = infos_projet['Entreprise']
                    else:
                        print(f"Aucune information trouvée pour le projet {projet.nom} dans le fichier common/dataProjects.xlsx")

                # Vérifier les anomalies
                self.all_errors = verifier_anomalies(result_solver, self.projets, self.eleves)

                

            # sauvegarde des résultats dans un fichier Excel
            # # Créer un dictionnaire pour stocker les données des projets et des élèves

            dataFrameProjets = pd.DataFrame([vars(s) for s in self.projets])
            cols = ['numero_proj', 'intitule', 'par', 'eleves', 'tel', 'mail', 'description', 'nbmin', 'nbmax', 'entreprise']
            dataFrameProjets = dataFrameProjets[cols]

            dataFrameEleves = pd.DataFrame([vars(s) for s in self.eleves])
            cols = ['nom', 'prenom', 'mail']
            dataFrameEleves = dataFrameEleves[cols]
            
            dataFrameAnomalies = pd.DataFrame([vars(s) for s in self.all_errors])

            # create a excel writer object
            with pd.ExcelWriter("./common/recap.xlsx") as writer:
                # use to_excel function and specify the sheet_name and index 
                # to store the dataframe in specified sheet
                dataFrameProjets.to_excel(writer, sheet_name="Projet", index=False)
                dataFrameEleves.to_excel(writer, sheet_name="Eleves", index=False)
                dataFrameAnomalies.to_excel(writer, sheet_name="Anomalies", index=False)

        else:
            print("Fichier de récapitulatif trouvé, chargement des données...")

            dataFrameProjets = pd.read_excel("./common/recap.xlsx", sheet_name="Projet")
            dataFrameEleves = pd.read_excel("./common/recap.xlsx", sheet_name="Eleves")
            dataFrameAnomalies = pd.read_excel("./common/recap.xlsx", sheet_name="Anomalies")

            self.projets = [Projet() for i in range(len(dataFrameProjets))]
            self.eleves = [Eleve() for i in range(len(dataFrameEleves))]
            self.all_errors = [Anomalies() for i in range(len(dataFrameAnomalies))]

            for i, row in dataFrameEleves.iterrows():
                self.eleves[i].nom = row["nom"]
                self.eleves[i].prenom = row["prenom"]
                self.eleves[i].mail = row["mail"]

            for i, row in dataFrameProjets.iterrows():
                self.projets[i].numero_proj = row["numero_proj"]
                self.projets[i].intitule = row["intitule"]
                self.projets[i].par = row["par"]
                self.projets[i].eleves = [eleve for eleve in self.eleves if eleve.mail in row["eleves"].replace("[", "").replace("]", "").replace("<Eleve>","").replace(" ","").split(",")]
                self.projets[i].tel = row["tel"]
                self.projets[i].mail = row["mail"]
                self.projets[i].description = row["description"]
                self.projets[i].nbmin = row["nbmin"]
                self.projets[i].nbmax = row["nbmax"]
                self.projets[i].entreprise = row["entreprise"]

            for i, row in dataFrameAnomalies.iterrows():
                self.all_errors[i].error = row["error"]
                if "eleve" in row:
                    self.all_errors[i].student = [eleve for eleve in self.eleves if eleve.mail in row["eleve"]][0]
                if "projet" in row:
                    self.all_errors[i].projet = [projet for projet in self.projets if projet.intitule in row["projet"]][0]
        self.show()

    def show(self):
        label = CTkLabel(self, text ="SolverProcess")
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
        
        # Ajouter les informations des self.projets dans le conteneur scrollable_frame
        for projet in self.projets:
            card = CTkFrame(right_frame)
            card.pack(padx=5, pady=5, fill="x")

            projet_label = CTkLabel(card, text=projet.representation() ,justify="left")
            projet_label.pack(padx=10, pady=10, anchor="w")

        for i, error in enumerate(self.all_errors):
            card = CTkFrame(left_frame, fg_color="red")
            card.pack(padx=5, pady=5, fill="x")

            error_label = CTkLabel(card, text=error, anchor="w", justify="left", fg_color="red")
            error_label.grid(row=i, column=1, padx=5, pady=2)

            solve_button = CTkButton(card, text="Résoudre", command=lambda: solve_function())
            solve_button.grid(row=i, column=0, padx=5, pady=10)

# all_errors = la fonction 
