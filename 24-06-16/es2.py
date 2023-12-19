
#
# Si scriva una funzione confronto_indici che riceve una lista L di interi, di lunghezza n, e una lista P di interi distinti
# compresi tra 0 e n-1. La funzione restituisce True se e solo se la somma degli elementi di L il cui indice compare in P è
# maggiore della somma degli elementi di L il cui indice non compare in P.
# Esempio: Se L = [1, 7, 5, 2, -3, 4, 0] e P = [1, 2, 4] allora confronto_indici(L,P) restituisce True perché L[1]+L[2]+L[4] (pari
# a 9) è maggiore di L[0]+L[3]+L[5]+L[6] (pari a 7).



def confronto_indici(L,P):
    somma_P=0
    somma_altri=0
    for i in range(len(L)):
        if i not in P:
            somma_altri+=L[i]
    for p in P:
        somma_P+=L[p]
    return somma_P>somma_altri


print(confronto_indici([1, 7, 5, 2, -3, 4, 0], [1, 2, 4]))

