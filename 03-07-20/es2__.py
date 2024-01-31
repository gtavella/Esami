# Si scriva una funzione verifica_liste che riceve due liste L1 ed L2 di interi
# e un intero k e restituisce True se e solo se L1
# contiene una sottolista di lunghezza k i cui elementi sono presenti in L2 nello stesso ordine
# (anche se in posizioni non consecutive).
# Esempio: Se L1 = [3, 1, 2, 5, 7, 3, 5, 3], L2 = [8, 1, 7, 4, 2, 6, 3, 5, 4] e k = 3, allora la funzione restituisce True perché la
# lista L1 contiene la sottolista [1, 2, 5] i cui elementi sono presenti in L2 nello stesso ordine.


def verifica_liste(L1,L2,k):
    for i in range(0, len(L1)-k+1):
        if condition(L1[i:i+k],L2):
            return True
    return False



# condition: all elements of L1 exist in L2 whose index is in ascending order
def condition(L1,L2):
    # last index of match in L2
    next_i=0
    for x in L1:
        if x in L2[next_i:]:
            i_match=L2.index(x)
            next_i=i_match+1
        else:
            return False
    return True


L1 = [3, 1, 2, 5, 7, 3, 5, 3]
L2 = [8, 1, 7, 4, 2, 6, 3, 5, 4]
k = 3

# L1 = [5,3,5,3,1,5,6]
# L2 = [3,4,1,7,5,8,6]
# k = 4

print(verifica_liste(L1,L2,k))
