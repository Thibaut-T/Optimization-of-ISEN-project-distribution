import tkinter as tk
from tkinter import ttk
import pandas as pd

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

# Charger le fichier Excel
donnees = pd.read_excel('test_projet.xlsx')

projets = []  # Liste pour stocker les objets de la classe Projet

# Parcourir toutes les colonnes
for colonne in donnees.columns:
    # Vérifier si la colonne contient la valeur 1
    if (donnees[colonne] == 1).any():
        # Créer une instance de la classe Projet
        projet = Projet()
        # Affecter le nom de la colonne au champ nom de l'objet Projet
        projet.nom = colonne
        # Afficher le titre de la colonne
        print(f"Projet : {colonne}")
        # Afficher les titres de ligne avec la valeur 1 dans cette colonne
        lignes = donnees[donnees[colonne] == 1].index
        for ligne in lignes:
            # Récupérer le titre de la ligne (première cellule de la ligne)
            titre_ligne = donnees.iloc[ligne, 0]  # Utilisation de iloc pour accéder à la première cellule de la ligne
            # Créer une instance de la classe Eleve
            eleve = Eleve()
            # Affecter le titre de la ligne au champ nom de l'objet Eleve
            eleve.nom = titre_ligne
            # Ajouter l'objet Eleve à la liste eleves de l'objet Projet
            projet.eleves.append(eleve)
            print(f" - Elève : {titre_ligne}")
        # Ajouter l'objet Projet à la liste projets
        projets.append(projet)

# Charger les données du fichier output.xlsx
donnees_output = pd.read_excel('output.xlsx')

# Parcourir les projets et compléter les informations
for projet in projets:
    # Récupérer les informations du projet correspondant à son nom dans output.xlsx
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
        print(f"Aucune information trouvée pour le projet {projet.nom} dans le fichier output.xlsx")

# Créer l'interface utilisateur avec tkinter
class SolverOutputManagment(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="white")

        self.previous_frame = "solverProcess"
        self.next_frame = "exportStudentDistribution"
        self.objective_fulfilled = True


        self.controller = controller
        self.show()
    
    def reload(self):
        children = self.winfo_children()
        for item in children:
            item.pack_forget()
            item.grid_forget()
        self.show()
    
    def show(self):
        # label of frame SolverOutputManagment
        label = ttk.Label(self, text ="SolverOutputManagment")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

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
        mid_x = parent.winfo_width() // 2  # Coordonnée x au milieu de la fenêtre
        
        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((mid_x, 0), window=scrollable_frame, anchor="nw")

        # Ajouter les informations des projets dans le conteneur scrollable_frame
        for projet in projets:
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

        # Configurer le Canvas pour le défilement
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

if __name__ == "__main__":
    # Créer une instance de Tkinter
    root = tk.Tk()
    root.title("Gestion des projets")

    # Créer une instance de SolverOutputManagment
    solver_output = SolverOutputManagment(root, None)
    solver_output.pack(expand=True, fill="both")

    # Lancer la boucle principale de Tkinter
    root.mainloop()
