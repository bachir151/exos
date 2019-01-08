from math import *

def find_carre_parfait (n):
    liste_carre=[]
    for i in range (1,n):
        for j in range(1,int(sqrt(n))):
            if i==j*j :
                liste_carre.append(i)
    return(liste_carre)


l=find_carre_parfait(9999)
l= [x for x in l if len(str(x)) != 1 and len(str(x)) != 3 and len(str(x)) != 2 ]
print(l)
def sep_carre_pafait(n):
    l = find_carre_parfait(n)
    l = [x for x in l if len(str(x)) != 1 and len(str(x)) != 3 and len(str(x)) != 2 ]
