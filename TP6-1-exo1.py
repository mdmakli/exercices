
#Q1 
ch = 'Bienvenue dans le module informatique 2, Algorithme et programmation Python'
#Q2 taille de la chaine ch:
t = len(ch)
print("la taille de la chaine",t)
#Q3 extraction: [1]
c1 = ch[0]
print(c1)
#Q4 extraction: [-1] ou [t]
c2=ch[-1]
print("ch[",-1,"]= ", c2)
c2 = ch[t-1]
print("ch[",t,"]= ", c2)
#Q5 extraction: [1:10] sch1 = souschaine(ch,1,10)
sch1=ch[0:10]
#Q6 extraction: [11:20] sch2 = souschaine(ch, 11, 20)
sch2 = ch[10:20]
sch3 = ch[21:]
print("ch[1,10] = ",sch1,"\nch[11,20] = ",sch2,"\nch[22,fin] = ", sch3)
#sch4 = souschaine(ch,t-10, t-1)
print("sch[t-10,t] = ")
sch4 = ch[t-10:]
print(sch4)
sch5 = ch[-10:]
print(sch5)
print("*"*80) 
chBc = ch.upper()#majuscule
chBc = ch.lower()#minuscule
print(chBc)  

