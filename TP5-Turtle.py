from turtle import *
def marche(h):
    left(90)
    for i in range(4):
        forward(h)
        right(90)
        forward(h)
def escalier(n, h):
    for k in range(n):
        marche(h)
speed(5) # parametrage de la vitesse de 1 lent à 10 rapide

# 0 étant la vitesse la plus rapide
shape("turtle") # choix de la forme de la tortue
pencolor("red") # choix de la couleur du crayon
pensize(4) # épaisseur du crayon
up() # lever le crayon
goto(-150,-150) # aller à la position (-150,-150)
setheading( 0) # orientation de la tortue vers l'Est /
# 90 Nord / 180 Ouest / 270 Sud

down() # poser le crayon
escalier(5, 50)
exitonclick() #