import tkinter as tk
from tkinter import ttk
import pandas as pd


#####################################################################################
# Définition des classes existantes

class Projet:
    def __init__(self):
        self.nom = ""
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

class Eleve:
    def __init__(self):
        self.nom = ""
        self.prenom = ""
        self.mail = ""

class Anomalies:
    def __init__(self):
        self.error = ""
    def __str__(self):
        return f"Warning : {self.error}"

class Epasdeproj(Anomalies):
    def __init__(self):
        super().__init__()
        self.student = ""


class Etropdeproj(Anomalies):
    def __init__(self):
        super().__init__()
        self.student = ""

    
        

class Ppasassezeleve(Anomalies):
    def __init__(self):
        super().__init__()
        self.projet = ""
    
    

class Ptropeleve(Anomalies):
    def __init__(self):
        super().__init__()
        self.projet = ""
    

def verifier_anomalies(self, donnees_anomalie):
        all_errors = []
        for index, row in donnees_anomalie.iterrows():
            if sum(row.iloc[1:]) < 1:
                tmp = Epasdeproj()
                tmp.error = f"{row.iloc[0]} n'est pas affecté à un projet"
                print(tmp)
                all_errors.append(tmp.error)

            if sum(row.iloc[1:]) > 1:
                tmp = Etropdeproj()
                tmp.error = f"{row.iloc[0]} est affecté à plusieurs projets"
                print(tmp)
                all_errors.append(tmp.error)
        
        df_projet = pd.read_excel("dataProjects.xlsx")

        for index, row in df_projet.iterrows():
            intitule_projet = row["Intitulé"]
            nb_min_etudiants = row["Minimum d'étudiants"]
            somme_etudiants = donnees_anomalie[intitule_projet].sum()
            
            if somme_etudiants < nb_min_etudiants:
                self.error = f"{intitule_projet} n'a pas le minimum requis d'étudiants"
                print(self)
        
            intitule_projet = row["Intitulé"]
            nb_max_etudiants = row["Maximum d'étudiants"]
            somme_etudiants = donnees_anomalie[intitule_projet].sum()
            
            if somme_etudiants > nb_max_etudiants:
                self.error = f"{intitule_projet} contient trop d'étudiants"
                print(self)

        return all_errors



    

