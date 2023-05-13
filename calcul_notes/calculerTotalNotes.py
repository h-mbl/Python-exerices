# La fonction decouperEnLignes prend un texte en paramètre
# et retourne un tableau contenant les lignes de ce texte
def decouperEnLignes(contenu):
    lignes = contenu.split('\n')
    if lignes[-1] == '':
        lignes.pop()
    return lignes

# La fonction decouperCSV prend un texte représentant le contenu
# d'un fichier CSV en paramètre et retourne une matrice contenant
# les données du fichier CSV
def decouperCSV(contenu):
    lignes = decouperEnLignes(contenu)
    
    matrice = []
    for ligne in lignes:
        matrice.append(ligne.split(','))
    
    return matrice

# La fonction lireCSV prend en paramètre un texte (un nom de fichier CSV)
# et elle retourne une matrice représentant le contenu de ce fichier CSV
def lireCSV(fichier):
    contenu = readFile(fichier)
    return decouperCSV(contenu)

# La procédure ecrireCSV prend deux paramètres. Le premier paramètre est
# un texte (nom du fichier) et le deuxième est une matrice (un tableau)
# à écrire dans le fichier en CSV)
def ecrireCSV(fichier, matrice):        
    rangeesTexte = list(map(','.join, matrice))
    contenu = '\n'.join(rangeesTexte)
    writeFile(fichier, contenu)
    
# La fonction somme prend un tableau de nombres et retourne
# la somme des nombres dans ce tableau
def somme(nombres):
    total = 0
    for n in nombres:
        total += n
    return total
    
# La fonction rangee2Etudiant prend un tableau représentant un étudiant
# dans un fichier CSV et retourne un struct avec les champs
# prenom, nom, notes et total représentant cet étudiant
def rangee2Etudiant(rangee):
    notes = list(map(int, rangee[2:]))
    return struct(nom=rangee[0],
                  prenom=rangee[1],
                  notes=notes,
                  total=somme(notes))

# La fonction etudiant2RangeeAvecTotal un struct représentant un étudiant
# en paramètre et retourne un tableau contenant le nom, le prenom
# et total des notes de l'étudiant
def etudiant2RangeeAvecTotal(etudiant):
    return [etudiant.nom, etudiant.prenom, str(etudiant.total)]
    
# La procédure calculerTotal prend en paramètres le nom d'un fichier CSV de
# notes d'étudiants et calcule le total de chaque étudiant. Le total
# est écrit dans un fichier dont le nom est le deuxième paramètre de la
# fonction
def calculerTotal(fichierNotes, fichierTotal):
    matrice = lireCSV(fichierNotes)
    etudiants = list(map(rangee2Etudiant, matrice))
    matriceAvecTotal = list(map(etudiant2RangeeAvecTotal, etudiants))
    ecrireCSV(fichierTotal, matriceAvecTotal)
    
calculerTotal("notes.csv", "total.csv")
    
    
    
    
    
    