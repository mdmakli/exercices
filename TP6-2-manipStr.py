"""Q.1/Écrire une procédure nommée afficher permettant d’afficher tous les éléments   d’uneliste quelconque (nommée liste), ainsi que la taille de la liste."""
""" Algorithmique:
procédure afficher(e : liste chaine):
    var: i,n : entier;
    Début:
        n = longueur(e)
        pour i de 0, n-1 faire:
            écrire(e[i])
procédure afficher_2(e : liste de chaine)
   var: element : chaine;
   Début:
        pour element dans e faire:
         écrire(element)
"""
def afficher(e):
    for element in e:
        print(element)
    print(len(e),"\n\n")





""" 
def afficher(l):
    for i in l:
        print(i)
    print("La taille de la liste = ", len(l))
    
"""
"""Q.2/Créer une liste nommée listeMots contenant les valeurs suivantes : « Algorithme », « Programme ». Appeler la procédure afficher pour listeMots. Tester."""
listeMots = ["Algorithme", "Programme"]
afficher(listeMots)


"""Q.3/Ajouter en 1re position de listeMots la chaîne « Informatique2 », puis remplacer le mot « Programme » (qui se trouve toujours en fin de liste) par « Python » dans listeMots.Appeler de nouveau la procédure afficher pour listeMots. Tester."""
listeMots.insert(0, "Informatique2")
listeMots.append("C++")

afficher(listeMots)



"""listeMots.pop()
listeMots.append("Python")"""
listeMots[-1] = "Python"
afficher(listeMots)


"""Q.4/Trier listeMots par ordre alphabétique. Appeler de nouveau la procédure afficher pour listeMots. Tester."""
listeMots.sort()
"""Q.5/Chercher la position p de la première occurrence du mot « Informatique2 » dans listeMots. Afficher p. Tester."""
p = listeMots.index("Informatique2")
print(p)
"""Q.6/Créer une liste nommée listeNombres avec quelques valeurs numériques au choix. Appeler la procédure afficher pour listeNombres. Est-ce possible en algorithmique ? Tester avec Python."""
listeNombres= [251,512,44,86,910]
afficher(listeNombres)