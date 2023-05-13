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

#la procédure ecrireTXT,ecrit la facture avec 40 caractères maximum par ligne
#et tronque le nom de commande superieur à 15 caractères
#le premier parametre est le lien vers le fichier facture.txt
#le deuxieme parametre est la variable resultatCommande qui combine la fonctio
#n qui lit le fichier CSV de commande et
#nomme tous les elements du fichier et retourne un enregistrement du fichier
#le troisieme parametre est la variable resultatInventaire qui s'execute comme
#la variable resultatCommande mais pour 
#le fichier CSV de fichier.

def ecrireTXT(fichier,matrice2Commande,matrice2Inventaire):
   # breakpoint()
    prix=0
    matriceFacture=[]
    for i in range (len(matrice2Commande)):
        for j in range(len(matrice2Inventaire)):
            if matrice2Commande[i].nomDansCommande == \
               matrice2Inventaire[j].nomDansInventaire:
                #
                rangeesLigne = str(matrice2Commande[i].quantiteDansCommande)\
                       + " X " + matrice2Commande[i].nomDansCommande + "." + \
                      str(((matrice2Inventaire[j].prixDansInventaire/100)*\
                           matrice2Commande[i].quantiteDansCommande)) + "$"
                #
                if len(rangeesLigne)< 40 :
                    if len(matrice2Commande[i].nomDansCommande) <15:
                        #
                        matriceFacture.append(str(matrice2Commande[i].\
       quantiteDansCommande) + " X " + matrice2Commande[i].nomDansCommande + \
( "."*(40-len(rangeesLigne)+1))+ str((matrice2Inventaire[j].prixDansInventaire\
                    *matrice2Commande[i].quantiteDansCommande)//100 )+ "," + \
                                str((matrice2Inventaire[j].prixDansInventaire\
                       *matrice2Commande[i].quantiteDansCommande)%100 ) + "$")
                        #
                    else:
                        matriceFacture.append(str(matrice2Commande[i].\
  quantiteDansCommande) + " X " + matrice2Commande[i].nomDansCommande[:15] + \
  ( "."*(40-len(rangeesLigne)+1+ len( matrice2Commande[i].nomDansCommande[15:]\
   )))+str((matrice2Inventaire[j].prixDansInventaire *matrice2Commande[i].\
             quantiteDansCommande)//100 )+ "," + str((matrice2Inventaire[j].\
      prixDansInventaire*matrice2Commande[i].quantiteDansCommande)%100 )  +"$")
                        
                    prix += matrice2Inventaire[j].\
                    prixDansInventaire*matrice2Commande[i].quantiteDansCommande
                    #
    totalPrix = "TOTAL" + ("."*(40-len("TOTAL$")-len(str(prix/100))))\
    + str(prix//100)+","+str(prix%100)+"$"
    
    matriceFacture.append(totalPrix)
    return matriceFacture
def testTXT(fichier,matriceFacture):
    contenu = '\n'.join(matriceFacture)
    writeFile(fichier,contenu)  
    
#la procedure rangee2Inventaire transforme une liste en enregistrement
#et donne à chaque élément un nom.
#
#
#
def rangee2Inventaire(rangeeInventaire):
    enr2Inventaire = struct(nomDansInventaire=rangeeInventaire[0],\
                          prixDansInventaire=int(rangeeInventaire[1]),\
                            quantiteDansInventaire= int(rangeeInventaire[2]))
    return enr2Inventaire
    

##mets à jour inventaire.csv en modifiant la quantite
#en fait le probleme qui reste a ce point est que struct() ne peut pas 
#se convertir 
#directement en csv car ce n'est pas un tableau donc il faut chercher 
#un moyen de changer 
# un enregistrement en tab pour que cela puisse s'ecrire en csv 
#attention,a cet etape tous les dossiers deviennent sensible et que cela peut 
#supprimer tous le contenu d'un fichier

def rangee2InventaireAvecReduction(enr2Inventaire,enr2Commande):
    #breakpoint()
    matricenveauInventaire=[]
    for i in enr2Inventaire:
        for j in enr2Commande:
            nveauInventaire=[]
            if i.nomDansInventaire == j.nomDansCommande:
                if j.quantiteDansCommande <= i.quantiteDansInventaire :
                    nvQuantite= i.quantiteDansInventaire - \
                                                        j.quantiteDansCommande
                    i.quantiteDansInventaire = nvQuantite
                    nveauInventaire.append(i)
                else: 
                    return \
                "Commande refusée pour cause d'inventaire insuffisant"
            else: 
                nveauInventaire.append(i)
        matricenveauInventaire.append(nveauInventaire)
        
    #maticeaa = matricenvInventaire
    #ensuite ecris le CSV
    def testCSV(matricenveauInventaire):
        list2Inventaire =[]
        for i in range(len(matricenveauInventaire)): 
            list2Inventaire.append([matricenveauInventaire[i][0].\
  nomDansInventaire , str(int((matricenveauInventaire[i][0].\
  prixDansInventaire))), str(matricenveauInventaire[i][0].\
                             quantiteDansInventaire) ])
        matrice1 = ecrireCSV("inventaire.csv",list2Inventaire)
    testCSV(matricenveauInventaire)
    return matricenveauInventaire
  
    
#la procedure rangee2Inventaire transforme une liste en enregistrement
#et donne à chaque élément un nom. 
#
#
#          
def rangee2Commande(rangeeCommande):
    enr2Commande = struct(nomDansCommande=rangeeCommande[0],\
                          quantiteDansCommande= int (rangeeCommande[1]))

    return enr2Commande

#    
def facturer(inventaire,commande1, facture): 
    matriceInventaire = lireCSV(inventaire)
    resultatInventaire = list(map(rangee2Inventaire, matriceInventaire))
    matriceCommande = lireCSV(commande1)
    resultatCommande= list(map(rangee2Commande,matriceCommande))
    rangee2InventaireAvecReduction(resultatInventaire,  resultatCommande)  
    ecrireTXT(facture,resultatCommande,resultatInventaire)  
    testTXT(facture,ecrireTXT(facture,resultatCommande,resultatInventaire) )
    
   #breakpoint()

facturer("inventaire.csv", "commande1.csv","facture.txt")
def testFacturer():
    #je cree de fonctions de tous les cas 
    #lorsque il n'a rien dans l'inventaire et rien dans la commande
    
    assert  ecrireTXT("facture.txt",[],[])  ==\
    ['TOTAL...............................0,0$']
    
    #lorsqu'il y a des choses dans l'inventaire mais rien dans la commande 
   
    assert  ecrireTXT("facture.txt",[],(( struct(nomDansInventaire= "banane",\
        prixDansInventaire=10,quantiteDansInventaire= 20),\
         struct(nomDansInventaire= "lait", prixDansInventaire=899,\
    quantiteDansInventaire= 1),struct(nomDansInventaire= "pain",\
          prixDansInventaire=45,quantiteDansInventaire= 10))))  == \
                      ['TOTAL...............................0,0$']
   
    #lorsqu'il y a des choses dans la commande mais rien dans l'inventaire 
    assert  ecrireTXT("facture.txt",(struct(nomDansCommande="banane",\
                          quantiteDansCommande= 21),\
                                      struct(nomDansCommande="pain",\
                          quantiteDansCommande= 15)),[])  == \
                           ['TOTAL...............................0,0$']
    #lorsqu'il y a des surplus dans la commade 
    assert rangee2InventaireAvecReduction(( struct(nomDansInventaire= "banane"\
                          ,prixDansInventaire=10,quantiteDansInventaire= 20),\
                                           struct(nomDansInventaire= "lait",\
                          prixDansInventaire=899,quantiteDansInventaire= 1),\
                                           struct(nomDansInventaire= "pain",\
                          prixDansInventaire=45,quantiteDansInventaire= 10)),\
                                          (struct(nomDansCommande="banane",\
                          quantiteDansCommande= 21),\
                                           struct(nomDansCommande="pain",\
                          quantiteDansCommande= 15)))==\
    "Commande refusée pour cause d'inventaire insuffisant"
      #une commande normal(l'exempple du professeur) 
      #lorsqu'il y a un nom trop long 
    assert ecrireTXT("facture.txt",(struct(nomDansCommande='biscuits', \
                                           quantiteDansCommande=2),\
                                     struct(nomDansCommande='banane',\
                                            quantiteDansCommande=1),\
                                     struct(nomDansCommande='lait',\
                                            quantiteDansCommande=2),\
       struct(nomDansCommande='gateau au chocolat', quantiteDansCommande=1)),\
  (struct(nomDansInventaire='banane', prixDansInventaire=89,\
 quantiteDansInventaire=200), struct(nomDansInventaire='lait',\
 prixDansInventaire=899, quantiteDansInventaire=45),\
  struct(nomDansInventaire='pain', prixDansInventaire=450,\
   quantiteDansInventaire=12),struct(nomDansInventaire='biscuits',\
    prixDansInventaire=399, quantiteDansInventaire=60),\
  struct(nomDansInventaire='fromage', prixDansInventaire=650,\
  quantiteDansInventaire=34), struct(nomDansInventaire='gateau au chocolat',\
                    prixDansInventaire=1299, quantiteDansInventaire=4))) == \
               ['2 X biscuits.......................7,98$',\
                '1 X banane.........................0,89$',\
                '2 X lait..........................17,98$', \
                '1 X gateau au choco...............12,99$', \
                'TOTAL.............................39,84$']
    #modification de l'inventaire
    assert rangee2InventaireAvecReduction(\
  (struct(nomDansInventaire='banane', prixDansInventaire=89,\
 quantiteDansInventaire=200), struct(nomDansInventaire='lait',\
 prixDansInventaire=899, quantiteDansInventaire=45),\
  struct(nomDansInventaire='pain', prixDansInventaire=450,\
   quantiteDansInventaire=12),struct(nomDansInventaire='biscuits',\
    prixDansInventaire=399, quantiteDansInventaire=60),\
  struct(nomDansInventaire='fromage', prixDansInventaire=650,\
  quantiteDansInventaire=34), struct(nomDansInventaire='gateau au chocolat',\
                     prixDansInventaire=1299, quantiteDansInventaire=4)),
  (struct(nomDansCommande='biscuits', quantiteDansCommande=2),\
     struct(nomDansCommande='banane', quantiteDansCommande=1),\
  struct(nomDansCommande='lait',  quantiteDansCommande=2),\
   struct(nomDansCommande='gateau au chocolat', quantiteDansCommande=1))) ==\
    [[struct(nomDansInventaire='banane', prixDansInventaire=89,\
             quantiteDansInventaire=199)], [struct(nomDansInventaire='lait',\
     prixDansInventaire=899, quantiteDansInventaire=43)], \
     [struct(nomDansInventaire='pain', prixDansInventaire=450,\
 quantiteDansInventaire=12)], [struct(nomDansInventaire='biscuits', \
  prixDansInventaire=399, quantiteDansInventaire=58)],\
     [struct(nomDansInventaire='fromage', prixDansInventaire=650,\
  quantiteDansInventaire=34)], [struct(nomDansInventaire='gateau au chocolat',\
                        prixDansInventaire=1299, quantiteDansInventaire=3)]]

    
 
  
testFacturer()