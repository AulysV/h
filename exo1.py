from turtle import *

forward(100)
left(60)
forward(100)
right(120)
forward(100)
left(60)
forward(100)

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



exitonclick()