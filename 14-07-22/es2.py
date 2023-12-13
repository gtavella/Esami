

# Si scriva una funzione verifica_lista che riceve in ingresso una lista L di interi ed un intero k. La funzione
# restituisce True se e solo se la lista L non contiene nessuna sotto-lista di lunghezza k avente valori
# strettamente crescenti.
# Esempio: Se L = [4,5,5,6,1,1,2,2,5,3], allora verifica_lista(L,3) restituisce True perché nessuna delle sotto-liste
# di lunghezza 3 ([4,5,5], [5,5,6], [5,6,1], [6,1,1], [1,1,2], [1,2,2], [2,2,5] e [2,5,3]) ha valori strettamente
# crescenti.



def calcola_sottoliste(L,k):
    ret=[]
    for i in range(len(L)-k+1):
        ret.append(L[i:i+k])
    return ret


def contiene_sottolista_cresc(liste):
    for lista in liste:
        non_crescente = False
        for i in range(1, len(lista)):
            if lista[i] <= lista[i-1]:
                non_crescente = True
                break
        if not non_crescente:
            return True
    return False


def verifica_lista(L,k):
    sottoliste=calcola_sottoliste(L,k)
    if contiene_sottolista_cresc(sottoliste):
        return False
    return True


print(verifica_lista([4,5,5,6,1,1,2,2,5,3], 3))
