# Si scriva una funzione verifica che riceve una lista L di interi e un intero k e restituisce True se e solo se L contiene
# almeno k elementi consecutivi uguali.
# Esempio: Se L = [1, 8, 2, 1, 1, 1, 2, 1] e k = 3 allora verifica(L,k) restituisce True perché L contiene 3 elementi consecutivi
# uguali


def verifica(L,k):
    # inizializzo contatore a 1
    c = 1
    # seleziona il primo numero come ultimo elemento
    last_x = L[0]
    # itera nella coda della lista (cioe' tutta la lista escluso il primo elemento)
    for i in range(1, len(L)):
        # l'elemento attuale
        x = L[i]
        # se l'ultimo elemento e' uguale all'attuale
        if last_x == x:
            # incrementa il contatore
            c += 1
            if c == k:
                return True
        # vuol dire che il numero attuale e l'ultimo non sono uguali
        else:
            # resetto il contatore a 1, questo perche' dire che il numero attuale
            # e' uguale al precedente, significa che ci sono gia' 2 match
            c = 1
        # il numero attuale sara' l'ultimo della prossima iterazione
        last_x = x
    return False


L = [1, 8, 2, 1, 1, 1, 2, 1]
k = 3

print(verifica(L, k))
