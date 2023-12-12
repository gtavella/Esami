# Si scriva una funzione calcola_lista che riceve una lista L di interi ed un intero x e restituisce una lista
# contenente ogni sottolista di L che soddisfa le seguenti condizioni:
# • ha lunghezza x;
# • contiene solo elementi che non sono minori di x;
# • la somma dei suoi elementi è multipla di x.
# Esempio: Se L = [4, 3, 5, 2, 4, 6, 9, 9, 6] e x = 3, allora la funzione restituisce la lista [[4, 3, 5], [6, 9, 9], [9, 9, 6]].
# Si noti che le liste contenute nel risultato soddisfano le prime due condizioni e le somme dei loro elementi
# sono 12, 24 e 24, rispettivamente, che sono multipli di 3.



def calcola_lista(L,x):
    ret=[]
    for i in range(len(L)-x+1):
        sottolista=L[i:i+x]
        if tutti_maggiori(sottolista, x) and somma_e_multiplo(sottolista, x):
            ret.append(sottolista)
    return ret

def tutti_maggiori(L,x):
    for el in L:
        if el<x:
            return False
    return True

def somma_e_multiplo(L,x):
    return sum(L) % x == 0



# print(calcola_lista([4, 3, 5, 2, 4, 6, 9, 9, 6], 3))
