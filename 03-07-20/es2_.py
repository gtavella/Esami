
def verifica_liste(L1,L2,k):
    for i in range(len(L1)-k+1):
        sottolista=L1[i:i+k]
        if hanno_ordine(sottolista,L2):
            return True
    return False


def hanno_ordine(sottolista,L):
    primo=sottolista[0]
    if primo not in L:
        return False
    i_prec=L.index(primo)
    for x in sottolista[1:]:
        if x not in L:
            return False
        i=L.index(x)
        if i<i_prec:
            return False
        i_prec=i
    return True




L1=[3,1,2,5,7,3,5,3]
L2=[8,1,7,4,2,6,3,5,4]
k=3
print(verifica_liste(L1,L2,k))
