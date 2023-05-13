# Hervé Ngisse
# 15 Octobre 2022

# La fonction nombreDizaineFrancais6 prend en parametre un nombre
# entier entre 1 et 6 et retourne un texte qui est le mot Francais
# pour ce nombre de nombreDizaineFrancais6, en lettres minuscules.

def nombreDizaineFrancais6(n):
    if n == 1:
        return "dix"
    elif n == 2:
        return "vingt"
    elif n == 3:
        return "trente"
    elif n == 4:
        return "quarante"
    elif n == 5:
        return "cinquante"
    else:
        return "soixante"

# La fonction nombreFrancais9 prend en parametre un nombre entier
# entre 1 et 9 et retourne un texte qui est le mot Francais pour ce
# nombre, en lettres minuscules.

def nombreFrancais9(n):
    if n == 1:
        return "un"
    elif n == 2:
        return "deux"
    elif n == 3:
        return "trois"
    elif n == 4:
        return "quatre"
    elif n == 5:
        return "cinq"
    elif n == 6:
        return "six"
    elif n == 7:
        return "sept"
    elif n == 8:
        return "huit"
    else:
        return "neuf"

# La fonction nombreFrancais19 prend en parametre un nombre entier
# entre 1 et 19 et retourne un texte qui correspond a ce nombre en
# Francais, en lettres minuscules.

def nombreFrancais19(n):
    if n <= 9:
        return nombreFrancais9(n)
    elif n == 10:
        return nombreDizaineFrancais6(1)
    elif n == 11:
        return "onze"
    elif n == 12:
        return "douze"
    elif n == 13:
        return "treize"
    elif n == 14:
        return "quatorze"
    elif n == 15:
        return "quinze"
    elif n == 16:
        return "seize"
    else:
        return nombreDizaineFrancais6(1) + "-" + nombreFrancais9(n - 10)

# La fonction nombreFrancais99 prend un parametre qui est un nombre
# entier entre 1 et 99, et retourne un texte qui correspond a ce
# nombre en Francais, en lettres minuscules.

def nombreFrancais99(n):

    #les variables locals :
    modulo= n%10
    divEntiere= n//10
    quatrevingt = nombreFrancais9(4) + "-" + nombreDizaineFrancais6(2)
    #
    #
    if n <20 :
        return nombreFrancais19(n)
    elif divEntiere < 7 : 
        if modulo== 0 :
            return nombreDizaineFrancais6(n/10)
        elif modulo==1:
            return nombreDizaineFrancais6(divEntiere) +"-et-" + nombreFrancais9(1)
        else : 
            return nombreDizaineFrancais6(divEntiere) + "-" + nombreFrancais9(modulo)
    elif divEntiere == 7 :
        if modulo == 1 :
            return nombreDizaineFrancais6(6) + "-et-" + nombreFrancais19 (11)
        else : 
            return nombreDizaineFrancais6(6) + "-" + nombreFrancais19 (n-60)
    elif divEntiere == 8:
        if modulo == 0  :
            return quatrevingt + "s" 
        else: 
            return quatrevingt +"-" + nombreFrancais9(modulo)
    else :
        return quatrevingt + "-" + nombreFrancais19(n-80)
        
# La fonction nombreFrancais prend un parametre qui est un nombre
# entier entre 1 et 999, et retourne un texte qui correspond a ce
# nombre en Francais, en lettres minuscules.
def nombreFrancais(n):

    #les variables locals :
    modulo= n%100
    divEntiere= n//100
    #
    #
    if n<100: 
        return nombreFrancais99(n)
    elif divEntiere==1 :
        if modulo == 0: 
            return "cent" 
        elif modulo == 1 :
            return nombreFrancais(100) + "-et-" + nombreFrancais9(1)
        else: 
            return  nombreFrancais(100) + "-" + nombreFrancais99(n-100)
    else :
        if modulo == 0 : 
            return nombreFrancais9(n/100) + "-" + nombreFrancais(100) + "s"
        elif modulo == 1 :
            return nombreFrancais9(divEntiere) + "-" + nombreFrancais(100) + "-et-" + nombreFrancais9(1)
        else: 
            return nombreFrancais9(n/100) + "-" + nombreFrancais(100) + "-" + nombreFrancais99(n-divEntiere*100)

# La procedure testNombreFrancais contient les tests unitaires
# de la fonction nombreFrancais.

def testNombreFrancais():
    assert nombreFrancais (17) == "dix-sept"    #1
    assert nombreFrancais(31) == "trente-et-un" #2
    assert nombreFrancais(32) == "trente-deux"  #3
    assert nombreFrancais(50) == "cinquante"    #4
    assert nombreFrancais(70) == "soixante-dix" #5
    assert nombreFrancais(71) == "soixante-et-onze" #6
    assert nombreFrancais(80) == "quatre-vingts"    #7
    assert nombreFrancais(81) == "quatre-vingt-un"  #8
    assert nombreFrancais (90) == "quatre-vingt-dix" #9
    assert nombreFrancais(99) == "quatre-vingt-dix-neuf" #10
    assert nombreFrancais(100) == "cent" #11
    assert nombreFrancais(101) == "cent-et-un"  #12
    assert nombreFrancais(117) == "cent-dix-sept"   #13
    assert nombreFrancais(131) == "cent-trente-et-un" #14
    assert nombreFrancais(132) == "cent-trente-deux"#15
    assert nombreFrancais(150) == "cent-cinquante" #16
    assert nombreFrancais(171) == "cent-soixante-et-onze"   #17
    assert nombreFrancais(170) == "cent-soixante-dix"   #18
    assert nombreFrancais(180) == "cent-quatre-vingts"   #19
    assert nombreFrancais(181) == "cent-quatre-vingt-un"    #20
    assert nombreFrancais(191) == "cent-quatre-vingt-onze"  #21
    assert nombreFrancais(200) == "deux-cents"  #22
    assert nombreFrancais(201) == "deux-cent-et-un" #23
    assert nombreFrancais(900) == "neuf-cents"  #24
    assert nombreFrancais(999) == "neuf-cent-quatre-vingt-dix-neuf" #25

testNombreFrancais() # Executer les tests unitaires