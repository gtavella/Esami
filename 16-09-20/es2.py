# Si scriva una funzione verifica_lista che riceve una lista L di interi e restituisce True se e solo se ogni elemento di L
# avente valore n > 0 è immediatamente seguito da almeno n elementi aventi valore minore o uguale a 0.
# Esempio: Se L = [-3, 1, -2, 2, 0, -1, -3, 3, 0, -1, -3, -1], allora la funzione restituisce True perché l’elemento L[1] = 1 è
# seguito da un elemento minore o uguale a 0, l’elemento L[3] = 2 è seguito da 3 elementi minori o uguali a 0 e l’elemento
# L[7] = 3 è seguito da 4 elementi minori o uguali a 0.



# prendi ogni prossima sottolista di n elementi (se esiste)
# verifica che al suo interno ogni elemento sia minore o uguale a 0
# se condizione non soddisfatta, allora ritorna falso
# i: l'indice attuale di n
# n: il numero attuale, che indica di quanti 'passi' fare lo slicing
def prossima_sottolista_valida(L, i, n):
    # parti dal prossimo elemento (incluso), quindi i+1
    # includi anche l'ultimo elemento, quindi i+n+1
    prossima_sottolista = L[i+1:i+n+1]
    # se prendi una sottolista finale piu' piccola di n, vuol dire che gli ultimi elementi "non bastano" per coprire
    # quindi in questo case la sottolista non e' comunque valida
    # questo include il caso in cui la prossima sottolista sia vuota, cioe' quando il numero e' proprio l'ultima
    # (infatti l'ultimo elemento non ha "una prossima sottolista")
    if len(prossima_sottolista) < n:
        return False
    # print(prossima_sottolista, L, i, n)
    for j in range(len(prossima_sottolista)):
        # se c'e' almeno un elemento che non soddisfa la condizione, ovvero
        # siccome il negato di "minore o uguale a 0" e' "maggiore di 0", testo la condizione negata
        if prossima_sottolista[j] > 0:
            return False
    # allora tutti i numeri della sottolista sono minori o uguali a 0, cioe' rispettano la condizione
    return True



def verifica_lista(L):
    for i in range(len(L)):
        # ogni numero in L indica anche di quanti 'passi' fare lo slicing di L
        # cioe' quanti elementi dovra' contenere la prossima sottolista
        n = L[i]
        if n > 0:
            if not prossima_sottolista_valida(L, i, n):
                return False
    return True



L = [-3, 1, -2, 2, 0, -1, -3, 3, 0, -1, -3, -1]
L1 = [1, -2, 1, -2, 3, -2, -1, -1, 1, -1, 1, -2, 2, -1, -1, -2]

print(verifica_lista(L1))
