import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Calculatrice")

pad_y = 5  # Espacement vertical entre les boutons
pad_x = 5

# Style général de la fenêtre
root.config(bg="#2e2e2e") 
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# Style général des boutons
default_button_style = {
    "width": 5,
    "height": 2,
    "bg": "#4CAF50",  # Couleur de fond du bouton
    "fg": "#ffffff",  # Couleur du texte
    "font": button_font,
    "relief": "raised",  # Style de bordure (flat, raised, sunken, etc.)
    "bd": 3,  # Largeur de bordure
}

default_button_grid = {"padx": pad_x, "pady": pad_y, "sticky": "nsew"}
equal_button_style = {**default_button_style, "bg": "#f05a2D"}  # Combine le style du bouton égal avec une couleur personnalisée

# Fonction pour ajouter du texte dans le champ de texte
def button_click(value):
    current_text = entry.get()  # Récupère le texte actuel dans le champ de texte
    entry.insert(tk.END, value)  # Ajoute le texte du bouton dans le champ de texte

def supp():
    entry.delete(0, tk.END)


def equal():
    champs = entry.get()
    try:
        result = eval(champs)  # Évalue l'expression mathématique
        entry.delete(0, tk.END)  # Supprime le contenu actuel du champ de texte
        entry.insert(tk.END, str(result))  # Affiche le résultat dans le champ de texte
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erreur")  # En cas d'erreur, affiche "Erreur" dans le champ de texte

def close():
    root.destroy()  # Ferme la fenêtre


# Création du champ de texte (Entry) en haut de la fenêtre
entry = tk.Entry(root, font=("Helvetica", 16), bg="#ffffff", fg="#000000", justify="right")
entry.pack(padx=10, pady=10, fill="x")  # La méthode `pack` permet de placer le champ de texte

# Création du cadre pour organiser les boutons
frame = tk.Frame(root, bg="#2e2e2e")
frame.pack(padx=10, pady=10)

# Ajout des boutons avec une disposition en grille
tk.Button(frame, text="Del", command=lambda: supp(), **default_button_style).grid(row=1, column=1, **default_button_grid)
tk.Button(frame, text="Close", command=lambda: close(), **default_button_style).grid(row=1, column=2, **default_button_grid)
tk.Button(frame, text="0", command=lambda: button_click("0"), **default_button_style).grid(row=5, column=1, columnspan=2, **default_button_grid)
tk.Button(frame, text="1", command=lambda: button_click("1"), **default_button_style).grid(row=4, column=1, **default_button_grid)       
tk.Button(frame, text="2", command=lambda: button_click("2"), **default_button_style).grid(row=4, column=2, **default_button_grid)
tk.Button(frame, text="3", command=lambda: button_click("3"), **default_button_style).grid(row=4, column=3, **default_button_grid)
tk.Button(frame, text="4", command=lambda: button_click("4"), **default_button_style).grid(row=3, column=1, **default_button_grid)
tk.Button(frame, text="5", command=lambda: button_click("5"), **default_button_style).grid(row=3, column=2, **default_button_grid)
tk.Button(frame, text="6", command=lambda: button_click("6"), **default_button_style).grid(row=3, column=3, **default_button_grid)
tk.Button(frame, text="7", command=lambda: button_click("7"), **default_button_style).grid(row=2, column=1, **default_button_grid)
tk.Button(frame, text="8", command=lambda: button_click("8"), **default_button_style).grid(row=2, column=2, **default_button_grid)
tk.Button(frame, text="9", command=lambda: button_click("9"), **default_button_style).grid(row=2, column=3, **default_button_grid)

# Boutons des opérateurs
tk.Button(frame, text="+", command=lambda: button_click("+"), **default_button_style).grid(row=3, column=4, **default_button_grid)
tk.Button(frame, text="-", command=lambda: button_click("-"), **default_button_style).grid(row=2, column=4, **default_button_grid)
tk.Button(frame, text="x", command=lambda: button_click("*"), **default_button_style).grid(row=1, column=4, **default_button_grid)
tk.Button(frame, text="/", command=lambda: button_click("/"), **default_button_style).grid(row=1, column=3, **default_button_grid)
tk.Button(frame, text="=", command=lambda: equal(), **equal_button_style).grid(column=4, row=4, rowspan=2, **default_button_grid)
tk.Button(frame, text=".", command=lambda: button_click("."), **default_button_style).grid(row=5, column=3, **default_button_grid)

root.mainloop()
