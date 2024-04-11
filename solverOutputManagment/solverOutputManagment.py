import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkScrollableFrame
import math
import pandas as pd


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

    def __str__(self):
        return f"Projet {self.intitule} :\n - Min : {int(self.nbmin) if not math.isnan(self.nbmin) else 3}\n - Max : {int(self.nbmax) if not math.isnan(self.nbmax) else 7}\n - Equipe de {len(self.eleves)} étudiants :\n" + "\n".join([f"\t- {eleve.nom} {eleve.prenom}" for eleve in self.eleves]) + "\n"
    
    def __repr__(self):
        return f"<Projet> Projet {self.intitule} : {len(self.eleves)} élèves"

class Eleve:
    def __init__(self):
        self.nom = ""
        self.prenom = ""
        self.mail = ""

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Anomalies:
    def __init__(self):
        self.error = ""
    def __str__(self):
        return f"Warning : {self.error}"

class Epasdeproj(Anomalies):
    def __init__(self):
        super().__init__()
        self.student = None


class Etropdeproj(Anomalies):
    def __init__(self):
        super().__init__()
        self.student = None

 

class Ppasassezeleve(Anomalies):
    def __init__(self):
        super().__init__()
        self.projet = None
    
    

class Ptropeleve(Anomalies):
    def __init__(self):
        super().__init__()
        self.projet = None
    

def verifier_anomalies(resultSolver, projets, eleves):
        all_errors = []
        for index, row in resultSolver.iterrows():
            if sum(row.iloc[1:]) < 1:
                tmp = Epasdeproj()
                tmp.student = eleves[index]
                tmp.error = f"{tmp.student.nom} {tmp.student.prenom} n'est pas affecté à un projet"
                all_errors.append(tmp.error)

            if sum(row.iloc[1:]) > 1:
                tmp = Etropdeproj()
                tmp.student = eleves[index]
                tmp.error = f"{tmp.student.nom} {tmp.student.prenom} est affecté à plusieurs projets"
                all_errors.append(tmp.error)

        df_projet = pd.read_excel("./common/dataProjects.xlsx")

        print("Projets : ", projets)
        print("longgggggggggggggggggggggggggggggg",len(projets))

        for projet in projets:
            print("projet : ", projet)
            corresponding_row = df_projet[df_projet["Numéro du projet"] == projet.numero_proj]
            somme_etudiants = len(projet.eleves)
            print("somme_etudiants : ", somme_etudiants)

            if somme_etudiants < corresponding_row["Minimum d'étudiants"].values[0]:
                tmp = Ppasassezeleve()
                tmp.projet = projet
                tmp.error = f"{tmp.projet.intitule} n'a pas le minimum requis d'étudiants"
                all_errors.append(tmp.error)

            if somme_etudiants > corresponding_row["Maximum d'étudiants"].values[0]:
                tmp = Ptropeleve()
                tmp.projet = projet
                tmp.error = f"{tmp.projet.intitule} contient trop d'étudiants"
                all_errors.append(tmp.error)

        return all_errors


    

# Création de l'interface utilisateur avec tkinter
class SolverOutputManagment(CTkFrame):
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
        
        # Chargement des fichiers Excel
        dataProjects = pd.read_excel('./common/dataProjects.xlsx')
        answerProjects = pd.read_excel('./common/answerProjects.xlsx')
        result_solver = pd.read_csv('./common/resultSolver.csv')
        
        self.projets = [] # Liste pour stocker les objets de la classe Projet
        self.eleves = [] # Liste pour stocker les objets de la classe Eleve

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

        print("Anomalies -----------------------------\n", self.all_errors)
        


        # # Initialiser un dictionnaire pour stocker les données des projets et des élèves
        # donnees_projet_eleves = {}

        # # Parcourir chaque colonne du DataFrame
        # for colonne in result_solver.columns:
        #     # Vérifier si la colonne contient au moins un 1
        #     if (result_solver[colonne] == 1).any():
        #         # Récupérer le nom du projet (première cellule de la colonne)
        #         nom_projet = colonne
        #         # Initialiser une liste pour stocker les noms des élèves
        #         eleves_projet = []
        #         # Parcourir chaque ligne de la colonne
        #         for index, valeur in result_solver[colonne].items():
        #             # Vérifier si la valeur est égale à 1
        #             if valeur == 1:
        #                 # Récupérer le nom de l'élève (première cellule de la ligne)
        #                 nom_eleve = result_solver.iloc[index, 0]
        #                 # Ajouter le nom de l'élève à la liste des élèves du projet
        #                 eleves_projet.append(nom_eleve)
        #         # Ajouter les élèves du projet au dictionnaire
        #         donnees_projet_eleves[nom_projet] = eleves_projet

        # # Créer un DataFrame à partir du dictionnaire
        # df_excel = pd.DataFrame.from_dict(donnees_projet_eleves, orient='index').transpose()

        # # Spécifier le nom du fichier Excel de sortie
        # nom_fichier_sortie = "resultats_output2.xlsx"

        # # Écrire les données dans un nouveau fichier Excel
        # df_excel.to_excel(nom_fichier_sortie, index=False)
        
        #print(f"Les résultats ont été écrits dans le fichier Excel : {nom_fichier_sortie}")

        self.show()

    def show(self):
        # Cadre principal pour contenir les cadres gauche et droit
        self.grid_columnconfigure(0, weight=1)  # Colonne 0
        self.grid_columnconfigure(1, weight=1)  # Colonne 1
        self.grid_rowconfigure(0, weight=1)     # Ligne 0
        
        # Cadre gauche avec un poids de 1
        left_frame = CTkScrollableFrame(self)
        left_frame.grid(row=0, column=0, padx=5, sticky="nsew")
        
        # Cadre droit avec un poids de 1
        right_frame = CTkScrollableFrame(self)
        right_frame.grid(row=0, column=1, padx=5, sticky="nsew")
        
        # Ajouter les informations des self.projets dans le conteneur scrollable_frame
        for projet in self.projets:
            card = CTkFrame(right_frame)
            card.pack(padx=5, pady=5, fill="x")

            projet_label = CTkLabel(card, text=projet,justify="left")
            projet_label.pack(padx=10, pady=10, anchor="w")

        for i, error in enumerate(self.all_errors):
            error_label = CTkLabel(left_frame, text=error, bg_color="red", anchor="w", justify="left")
            error_label.grid(row=i, column=0, padx=5, pady=2)

# all_errors = la fonction 
