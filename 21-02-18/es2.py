# Si scriva una funzione massimi_sequenze che riceve due interi positivi n e k ed una lista L1 di interi avente lunghezza
# n*k e restituisce una lista L2 di lunghezza k costruita come segue:
#  consideriamo le n sotto-liste non sovrapposte di k elementi in L1;
#  l’elemento L2[j] contiene il massimo degli elementi che si trovano in posizione j nelle sotto-liste.
# Esempio: Se n = 4, k = 3 e L1 = [7, 4, 7, 3, 6, 8, 9, 1, 5, 6, 2, 5], allora:
#  le sottoliste non sovrapposte di 3 elementi in L1 sono [7, 4, 7], [3, 6, 8], [9, 1, 5] e [6, 2, 5];
#  L2[0] = 9 perché gli elementi in posizione 0 nelle sotto-liste sono 7, 3, 9 e 6;
#  L2[1] = 6 perché gli elementi in posizione 1 nelle sotto-liste sono 4, 6, 1 e 2;
#  L2[2] = 8 perché gli elementi in posizione 2 nelle sotto-liste sono 7, 8, 5 e 5


# crea sottoliste in modo che la fine +1 di una sottolista indica l'inizio della prossima

# trova il massimo valore in una lista
def trova_massimo(lista):
    valore_max = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > valore_max:
            valore_max=lista[i]
    return valore_max


def massimi_sequenze(n,k,L1):
    # popolo L2 con zero
    L2 = [0] * k
    sottoliste = []
    # crea le sottoliste
    # itera finche' hai raggiunto lunghezza di L1-k+1
    i=0
    while i < len(L1)-k+1:
        sottoliste.append(L1[i:i+k])
        # avanza l'indice mobile di k
        i += k
    # ora itera nelle sottoliste e trova il massimo elemento all'indice j
    for j in range(k):
        # tutti i numeri in un certa posizione j nelle sottoliste
        # riaggiorna ad ogni iterazione di j
        numeri_in_posizione_j = []
        for sottolista in sottoliste:
            # il numero che corrisponde alla sottolista attuale
            numeri_in_posizione_j.append(sottolista[j])
        # solo dopo che hai iterato, per la stessa posizione, in tutte le sottoliste, solo adesso
        # trova il massimo e salvalo nella posizione j di L2
        L2[j] = trova_massimo(numeri_in_posizione_j)
    return L2



n = 4
k = 3
L1 = [7, 4, 7, 3, 6, 8, 9, 1, 5, 6, 2, 5]

print(massimi_sequenze(n,k,L1))
