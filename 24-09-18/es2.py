# Si scriva una funzione esamina_lista che riceve una lista L di interi distinti e restituisce un booleano. In particolare, la
# funzione restituisce True se e solo se L contiene due elementi il cui scambio rende L ordinata in senso crescente.
# Esempio: Se L = [1, 2, 10, 6, 9, 4, 12] allora la funzione restituisce True perché, dopo aver scambiato gli elementi di
# valore 10 e 4, la lista risulta ordinata in senso crescente


# visto che lista crescente significa che ogni prossimo elemento e' strettamente maggiore del precedente, questo implica che
# affinche' esista la condizione richiesta dalla traccia, ci devono essere due elementi tali per cui
# il prossimo elemento e' minore dell'elemento attuale
# se esistono, il loro indice viene salvato a parte
# poi bisogna verificare che il secondo elemento trovato sia strettamente compreso tra l'elemento precedente e successivo del suo indice
# stessa cosa per il secondo elemento

# so bene che questo algoritmo e' un verboso
# feedback e' il benvenuto

def scambio_e_valido(L,indice_a, indice_b):
    elemento_a = L[indice_a]
    elemento_b = L[indice_b]
    # gli elementi che hai trovato che non seguono la proprieta' di crescenza della lista,
    # percaso se li volessi scambiare, non e' che rendono la lista crescente?
    if (elemento_b > L[indice_a - 1] and elemento_b < L[indice_a + 1]) and (elemento_a > L[indice_b - 1] and elemento_a < L[indice_b + 1]):
        return True
    return False


def esistono_scambi_validi(L, indici):
    indice_a1, indice_a2 = indici[0]
    indice_b1, indice_b2 = indici[1]

    # testa con tutte le combinazioni di elementi che hai trovato
    if scambio_e_valido(L,indice_a1, indice_b1):
        print('indici', indice_a1, indice_b1,'scambia', L[indice_a1], 'con', L[indice_b1])
        return True
    if scambio_e_valido(L,indice_a1, indice_b2):
        print('indici',indice_a1, indice_b2,'scambia', L[indice_a1],'con', L[indice_b2])
        return True
    if scambio_e_valido(L,indice_a2, indice_b1):
        print('indici',indice_a2, indice_b1,'scambia', L[indice_a2],'con', L[indice_b1])
        return True
    if scambio_e_valido(L,indice_a2, indice_b2):
        print('indici',indice_a2, indice_b2,'scambia', L[indice_a2],'con', L[indice_b2])
        return True

    return False


def esamina_lista(L):
    # chiamo a il primo elemento
    # chiamo b il secondo elemento
    indici_da_scambiare = []
    n_precedente = L[0]
    # infatti due elementi siano strettamente crescenti il prossimo deve essere maggiore del precedente
    # quindi cerco un elemento attuale che e' maggiore del prossimo (cioe' NON sono strettamente crescenti)
    for i in range(1, len(L)):
        # se il numero attuale e' minore del precedente
        if L[i] < n_precedente:
            # allora salvo l'indice dove ho trovato l'elemento piu' grande che non e' strett. crescente
            # prendi entrambi gli indici, perche' non sai quale funzionera'
            indici_da_scambiare.append([i-1, i])
        # ad ogni iterazione l'elemento attuale diventa quello precedente per la prossima iterazione
        n_precedente = L[i]
    if esistono_scambi_validi(L,indici_da_scambiare):
        return True
    return False



L = [1, 2, 10, 6, 9, 4, 12]


print(esamina_lista(L))
