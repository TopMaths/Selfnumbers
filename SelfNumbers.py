# fichier SelfNumbers.py fourni par TopMaths, sans aucune garantie
# Vous pouvez consulter la vidéo Autonombres sur ma chaine Youtube
# S'il y a des erreurs, vous pouvez me le signaler dans les commentaires de la vidéo
# N'hésitez pas à me faire de la pub !

def SC(n,b):
    """somme des chiffres en base b de n"""
    S=0
    while n>0:
        S+=(n%b)
        n//=b
    return S
    
def S(n,b):
    """digit addition de n en base b"""
    return n+SC(n,b)

def SCR(n,b):
    """somme répétées des chiffres de n en base b""" 
    while n>=b:
        n=SC(n,b)
    return n

def nbchiffres(n,b):
    """détermine le nombre de chiffres de n en base b"""
    if n==0: return 1
    from math import log,floor
    return floor(1+log(n,b))

def TestKaprekar(n,b):
    """test de Kaprekar : n est-il un autonombre~?

exemples : 

>>> TestKaprekar(32,10)
False

32 n'est pas un autonombre en base 10

>>> TestKaprekar(35,7)
True

35 est un autonombre en base 7
 """    
    if b%2==1: # th de Joshi
        return n%2==1
    # maintenant la base b est paire 
    dec=SC(n,b)
    if dec%2==1:dec=(dec+b-1)
    g=n-dec//2 # générateur potentiel
    for i in range(1+nbchiffres(n,b)):
        if S(g,b)==n: return False
        g-=b-1
    return True


def sequence(n,b,p):
    """suite des p premiers termes de la suite de Kaprekar de n en base b"""
    Seq=[n]
    for i in  range(p):
        n=S(n,b)
        Seq.append(n)
    return Seq

            
def classemod(n,b):
    """calcule la suite de Kaprekar de n modulo b-1"""
    n=n%(b-1)
    L=[n]
    for i in range(b):
        n=(2*n)%(b-1)
        L.append(n)
    return L

def jointure(n,m,b):
    """permet de déterminer si la jonction entre n et m existe en base b"""
    n,m=min(n,m), max(n,m)
    if n==0 and b!=0: return False
    N=set(classemod(n,b))
    M=set(classemod(m,b))
    return N.intersection(M)!=set()

def jonction(n,m,b):
    """calcule la jonction entre n et m en base b : c'est le premier nombre commun dans les suites de Kaprékar de n et de m. Renvoie -1 si cette joinction n'existe pas.

exemples : 
>>> jonction(1,13,10)
620

>>> jonction(1,9,10)
-1

"""
    if not jointure(n,m,b): return -1
    while n!=m:
        if n<m:
            n=S(n,b)
        else:
            m=S(m,b)
    return n


def jonctionManuelle(n,m,b):
    """calcule la jonction entre n et m en base b : c'est le premier nombre commun dans les suites de Kaprékar de n et de m. Le programme boucle indéfiniment s'il n'y a pas de jonction !"""
    while n!=m:
        if n<m:
            n=S(n,b)
        else:
            m=S(m,b)
    return n


def classes(b,max=None):
    """Déterminer les classes de nombres de 1 à max : deux nombres sont dans la même classe si ces deux nombres se rejoignent

par défaut max vaut b

exemple :
>>> classes(10)
[[10, 1, 2, 4, 5, 7, 8], [9], [6, 3], [0]]


Un nombre d'une classe rejoint tout nombre de la même classe par les suites de Kaprékar mais ne rejoint aucun nombre d'une autre classe 
 """
    if max==None: max=b
    L=[]
    NF=list(range(max+1))
    while NF:
        F=[]
        x=NF.pop()
        L.append([x])
        for i in NF:
            if jointure(x,i,b):
                L[-1].append(i)
                F.append(i)
        for y in F:
            NF.remove(y)
    return L


