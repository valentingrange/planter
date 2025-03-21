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

# Paramètres de l'arbre
largeur_arbre = 10
hauteur_arbre = 10
x_arbre = x_personnage + 25  # L'arbre commence à 25 px à droite du personnage
y_arbre = y_personnage  # L'arbre commence à la même hauteur que le personnage

# Créer un canevas pour dessiner
canvas = tk.Canvas(root, width=largeur_fenetre, height=hauteur_fenetre)
canvas.pack()

# Créer une plateforme (rectangle vert qui occupe toute la largeur et la hauteur de la fenêtre)
canvas.create_rectangle(0, 0, largeur_fenetre, hauteur_fenetre, fill="green")

# Créer un personnage (rectangle bleu)
personnage = canvas.create_rectangle(x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage, fill="blue")

# Créer un arbre (rectangle rouge)
arbre = canvas.create_rectangle(x_arbre, y_arbre, x_arbre + largeur_arbre, y_arbre + hauteur_arbre, fill="red")

# Déplacer le personnage et l'arbre à gauche
def deplacer_gauche(event):
    global x_personnage, x_arbre
    if x_personnage > 0:  # Limiter à la gauche de la fenêtre
        x_personnage -= vitesse
        x_arbre -= vitesse  # Déplace également l'arbre
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)
        canvas.coords(arbre, x_arbre, y_arbre, x_arbre + largeur_arbre, y_arbre + hauteur_arbre)

# Déplacer le personnage et l'arbre à droite
def deplacer_droite(event):
    global x_personnage, x_arbre
    if x_personnage < largeur_fenetre - largeur_personnage:  # Limiter à la droite de la fenêtre
        x_personnage += vitesse
        x_arbre += vitesse  # Déplace également l'arbre
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)
        canvas.coords(arbre, x_arbre, y_arbre, x_arbre + largeur_arbre, y_arbre + hauteur_arbre)

# Déplacer le personnage et l'arbre vers le haut
def deplacer_haut(event):
    global y_personnage, y_arbre
    if y_personnage > 0:  # Limiter en haut de la fenêtre
        y_personnage -= vitesse  # Décale vers le haut
        y_arbre -= vitesse  # Déplace également l'arbre
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)
        canvas.coords(arbre, x_arbre, y_arbre, x_arbre + largeur_arbre, y_arbre + hauteur_arbre)

# Déplacer le personnage et l'arbre vers le bas
def deplacer_bas(event):
    global y_personnage, y_arbre
    if y_personnage < hauteur_fenetre - hauteur_personnage:  # Limiter en bas de la fenêtre
        y_personnage += vitesse  # Décale vers le bas
        y_arbre += vitesse  # Déplace également l'arbre
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)
        canvas.coords(arbre, x_arbre, y_arbre, x_arbre + largeur_arbre, y_arbre + hauteur_arbre)

# Associer les touches du clavier aux actions
root.bind("<Left>", deplacer_gauche)
root.bind("<Right>", deplacer_droite)
root.bind("<Up>", deplacer_haut)
root.bind("<Down>", deplacer_bas)

# Lancer la fenêtre
root.mainloop()
