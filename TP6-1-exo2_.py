print("*"*80)
print("*"*30,"rechercher chaine","*"*30)
print("*"*80)
texte = "Binaire est un blog de vulgarisation sur l’informatique, indépendant, tenu par des académiques, qui parle aussi bien de la technologie que de la science, d’enseignement, de questions industrielles, d’algorithmes rigolos, d’algorithmes pas rigolos, de gentilles data, de méchants bugs, bref, de tous les sujets en lien avec le monde numérique et data qui nous entoure."
p = texte.find("olo")
#p = Rechercher(texte, "olo")
print("\nla position de la première occurence du mot olo est : ",p)
#texte = Remplacer(texte, "data", "donnée")
texte = texte.replace("data","donnée")
#

print("\n\n","*"*80)
print("*"*24,"remplacer toute les occurrences","*"*24)
print("*"*80,"\n")
print(texte)
print("\n","*"*80)