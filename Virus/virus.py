import pyautogui
import keyboard
import random
import time
import os
from plyer import notification  # Pour les notifications système
import winsound  # Pour les sons inquiétants

# Variable pour garder une trace de l'état de l'utilisateur
interaction_count = 0

# Liste de messages effrayants
messages = [
    "Je suis là...",
    "Tu ne peux pas m'échapper...",
    "J'ai vu ce que tu as fait...",
    "Tu crois avoir le contrôle ?",
    "Je t'ai vu... je suis partout.",
    "Ne ferme pas les yeux...",
    "C'est trop tard pour revenir en arrière."
]

# Liste de phrases spécifiques pour le Bloc-notes
notepad_messages = [
    "Tu n'es jamais seul... Quelqu'un te regarde.",
    "Regarde derrière toi... Je suis là.",
    "La porte est fermée, mais je suis déjà à l'intérieur.",
    "La lumière s'éteindra bientôt...",
    "Je sais ce que tu as fait la nuit dernière.",
    "Tu as entendu ce bruit ? C'est moi.",
    "C'est ton dernier avertissement..."
]

# Fonction pour jouer un son inquiétant
def play_anguishing_sound():
    if random.random() < 0.1:  # 10% de chances de jouer un son
        frequency = random.randint(400, 800)  # Fréquence aléatoire du son
        duration = random.randint(100, 500)   # Durée aléatoire
        winsound.Beep(frequency, duration)

# Fonction pour afficher un message inquiétant dans des endroits divers
def display_anguishing_message():
    global interaction_count
    
    # Message aléatoire
    message = random.choice(messages)

    # Afficher une notification système tous les 5 cycles
    if interaction_count % 5 == 0:
        notification.notify(
            title='ALERTE',
            message=message,
            timeout=5  # Durée de la notification
        )

    # Afficher dans la console moins fréquemment
    if interaction_count % 3 == 0:
        print(f"[ALERTE] {message}")
    
    interaction_count += 1  # Incrémenter l'interaction

# Fonction pour déplacer la souris de manière aléatoire
def move_mouse_randomly():
    screen_width, screen_height = pyautogui.size()
    random_x = random.randint(0, screen_width)
    random_y = random.randint(0, screen_height)
    pyautogui.moveTo(random_x, random_y, duration=0.5)

# Fonction pour localiser et cliquer sur l'icône d'une application (ex. Bloc-notes, Tor, etc.)
def click_on_application_icon(image_path):
    try:
        # Cherche l'icône de l'application dans l'écran à l'aide de l'image fournie
        icon_location = pyautogui.locateOnScreen(image_path, confidence=0.8)  # Utilise la confiance pour être plus tolérant aux variations
        if icon_location:
            icon_center = pyautogui.center(icon_location)
            pyautogui.moveTo(icon_center, duration=random.uniform(1.5, 2.5))  # Déplacement lent
            pyautogui.click()  # Clique sur l'icône
            print(f"[INFO] Clic sur l'icône à {icon_center}")
        else:
            print("[ERROR] Icône non trouvée sur l'écran.")
    except Exception as e:
        print(f"[ERROR] Erreur lors de la localisation de l'icône : {e}")

# Fonction pour ouvrir Bloc-notes et écrire dedans (plus fréquemment)
def open_and_write_in_notepad():
    if random.random() < 0.5:  # 50% de chance d'ouvrir Bloc-notes (augmente la fréquence)
        # Chemin d'image de l'icône de l'application (il faut avoir une capture d'écran de l'icône de l'application)
        image_path = "path_to_notepad_icon.png"  # Remplacer ce chemin par le chemin réel de l'icône de l'application
        click_on_application_icon(image_path)  # Cliquer sur l'icône du Bloc-notes

        # Attendre que l'application se charge
        time.sleep(1)

        # Sélectionner une phrase aléatoire de la liste
        specific_message = random.choice(notepad_messages)

        pyautogui.write(specific_message, interval=0.1)  # Écrire avec un délai entre les caractères
        pyautogui.press('enter')  # Appuyer sur "Entrée" pour commencer une nouvelle ligne

# Fonction pour simuler une erreur système
def simulate_system_error():
    if random.random() < 0.1:  # 10% de chances d'afficher une erreur
        pyautogui.alert("Erreur système : Fichier introuvable", title="Erreur critique", button='OK')

# Fonction pour faire défiler les fenêtres aléatoirement
def random_window_resize():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)
    pyautogui.hotkey('win', 'down')  # Minimiser la fenêtre active
    time.sleep(0.5)
    pyautogui.hotkey('win', 'up')    # Restaurer la fenêtre
    time.sleep(random.uniform(1, 3))  # Attendre avant de continuer

# Fonction pour surveiller la touche secrète de sortie : '²'
def check_exit_command():
    if keyboard.is_pressed('²'):  # Si la touche est pressée
        response = pyautogui.confirm("Es-tu sûr de vouloir arrêter le programme ?")  # Demande de confirmation
        if response == 'OK':  # Si l'utilisateur confirme, on arrête
            pyautogui.alert("Le programme est maintenant arrêté...")
            print("Le programme est maintenant arrêté.")  # Affiche dans la console
            exit()  # Arrête le programme
        else:  # Si l'utilisateur annule
            pyautogui.alert("Le processus continue...")  # Message d'alerte
            time.sleep(1)  # Pause avant de revenir à l'action normale

# Fonction pour simuler un "bug" sur une fenêtre
def simulate_window_bug():
    if random.random() < 0.1:  # 10% de chance d'apparition de bug
        pyautogui.hotkey('alt', 'tab')  # Changer de fenêtre
        time.sleep(0.5)
        pyautogui.hotkey('win', 'left')  # Réduire la taille de la fenêtre
        time.sleep(0.5)
        pyautogui.hotkey('win', 'right')  # Étendre la fenêtre à nouveau

# Boucle principale pour simuler des actions
while True:
    # Vérifie si l'utilisateur appuie sur la touche '²'
    check_exit_command()

    # Effectuer une action aléatoire (mouvement de souris, ouvrir bloc-notes, erreurs système, etc.)
    action = random.choice([move_mouse_randomly, open_and_write_in_notepad, simulate_system_error, random_window_resize, simulate_window_bug])
    action()

    # Afficher un message angoissant
    display_anguishing_message()

    # Jouer un son effrayant de temps en temps (réduit à 10% de chance)
    play_anguishing_sound()

    # Attendre avant de recommencer une autre action
    time.sleep(random.randint(3, 7))  # Attente aléatoire entre les actions