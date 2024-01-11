from turtle import *


a = 0  
def courbe_koch(l,n):

    global a

    if n==0:
        forward(l)
        a += 1
    else :
        courbe_koch(l/3, n-1)
        left(60)
        courbe_koch(l/3, n-1)
        right(120)
        courbe_koch(l/3, n-1)
        left(60)
        courbe_koch(l/3, n-1)
        
        

#Creation fenêtre
hauteur=500
largeur=900
setup(largeur,hauteur)

#Réglage de la tortue
speed(0) #Vitesse (0 -> vitesse max)
hideturtle() #Cacher la tortue


penup() #Lever le stylo
#Placement de la tortue en bas à gauche de la fenêtre
setpos(-largeur/2,-hauteur/2+20)

pendown() #Baisser le stylo

x = 5

#Tracer la courbe
courbe_koch(largeur,x)

print(a)
print(a*largeur/(3**x))

exitonclick()
