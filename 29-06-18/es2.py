# Si scriva una funzione esamina_lista che riceve una lista L di interi non negativi e un intero t e restituisce un intero k.
# In particolare, k è il massimo valore tale che tutte le sotto-liste di lunghezza k presenti in L hanno somma minore o
# uguale a t. Se L contiene almeno un elemento maggiore di t, allora la funzione restituisce 0. Si noti che il valore k sarà
# quindi sempre compreso tra 0 e la lunghezza di L.
# Esempio: Se L = [3, 0, 7, 2, 0], e t = 10, allora il valore restituito dev’essere 3, perché:
#  la sottolista di lunghezza 5 ([3, 0, 7, 2, 0]) ha somma pari a 12;
#  le sottoliste di lunghezza 4 ([3, 0, 7, 2] e [0, 7, 2, 0]) hanno rispettivamente somma pari a 12 e 9;
#  le sottoliste di lunghezza 3 ([3, 0, 7], [0, 7, 2] e [7, 2, 0]) hanno rispettivamente somma pari a 10, 9 e 9.


# crea sottoliste partendo dalla stessa lunghezza della lista in input
# crea la prossima sottolista partendo muovendoti a 3 passi alla volta
# calcola la somma di ogni sottolista


# L: lista iniziale
# k: di quanti passi fare le sottoliste
def crea_sottoliste(L,k):
    sottoliste = []
    # i: indice mobile
    i = 0
    # continua ad iterare finche' la somma tra l'indice attuale e il passo arriva alla fine
    while i+k <= len(L):
        sottoliste.append(L[i:i+k])
        # avanza di 1 indice ad ogni iterazione
        i += 1
    return sottoliste


def somma_sottoliste_minore_di_t(sottoliste,t):
    for sottolista in sottoliste:
        # testo la condizione negata
        if sum(sottolista) > t:
            return False
    return True


def lista_ha_maggiore_di_t(L,t):
    for x in L:
        if x > t:
            return True
    return False



def esamina_lista(L, t):
    if lista_ha_maggiore_di_t(L,t):
        return 0
    # inizializza k
    # k: massimo valore tale che tutte le sotto-liste di lunghezza k presenti in L hanno somma minore o uguale a t
    # comincia dalla sottolista che e' proprio la lista iniziale stessa
    k = len(L)
    # per ogni iterazione, riduci n di 1 fino ad arrivare a 1
    while k >= 1:
        sottoliste = crea_sottoliste(L,k)
        if somma_sottoliste_minore_di_t(sottoliste,t):
            return k
        k -= 1
    # non e' specificato nella traccia cosa dovrei tornare nel caso in cui non si trovasse nessun valore k, ho scelto di ritornare 0
    return 0




L = [3, 0, 7, 2, 0]
t = 10

print(esamina_lista(L,t))

