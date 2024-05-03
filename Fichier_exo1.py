NomsEmployes=["Mahmoud Gendouz", "Abdelhamid Zouba","Khadidja Latreche","Amina Mezioud"]
Salaires=[80000,100000,150000]
#stocker les noms et salaires dans un fichier, séparé par "," et 
#forment une ligne séparé:
with open("employes.csv", "w") as fichier:
    for nom, salaire in zip(NomsEmployes, Salaires):
        fichier.write(f"{nom},{salaire}\n")
#lire le fichier et afficher les valeurs qu'il contient
with open("employes.csv","r") as fichier:
    contenu = fichier.readlines()
    for ln in contenu:
        print(ln.strip())
fichier.close()