import tkinter as tk

# Créer une fenêtre de jeu
root = tk.Tk()
root.title("Jeu de plateforme")

# Dimensions de la fenêtre
largeur_fenetre = 850
hauteur_fenetre = 650
root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")

# Paramètres du personnage
largeur_personnage = 50
hauteur_personnage = 50
x_personnage = largeur_fenetre // 2 - largeur_personnage // 2
y_personnage = hauteur_fenetre // 2 - hauteur_personnage // 2  # Initialement centré dans la fenêtre
vitesse = 50  # Vitesse de déplacement du personnage

# Paramètres de l'arbre_1
largeur_arbre_1 = 10
hauteur_arbre_1 = 10
x_arbre_1 = x_personnage + 50
y_arbre_1 = y_personnage + 20

# Paramètres de l'arbre_2
largeur_arbre_2 = 10
hauteur_arbre_2 = 10
x_arbre_2 = x_personnage - 10
y_arbre_2 = y_personnage + 20

# Variables de contrôle pour les arbres
controle_arbre_1 = True  # Par défaut, l'arbre_1 suit le personnage
controle_arbre_2 = True  # Par défaut, l'arbre_2 suit le personnage

# Créer un canevas pour dessiner
canvas = tk.Canvas(root, width=largeur_fenetre, height=hauteur_fenetre)
canvas.pack()

# Créer une plateforme (rectangle vert qui occupe toute la largeur et la hauteur de la fenêtre)
canvas.create_rectangle(0, 0, largeur_fenetre, hauteur_fenetre, fill="green")

# Créer un personnage (rectangle bleu)
personnage = canvas.create_rectangle(x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage, fill="blue")

# Créer un arbre_1 (rectangle rouge)
arbre_1 = canvas.create_rectangle(x_arbre_1, y_arbre_1, x_arbre_1 + largeur_arbre_1, y_arbre_1 + hauteur_arbre_1, fill="red")

# Créer un arbre_2 (rectangle rouge)
arbre_2 = canvas.create_rectangle(x_arbre_2, y_arbre_2, x_arbre_2 + largeur_arbre_2, y_arbre_2 + hauteur_arbre_2, fill="red")

# Déplacer le personnage et l'arbre_1 à gauche
def deplacer_gauche(event):
    global x_personnage, x_arbre_1, x_arbre_2
    if x_personnage > 0:  # Limiter à la gauche de la fenêtre
        x_personnage -= vitesse
        if controle_arbre_1:  # Si le contrôle de l'arbre_1 est actif, on déplace l'arbre_1
            x_arbre_1 -= vitesse
        if controle_arbre_2:  # Si le contrôle de l'arbre_2 est actif, on déplace l'arbre_2
            x_arbre_2 -= vitesse
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)
        canvas.coords(arbre_1, x_arbre_1, y_arbre_1, x_arbre_1 + largeur_arbre_1, y_arbre_1 + hauteur_arbre_1)
        canvas.coords(arbre_2, x_arbre_2, y_arbre_2, x_arbre_2 + largeur_arbre_2, y_arbre_2 + hauteur_arbre_2)

# Déplacer le personnage et l'arbre_1 à droite
def deplacer_droite(event):
    global x_personnage, x_arbre_1, x_arbre_2
    if x_personnage < largeur_fenetre - largeur_personnage:  # Limiter à la droite de la fenêtre
        x_personnage += vitesse
        if controle_arbre_1:  # Si le contrôle de l'arbre_1 est actif, on déplace l'arbre_1
            x_arbre_1 += vitesse
        if controle_arbre_2:  # Si le contrôle de l'arbre_2 est actif, on déplace l'arbre_2
            x_arbre_2 += vitesse
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)
        canvas.coords(arbre_1, x_arbre_1, y_arbre_1, x_arbre_1 + largeur_arbre_1, y_arbre_1 + hauteur_arbre_1)
        canvas.coords(arbre_2, x_arbre_2, y_arbre_2, x_arbre_2 + largeur_arbre_2, y_arbre_2 + hauteur_arbre_2)

# Déplacer le personnage et l'arbre_1 vers le haut
def deplacer_haut(event):
    global y_personnage, y_arbre_1, y_arbre_2
    if y_personnage > 0:  # Limiter en haut de la fenêtre
        y_personnage -= vitesse  # Décale vers le haut
        if controle_arbre_1:  # Si le contrôle de l'arbre_1 est actif, on déplace l'arbre_1
            y_arbre_1 -= vitesse
        if controle_arbre_2:  # Si le contrôle de l'arbre_2 est actif, on déplace l'arbre_2
            y_arbre_2 -= vitesse
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)
        canvas.coords(arbre_1, x_arbre_1, y_arbre_1, x_arbre_1 + largeur_arbre_1, y_arbre_1 + hauteur_arbre_1)
        canvas.coords(arbre_2, x_arbre_2, y_arbre_2, x_arbre_2 + largeur_arbre_2, y_arbre_2 + hauteur_arbre_2)

# Déplacer le personnage et l'arbre_1 vers le bas
def deplacer_bas(event):
    global y_personnage, y_arbre_1, y_arbre_2
    if y_personnage < hauteur_fenetre - hauteur_personnage:  # Limiter en bas de la fenêtre
        y_personnage += vitesse  # Décale vers le bas
        if controle_arbre_1:  # Si le contrôle de l'arbre_1 est actif, on déplace l'arbre_1
            y_arbre_1 += vitesse
        if controle_arbre_2:  # Si le contrôle de l'arbre_2 est actif, on déplace l'arbre_2
            y_arbre_2 += vitesse
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)
        canvas.coords(arbre_1, x_arbre_1, y_arbre_1, x_arbre_1 + largeur_arbre_1, y_arbre_1 + hauteur_arbre_1)
        canvas.coords(arbre_2, x_arbre_2, y_arbre_2, x_arbre_2 + largeur_arbre_2, y_arbre_2 + hauteur_arbre_2)

# Fonction pour désactiver le contrôle de l'arbre_1
def desactiver_controle_arbre_1(event):
    global controle_arbre_1
    controle_arbre_1 = False  # Désactive le contrôle de l'arbre_1

# Fonction pour désactiver le contrôle de l'arbre_2
def desactiver_controle_arbre_2(event):
    global controle_arbre_2
    controle_arbre_2 = False  # Désactive le contrôle de l'arbre_2

# Associer les touches du clavier aux actions
root.bind("<Left>", deplacer_gauche)
root.bind("<Right>", deplacer_droite)
root.bind("<Up>", deplacer_haut)
root.bind("<Down>", deplacer_bas)
root.bind("&", desactiver_controle_arbre_1)
root.bind("é", desactiver_controle_arbre_2)

# Lancer la fenêtre
root.mainloop()
