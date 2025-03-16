import tkinter as tk

# Créer une fenêtre de jeu
root = tk.Tk()
root.title("Jeu de plateforme")

# Dimensions de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")

# Paramètres du personnage
largeur_personnage = 50
hauteur_personnage = 50
x_personnage = largeur_fenetre // 2 - largeur_personnage // 2
y_personnage = hauteur_fenetre - hauteur_personnage - 50  # Position du personnage sur la plateforme
vitesse = 50  # Vitesse de déplacement du personnage

# Créer un canevas pour dessiner
canvas = tk.Canvas(root, width=largeur_fenetre, height=hauteur_fenetre)
canvas.pack()

# Créer une plateforme (simple rectangle vert)
canvas.create_rectangle(0, hauteur_fenetre - 50, largeur_fenetre, hauteur_fenetre, fill="green")

# Créer un personnage (rectangle bleu)
personnage = canvas.create_rectangle(x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage, fill="blue")

# Déplacer le personnage à gauche
def deplacer_gauche(event):
    global x_personnage
    if x_personnage > 0:
        x_personnage -= vitesse
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)

# Déplacer le personnage à droite
def deplacer_droite(event):
    global x_personnage
    if x_personnage < largeur_fenetre - largeur_personnage:
        x_personnage += vitesse
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)

# Déplacer le personnage vers le haut (saut)
def deplacer_haut(event):
    global y_personnage
    if y_personnage > 0:
        y_personnage -= vitesse  # Décale vers le haut
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)

# Déplacer le personnage vers le bas
def deplacer_bas(event):
    global y_personnage
    if y_personnage < hauteur_fenetre - hauteur_personnage - 50:  # Limite à la plateforme
        y_personnage += vitesse  # Décale vers le bas
        canvas.coords(personnage, x_personnage, y_personnage, x_personnage + largeur_personnage, y_personnage + hauteur_personnage)

# Associer les touches du clavier aux actions
root.bind("<Left>", deplacer_gauche)
root.bind("<Right>", deplacer_droite)
root.bind("<Up>", deplacer_haut)  # Touche pour déplacer vers le haut
root.bind("<Down>", deplacer_bas)  # Touche pour déplacer vers le bas

# Lancer la fenêtre
root.mainloop()
