# Si scriva una funzione verifica_presenza che riceve due array a e b,
# e restituisce un array v della stessa lunghezza di a. In particolare, l'i-esimo elemento di v e' calcolato come segue:
# - se a[i] e' uguale ad almeno un elemento di b, allora v[i] = a[i]
# - altrimenti, v[i] e' uguale alla somma degli elementi di a con indice minore o uguale ad i
# Esempio: Se a = [5, 2, 3, 5, 9, 3] e b = [3, 5, 7] l'array restituito e' v = [5, 7, 3, 5, 24, 3]



# inizializza una lista v
# per ogni elemento di lista a
# ottieni l'indice
# l'i-esimo elemento nella lista a esiste nella lista b?
# se esiste, l'i-esimo elemento di v e' l'i-esimo elemento di a
# altrimenti seleziona la sottolista dall'inizio fino all'indice attuale i (incluso)
# poi calcola la somma dei numeri di questa sottolista


def verifica_presenza(a,b):
    # inizializzo la lista v con la stessa lunghezza di a
    # assunzione: il valore 0 e' un segnaposto (quindi valore temporaneo)
    # assunzione: ogni segnaposto 0 verra' cambiato subito dopo l'inizializzazione della lista v
    v = [0] * len(a)
    for i in range(len(a)):
        # elemento attuale di a
        x = a[i]
        # se l'elemento attuale di x c'e' almeno una volta in b:
        if x in b:
            v[i] = x
        else:
            # seleziona la sottolista con i incluso (quindi i+1)
            # poi fai la somma
            v[i] = sum(a[:i+1])
    return v



a = [5, 2, 3, 5, 9, 3]
b = [3, 5, 7]

print(verifica_presenza(a, b))
