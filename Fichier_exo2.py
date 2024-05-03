from random import *
randint(0,20)
l=["e","e","r"]
choice(l)
#Partie 1 generation d'un ficier notes.txt
#Etape 1
#Prénom Nom note1 note2 note3
liste_nom=["CHIKH TOUHAMI","CHIOUB","CHOUDER","DAACHI","DAMECH","DAOUDI","DECHIR","DERRAR","DERRI","DINAR"]
liste_prenom=["MALEK","ABDERRAHMANE","MANAR","AYMENE","ILYES","BARAA MANEL","RADIA","HALIMA","MOHAMED AIMEN","OUDAY"]
#Etape 2
with open("notes.txt","w") as fichier:
    fichier.write("nom\tprenom\tnote1\tnote2\tnote3\n")
    for i in range(len(liste_nom)):
        nom=choice(liste_nom)
        prenom=choice(liste_prenom)
        note1=randint(0, 40) /2
        note2=randint(0, 40) /2
        note3=randint(0, 40) /2
        fichier.writelines(f"{nom}\t{prenom}\t{str(note1)}\t{str(note2)}\t{str(note3)}\n")
fichier.close()
with open("notes.txt","r") as fichier:
    contenu=fichier.readlines()
    for ln in contenu:
        print(ln.strip()+"\n")
# ÉTAPE 1: OUVERTURE DES FICHIERS SOURCE ET CIBLE
print('*'*80)
print("\n création fichier moyenne: \n")
with open("notes.txt", "r") as notes_file, open("moyennes.txt", "w") as moyennes_file:
    # Ignorer la première ligne (en-tête)
    liste_notes=notes_file.readlines()
    liste_notes.pop(0)
    # ÉTAPE 2: CRÉATION DU FICHIER moyennes.txt
    # Écrire l'en-tête
    moyennes_file.writelines("Prénom\tNom\tMoyenne\n")

    # Parcourir chaque ligne du fichier notes.txt
    for line in liste_notes:
        # Supprimer le caractère de fin de ligne
        line = line.strip("\n")
        # Diviser la ligne en une liste de données
        data = line.split("\t")
        # Extraire les données nécessaires
        prenom = data[0]
        nom = data[1]
        notes = [float(note) for note in data[2:]]  # Convertir les notes en float
        # Calculer la moyenne
        moyenne = sum(notes) / len(notes)
        # Convertir la moyenne en une chaîne avec deux décimales
        moyenne_str = '{0:.2f}'.format(moyenne)
        # Écrire la ligne dans le fichier moyennes.txt
        moyennes_file.write(f"{prenom}\t{nom}\t{moyenne_str}\n")

print("Le fichier moyennes.txt a été créé avec succès.")
        