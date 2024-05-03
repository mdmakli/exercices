def Afficher(lst=[]):#(lst: liste de chaine)
    for elt in lst:
        print(elt)
    print("\nla longueur de la liste = ", len(lst))

def transform(lst=[]):
    lst2=[]
    for i in range(len(lst)):
        lst2.insert(i, str(lst[i]))
    return lst2
lst = ["Algorithme", "Programme"]
Afficher(lst)
"""lst2=transform(lst)
lst2.sort(reverse=True) 
Afficher(lst2)"""
#inserer le mot informatique à la 1ère position
lst.insert(0, "Informatique2")
#remplacer le mot informatique par python
p=lst.index("Informatique2")
print("p = ",p)
lst[p] = "Python"
#trier la liste
lst.sort()
Afficher(lst)
lst2 = [100,250,2]
Afficher(lst2)