# Création de l'interface utilisateur avec tkinter
class SolverOutputManagment(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")

        self.previous_frame = "solverProcess"
        self.next_frame = "exportStudentDistribution"
        self.objective_fulfilled = True
        self.projets = []
        self.parent = parent
        self.controller = controller

        self.reload()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        
        self.all_errors = []
        
        try: 
            # Chargement des fichiers Excel
            donnees_output = pd.read_excel('output.xlsx')
            donnees_output2 = pd.read_excel('output2.xlsx')
            donnees_test_projet = pd.read_excel('test_projet.xlsx')


            self.projets = [] # Liste pour stocker les objets de la classe Projet

            # Parcourir toutes les colonnes
            for colonne in donnees_test_projet.columns:
            # Vérifier si la colonne contient la valeur 1
                if (donnees_test_projet[colonne] == 1).any():
                    # Créer une instance de la classe Projet
                    projet = Projet()
                    # Affecter le nom de la colonne au champ nom de l'objet Projet
                    projet.nom = colonne
                    # Afficher le titre de la colonne
                    print(f"Projet : {colonne}")
                    # Afficher les titres de ligne avec la valeur 1 dans cette colonne
                    lignes = donnees_test_projet[donnees_test_projet[colonne] == 1].index
                    for ligne in lignes:
                        # Récupérer le titre de la ligne (première cellule de la ligne)
                        titre_ligne = donnees_test_projet.iloc[ligne, 0]  # Utilisation de iloc pour accéder à la première cellule de la ligne
                        # Créer une instance de la classe Eleve
                        eleve = Eleve()
                        # Affecter le titre de la ligne au champ nom de l'objet Eleve
                        eleve.nom = titre_ligne
                        # Ajouter l'objet Eleve à la liste eleves de l'objet Projet
                        projet.eleves.append(eleve)
                        print(f" - Elève : {titre_ligne}")
                    # Ajouter l'objet Projet à la liste projets
                    self.projets.append(projet)

            
            # Vérification des données à la recherche d'anomalie
            epasdeproj_anomalies = Epasdeproj()
            epasdeproj_anomalies.verifier_anomalies(donnees_output2)
            if epasdeproj_anomalies.error:
                self.all_errors.append(str(epasdeproj_anomalies))
            

            etropdeproj_anomalies = Etropdeproj()
            etropdeproj_anomalies.verifier_anomalies(donnees_output2)
            if etropdeproj_anomalies.error:
                self.all_errors.append(str(etropdeproj_anomalies))
            

            ppasassezeleve_anomalies = Ppasassezeleve()
            ppasassezeleve_anomalies.verifier_anomalies(donnees_output2, 'output.xlsx')
            if ppasassezeleve_anomalies.error:
                self.all_errors.append(str(ppasassezeleve_anomalies))

            ptropeleve_anomalies = Ptropeleve()
            ptropeleve_anomalies.verifier_anomalies(donnees_output2, 'output.xlsx')
            if ptropeleve_anomalies.error:
                self.all_errors.append(str(ptropeleve_anomalies))

            # Ajouter les informations des projets dans le conteneur scrollable_frame
            # Parcourir les self.projets et compléter les informations
            for projet in self.projets:
                # Récupérer les informations du projet correspondant à son nom dans common/dataProjects.xlsx
                infos_projet = donnees_output[donnees_output['Intitulé'] == projet.nom]
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


            # Initialiser un dictionnaire pour stocker les données des projets et des élèves
            donnees_projet_eleves = {}

            # Parcourir chaque colonne du DataFrame
            for colonne in donnees_output2.columns:
                # Vérifier si la colonne contient au moins un 1
                if (donnees_output2[colonne] == 1).any():
                    # Récupérer le nom du projet (première cellule de la colonne)
                    nom_projet = colonne
                    # Initialiser une liste pour stocker les noms des élèves
                    eleves_projet = []
                    # Parcourir chaque ligne de la colonne
                    for index, valeur in donnees_output2[colonne].items():
                        # Vérifier si la valeur est égale à 1
                        if valeur == 1:
                            # Récupérer le nom de l'élève (première cellule de la ligne)
                            nom_eleve = donnees_output2.iloc[index, 0]
                            # Ajouter le nom de l'élève à la liste des élèves du projet
                            eleves_projet.append(nom_eleve)
                    # Ajouter les élèves du projet au dictionnaire
                    donnees_projet_eleves[nom_projet] = eleves_projet

            # Créer un DataFrame à partir du dictionnaire
            df_excel = pd.DataFrame.from_dict(donnees_projet_eleves, orient='index').transpose()

            # Spécifier le nom du fichier Excel de sortie
            nom_fichier_sortie = "resultats_output2.xlsx"

            # Écrire les données dans un nouveau fichier Excel
            df_excel.to_excel(nom_fichier_sortie, index=False)

            print(f"Les résultats ont été écrits dans le fichier Excel : {nom_fichier_sortie}")
                
        except FileNotFoundError:
            print("Fichier non trouvé")
            self.projets = []

        self.show()

    def show(self):
        # Cadre principal pour contenir les cadres gauche et droit
        self.grid_columnconfigure(0, weight=1)  # Colonne 0
        self.grid_columnconfigure(1, weight=1)  # Colonne 1
        self.grid_rowconfigure(0, weight=1)     # Ligne 0
        
        # Cadre gauche avec un poids de 1
        left_frame = tk.Frame(self, bg="purple")
        left_frame.grid(row=0, column=0, sticky="nsew")
        
        # Cadre droit avec un poids de 1
        right_frame = tk.Frame(self, bg="green")
        right_frame.grid(row=0, column=1, sticky="nsew")

        canvas = tk.Canvas(right_frame, bd=0)
        scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Conteneur pour les éléments dans le Canvas
        # Calcul des coordonnées au milieu de la fenêtre
        mid_x = self.parent.winfo_width() // 2  # Coordonnée x au milieu de la fenêtre
        
        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((mid_x, 0), window=scrollable_frame, anchor="nw")
        
        # Ajouter les informations des self.projets dans le conteneur scrollable_frame
        for projet in self.projets:
            projet_label = ttk.Label(scrollable_frame, text=f"Nom du projet : {projet.nom}\n"
                                                        f"Elèves du projet :\n"
                                                        f"Informations du projet :\n"
                                                        f"Intitulé : {projet.intitule}\n"
                                                        f"Proposé par : {projet.par}\n"
                                                        f"Equipe : {projet.equipe}\n"
                                                        f"Téléphone : {projet.tel}\n"
                                                        f"Mail : {projet.mail}\n"
                                                        f"Description : {projet.description}\n"
                                                        f"Minimum d'étudiants : {projet.nbmin}\n"
                                                        f"Maximum d'étudiants : {projet.nbmax}\n"
                                                        f"Entreprise : {projet.entreprise}\n",anchor="e",justify="right")
            projet_label.pack(padx=10, pady=10, anchor="e")
            
        # Ajoutez des étiquettes dans le cadre gauche pour afficher les anomalies
        error_frame = tk.Frame(left_frame, bg="red")
        error_frame.pack(fill="both", padx=10, pady=10)
        
        print(self.all_errors)

        for i, error in enumerate(self.all_errors):
            error_label = tk.Label(error_frame, text=error, bg="red", fg="white")
            error_label.grid(row=i, column=0, padx=5, pady=2)

        # Configurer le Canvas pour le défilement
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))





