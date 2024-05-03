def fibonnachi(N):
    liste = [ ]
    print(liste)
    liste.append(0)
    liste.append(1)
    print(liste)
    for i in range(2,N):
        liste.append(liste[i-1]+liste[i-2])
    return liste

def Afficher(liste):
    for element in liste:
        print((element))
def fibonnachi_1(N):
    a=0
    b=1
    for i in range(2,N):
        c = a+b
        a = b
        b = c
        print(c)

    print("\n",c)
Number = int(input("enter a number to calculate its sequence of fibonnachi "))
l=fibonnachi(Number)
Afficher(l)
fibonnachi_1(Number)