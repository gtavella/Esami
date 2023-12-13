
# Si scriva una funzione verifica_coppie che riceve in ingresso una lista L di interi positivi ed un intero k. La funzione
# verifica se esiste un valore n tale che L contiene almeno k coppie di elementi consecutivi uguali ad n (si noti che una
# sequenza di x valori uguali consecutivi equivale a x-1 coppie). Se tale valore esiste, la funzione lo restituisce. Se esiste
# più di un valore che soddisfa la condizione, la funzione ne restituisce uno qualsiasi. Se nessun valore soddisfa la
# condizione, la funzione restituisce -1.
# Esempio: Se L = [5, 5, 7, 1, 1, 7, 5, 7, 5, 5, 5, 1, 1, 3] e k = 3, allora la funzione restituisce 5


def verifica_coppie(L,k):
    cont=1
    prec=L[0]
    for i in range(1, len(L)):
        if L[i] == prec:
            cont += 1
            if cont == k:
                return L[i]
        else:
            prec=L[i]
            cont=1
    return -1


# print(verifica_coppie( [5, 5, 7, 1, 1, 7, 5, 7, 5, 5, 5, 1, 1, 3], 3))
