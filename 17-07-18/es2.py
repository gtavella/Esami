# Data una lista L, indichiamo con x il generico elemento di L e con x_ l’elemento in posizione simmetrica ad x. Si scriva
# una funzione esamina_lista che riceve una lista L di interi positivi avente lunghezza pari e restituisce un booleano. In
# particolare, la funzione restituisce True se e solo se, per ogni elemento x di L, la somma dei valori di x e x_ è maggiore
# della somma dei valori degli elementi posizionati tra x e x_.
# Si noti che, quando x e x_ sono adiacenti, la somma dei valori degli elementi posizionati tra x e x_ può essere assunta
# pari a zero.
# Esempio: Se L = [12, 9, 7, 2, 1, 1, 3, 12] allora la funzione restituisce True, perché:
# • 12 + 12 > 9 + 7 + 2 + 1 + 1 + 3;
# • 9 + 3 > 7 + 2 + 1 + 1;
# • 7 + 1 > 2 + 1;
# • 2 + 1 > 0





# seleziona la meta' della lista L
# itera fino alla meta' della lista L
# mentre iteri su ogni elemento di L, seleziona il suo elemento simmetrico
# calcola la somma tra questi due elementi
# seleziona la sottolista compresa tra questi due elementi (con i due elementi esclusi)
# se la sottolista e' vuota (cioe' sono elementi adiacenti), allora la somma di questa sottolista e' 0


def esamina_lista(L):
    # i e' l'indice 'mobile', mentre n rimane fermo
    i = 0
    n = len(L)-1
    # itera solo fino alla meta' della lista
    while i < len(L)/2:
        # elemento attuale
        a = L[i]
        # elemento simmetrico
        b = L[n-i]
        # sottolista dall'i-esimo elemento al suo simmetrico (con estremi esclusi)
        somma_sottolista_interna = sum(L[i+1:n-i])
        somma_estremi = a + b
        # esco al soddisfacimento della condizione negata
        if somma_estremi <= somma_sottolista_interna:
            return False
        i += 1
    return True




L = [12, 9, 7, 2, 1, 1, 3, 12]

print(esamina_lista(L))




