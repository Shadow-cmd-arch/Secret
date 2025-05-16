import tkinter as tk
from tkinter import messagebox
import pyautogui
import keyboard
import sys
import time
import random

# Fonction pour vérifier le mot de passe
def check_password(password_entry):
    entered_password = password_entry.get()  # Récupérer le mot de passe entré

    # Vérifier si le mot de passe est correct
    if entered_password == "Hacker_47":
        messagebox.showinfo("Accès autorisé", "Mot de passe correct ! Le programme va s'arrêter.")
        print("Accès autorisé. Le programme va s'arrêter.")
        sys.exit()  # Arrêter le programme si le mot de passe est correct
    else:
        messagebox.showerror("Erreur", "Mot de passe incorrect.")
        print("Mot de passe incorrect.")

# Fonction pour afficher la fenêtre de mot de passe lorsqu'on appuie sur '*'
def show_password_window():
    # Créer une fenêtre tkinter
    root = tk.Tk()
    root.title("Connexion Sécurisée")
    root.geometry("350x250")  # Taille de la fenêtre
    root.config(bg="#282C34")  # Fond de la fenêtre

    # Ajouter un titre personnalisé en haut
    title_label = tk.Label(root, text="Accès Restreint", font=("Helvetica", 18, "bold"), fg="#FF6347", bg="#282C34")
    title_label.pack(pady=10)

    # Frame pour organiser les éléments
    frame = tk.Frame(root, bg="#282C34")
    frame.pack(pady=20)

    # Ajouter un label personnalisé pour la demande de mot de passe
    label = tk.Label(frame, text="Entrez le mot de passe :", font=("Arial", 14), bg="#282C34", fg="white")
    label.grid(row=0, column=0, pady=10, padx=20)

    # Ajouter un champ de texte pour le mot de passe
    password_entry = tk.Entry(frame, show="*", width=30, font=("Arial", 12), bd=2, relief="solid", highlightthickness=2, highlightcolor="#FF6347")
    password_entry.grid(row=1, column=0, pady=10, padx=20)

    # Fonction pour l'effet de survol des boutons
    def on_hover(button):
        button.config(bg="#FF6347", fg="white")

    def on_leave(button):
        button.config(bg="#4CAF50", fg="white")

    # Ajouter un bouton de validation avec effet de survol
    login_button = tk.Button(frame, text="Valider", command=lambda: check_password(password_entry), font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", bd=3, width=20)
    login_button.grid(row=2, column=0, pady=10)
    login_button.bind("<Enter>", lambda event, button=login_button: on_hover(button))  # Effet survol
    login_button.bind("<Leave>", lambda event, button=login_button: on_leave(button))  # Effet de sortie

    # Ajouter un bouton pour quitter si l'utilisateur n'a pas le mot de passe avec effet de survol
    cancel_button = tk.Button(frame, text="Annuler", command=root.quit, font=("Arial", 12), bg="#f44336", fg="white", relief="raised", bd=3, width=20)
    cancel_button.grid(row=3, column=0, pady=10)
    cancel_button.bind("<Enter>", lambda event, button=cancel_button: on_hover(button))  # Effet survol
    cancel_button.bind("<Leave>", lambda event, button=cancel_button: on_leave(button))  # Effet de sortie

    # Ajouter une icône à la fenêtre (tu dois avoir une icône .ico)
    try:
        root.iconbitmap("lock_icon.ico")  # Remplacer par le chemin de ton icône .ico
    except:
        print("Icône non trouvée, pas de problème.")

    # Lancer la boucle principale de l'interface tkinter
    root.mainloop()

# Fonction pour déplacer la souris et cliquer de manière aléatoire
def move_mouse_randomly():
    screen_width, screen_height = pyautogui.size()  # Taille de l'écran
    random_x = random.randint(0, screen_width)  # Coordonnée X aléatoire
    random_y = random.randint(0, screen_height)  # Coordonnée Y aléatoire

    # Déplacer la souris en douceur vers la nouvelle position
    pyautogui.moveTo(random_x, random_y, duration=random.uniform(0.5, 1.0))  # Temps de déplacement aléatoire

    # Cliquer à l'endroit où la souris est positionnée
    if random.random() < 0.3:  # 30% de chances de cliquer
        pyautogui.click()
        print(f"Souris déplacée vers {random_x}, {random_y} et a cliqué.")
    else:
        print(f"Souris déplacée vers {random_x}, {random_y} sans cliquer.")

# Fonction pour créer un "bug visuel" avec des lignes de pixels aléatoires
def pixel_bug():
    screen_width, screen_height = pyautogui.size()
    # Générer des lignes de "bugs" aléatoires
    for _ in range(random.randint(3, 6)):
        x1 = random.randint(0, screen_width)
        y1 = random.randint(0, screen_height)
        x2 = random.randint(0, screen_width)
        y2 = random.randint(0, screen_height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Couleur aléatoire
        pyautogui.dragTo(x2, y2, duration=random.uniform(0.2, 0.5), button='left')  # Simule un bug visuel

# Boucle principale de contrôle
while True:
    # Si la touche '*' est pressée, afficher la fenêtre de mot de passe
    if keyboard.is_pressed('*'):
        show_password_window()  # Afficher la fenêtre pop-up de mot de passe

    # Simuler des bugs de pixels de manière aléatoire
    if random.random() < 0.1:  # 10% de chances de simuler un bug de pixels
        pixel_bug()

    # Déplacer la souris aléatoirement toutes les 2 à 4 secondes
    if random.random() < 0.2:  # 20% de chances de déplacer la souris
        move_mouse_randomly()

    # Autres act   # simulate_visual_bug()

    # Utilisation de pyautogui.PAUSE pour la pause
    pyautogui.PAUSE = 0.1  # Pause entre chaque action de pyautogui, ici on met 0.1ions du programme (comme les bugs visuels, etc.) peuvent être ici
    # Exemple:
 
    time.sleep(0.1)  # Vérification toutes les 100ms