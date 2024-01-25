# Question 1

plateau = [
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False]
]

# print(plateau[3][1])

i, j = 2, 3

# print(plateau[i-1][j-1])


# Question 2

def init_p(t):
    return [[False] * t for gloubiboulga in range(t)]

# Question 3

def gagne(p):
    return all(all(babar for babar in l) for l in p)

# Question 4

def voisines(i, j, t, x = False): # Le x permet d'ajouter le tuple (i, j) à la liste si voulu.
    return [(x, y) for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i, j) if x == True else False] if 0 <= x < t and 0 <= y < t]

# Question 5

def inverse(p, i, j): # On a besoin d'inverser la case i, j, donc on définit x = True
    for x, y in voisines(i, j, len(p), x = True) : p[x][y] = not p[x][y] 

# Question 6

# Permet d'afficher un plateau assez joli. Source : « ASCII draw » (https://github.com/Nokse22/ascii-draw)

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
                print(' ○', end=' ')
            if j == t - 1:
                print("┃")
            else:
                print("", end="")
    print("    ┗" + "━━━" * t + "┛")


# Bout de code qui fait fonctionner le jeu, le plus simple possible : 

p = init_p(int(input("Quelle taille de plateau ? ")))

while not gagne(p):
    affiche_p(p)
    inverse(p, int(input("À quelle ligne souhaitez-vous jouer ? ")), int(input("Et à quelle colonne ? ")))

affiche_p(p)
print("Bravo 🐵🐒🙊🙉🙈🦧 !!")

