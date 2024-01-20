def init_p(t):
    return [[False] * t for gloubiboulga in range(t)]

def gagne(p):
    return all(all(c for c in l) for l in p)

def voisines(i, j, t):
    vc = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [(x, y) for x, y in vc if 0 <= x < t and 0 <= y < t]

def inverse(p, i, j):
    t = len(p)
    p[i][j] = not p[i][j]
    for x, y in voisines(i, j, t):
        p[x][y] = not p[x][y]

# Un jouli tableau qui a pris pas mal de temps à être réalisé (ne marche qu'avec une police à largeur fixe)
# Merci à Gnome et au magnifique « ASCII draw » (https://github.com/Nokse22/ascii-draw)

def affiche_p(p):
    t = len(p)
    print("    ", end="")
    for i in range(t):
        print(f" {i:2}", end="")
    print("\n    ┏" + "━━━" * t + "┓")
    for i, l in enumerate(p):
        print(f"{i:2}  ┃", end="")
        for j, c in enumerate(l):
            if c:
                print(' ●', end=' ')
            else:
                print(' ◯', end=' ')
            if j == t - 1:
                print("┃")
            else:
                print("", end="")
    print("    ┗" + "━━━" * t + "┛")


# Bout de code qui fait fonctionner le jeu :

t = int(input("Quelle taille de plateau ? "))
p = init_p(t)

while not gagne(p):
    affiche_p(p)
    i, j = int(input("À quelle ligne souhaitez-vous jouer ? ")), int(input("Et à quelle colonne ? "))
    inverse(p, i, j)

print("GG !! WP")
    

# Version tkinter pour s'amuser :

import tkinter as tk
from tkinter import ttk, messagebox

def toggle_cell(i, j):
    p[i][j] = not p[i][j]
    for x, y in voisines(i, j, t):
        p[x][y] = not p[x][y]
    update_board()

def update_board():
    for i in range(t):
        for j in range(t):
            if p[i][j]:
                buttons[i][j].config(style='On.TButton')
            else:
                buttons[i][j].config(style='Off.TButton')

    if gagne(p):
        messagebox.showinfo("Partie terminée", "GG WP !!")
        root.quit()
    

t = int(input("Entrez la taille du plateau (version tkinter) : "))
p = init_p(t)

root = tk.Tk()
root.title("Othello version wish")

style = ttk.Style()

style.configure('Off.TButton', background='#424242', borderwidth=2, relief='flat', width=2, height=2)
style.map('Off.TButton', background=[('active', 'gray')])

style.configure('On.TButton', background='black', borderwidth=2, relief='flat', width=2, height=2)
style.map('On.TButton', background=[('active', 'darkgray')])

buttons = [[ttk.Button(root, style='Off.TButton', command=lambda i=i, j=j: toggle_cell(i, j)) for j in range(t)] for i in range(t)]

for i in range(t):
    for j in range(t):
        buttons[i][j].grid(row=i, column=j, padx=1, pady=1)

update_board()
root.mainloop()





