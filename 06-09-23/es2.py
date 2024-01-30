# Si scriva una funzione calcola_elementi_comuni che riceve in ingresso una lista L, in cui ogni elemento è una
# lista di numeri interi distinti, ordinata in modo crescente. La funzione restituisce una lista contente i numeri
# comuni a tutte le liste presenti in L.
# Esempio: Se L = [ [4,9,15,22], [3,4,9,15,18,22,27,55], [4,9,10,15,18,22], [4,9,15,19,22], [4,5,6,9,15,16] ], allora
# la funzione restituisce la lista [4,9,15].


def calcola_elementi_comuni(L):
    ret=[]
    source=L[0]
    rest=L[1:]
    for x in source:
        if condition(x,rest):
            ret.append(x)
    return ret


# condition: x must be in all lists of LL
def condition(x,LL):
    for L in LL:
        if x not in L:
            return False
    return True



L = [ [4,9,15,22], [3,4,9,15,18,22,27,55], [4,9,10,15,18,22], [4,9,15,19,22], [4,5,6,9,15,16] ]
print(calcola_elementi_comuni(L))
