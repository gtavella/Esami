#
# Si scriva una funzione costruisci_lista che riceve in ingresso due liste L1 ed L2 e restituisce una lista L3
# contenente alcuni elementi della lista L1. In particolare, l’elemento L1[i] è incluso in L3 se e solo se sono
# soddisfatte entrambe le seguenti condizioni:
# • L1[i] è inferiore alla somma degli elementi di indice dispari della lista L2;
# • L1[i] è maggiore di tutti gli elementi della lista L2 il cui indice è maggiore di i.
# Se L2 non contiene elementi con indice maggiore di i, la seconda condizione si intende verificata. Nel caso in
# cui nessun valore rispetti entrambe le condizioni, L3 è vuota.
# Esempio: Se L1 = [1,3,8,4,7,12,3,9] e L2 = [3,4,2,1,3,5], allora L3 = [8,7,3,9], perché ciascuno di questi valori
# è minore di 10 e maggiore di tutti gli elementi di L2 con indice superiore.


# FUNZIONA, LO PUOI PUBBLICARE


def costruisci_lista(L1,L2):
    L3=[]
    for i in range(len(L1)):
        if condizione1(L1[i], L2) and condizione2(L1[i], L2[i+1:]):
            L3.append(L1[i])
    return L3


def condizione1(x,L):
    somma=0
    for i in range(1, len(L), 2):
        somma+=L[i]
    return x<somma

def condizione2(x,L):
    if len(L) == 0: return True
    for el in L:
        if el>x:
            return False
    return True



print(costruisci_lista([1,3,8,4,7,12,3,9], [3,4,2,1,3,5]))
