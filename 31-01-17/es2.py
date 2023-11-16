# Si scriva una funzione verifica che riceve una lista L di interi e un intero k e restituisce True se e solo se L contiene
# almeno k elementi consecutivi uguali.
# Esempio: Se L = [1, 8, 2, 1, 1, 1, 2, 1] e k = 3 allora verifica(L,k) restituisce True perché L contiene 3 elementi consecutivi
# uguali


def verifica(L,k):
    c = 1
    last_x = L[0]
    for i in range(1, len(L)):
        x = L[i]
        if last_x == x:
            c += 1
            if c == k:
                return True
        else:
            c = 1
        last_x = x
    return False


L = [1, 8, 2, 1, 1, 1, 2, 1]
k = 3

print(verifica(L, k))
