from turtle import *
def clear():
 reset()
 delay(0)
 speed(0)
#
def ligne(carresParRangee, tailleCarre):
    pencolor(0.4, 0.4, 0.4)
    pensize(2)
    pd()
    fd(2*carresParRangee*tailleCarre)

def carre(tailleCarre):
    pensize(tailleCarre) 
    pd()
    fd(tailleCarre)
    pu()

def espace(tailleCarre):
    pu()
    fd(tailleCarre)
    pd()

def repetitionCarre(carresParRangee, tailleCarre):
    for j in range(carresParRangee):
        espace(tailleCarre)
        pencolor(0,0,0)
        carre(tailleCarre)

def position (xInitial,yInitial):
    #la position (x,y) initial a été choisie arbitrairement 
    #pour qu'elle corresponde au model énoncé
    pu()
    goto(xInitial,yInitial)
    pd()

def illusion( nbRangees, carresParRangee, tailleCarre): 

    #pour changer le premier espace blanc dans chaque rangée  
    #je declare une variable unique = à la tailleCarre pour
    #facilement modifier l'appel de la fonction
    valeurVariable = tailleCarre

    #pour simplifier les calculs de (x,y)initiale
    xInitial=-(tailleCarre*carresParRangee)
    yInitial=(tailleCarre*carresParRangee)-(nbRangees*carresParRangee)

    for i in range(nbRangees):
        #la fonction pour tracer un rangée
        def rangees(carresParRangee, tailleCarre,valeurVariable) :
            calculRedondant= yInitial-(i*tailleCarre)
            #positionne la ligne
            position(xInitial,calculRedondant + tailleCarre)
            #trace la ligne
            ligne(carresParRangee, tailleCarre)
            #positionne les carrés
            position(xInitial-tailleCarre,calculRedondant+(tailleCarre/2))
            #avance à une distance donnée 
            espace(valeurVariable)
            #une boucle pour tracer les carrés
            repetitionCarre(carresParRangee, tailleCarre)
        #les rangées impairs
        if (i + 1) % 2 != 0 :
            rangees(carresParRangee, tailleCarre,valeurVariable/2)
        #les rangées pairs et non-multiple de 4      
        elif (i+1)%2 != (i+1)%4 :
            rangees(carresParRangee, tailleCarre, 3*valeurVariable/4)
        #les autres rangées pairs  
        else :
            rangees(carresParRangee, tailleCarre,valeurVariable/4)



    #la dernière ligne
    position(xInitial,yInitial-((i+1)*tailleCarre)+ tailleCarre)
    ligne(carresParRangee,tailleCarre)

    #le retour à la position initiale
    position(xInitial,yInitial-((i-i)*tailleCarre)+ tailleCarre)
    
illusion(8,5,25)
