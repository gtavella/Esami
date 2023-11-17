# Si scriva una funzione verifica_liste che riceve una lista L1 di interi positivi distinti ed una lista L2 di interi. La funzione
# restituisce True se e solo se per ogni elemento x = L1[i], la lista L2 contiene una sottolista di lunghezza almeno x
# contenente solo elementi uguali ad x.
# Esempio: Se L1 = [3, 1, 4] ed L2 = [-3, 2, 1, 5, 4, 4, 4, 4, -1, 2, 3, 3, 3, 3], allora la funzione restituisce True perché
# l’elemento L[0] ha valore pari a 3 e la lista L2 contiene una sottolista di lunghezza 4 contenente solo elementi uguali
# a 3, l’elemento L[1] ha valore pari ad 1 e la lista L2 contiene una sottolista di lunghezza 1 contenente solo elementi
# uguali a 1 e l’elemento L[2] ha valore pari a 4 e la lista L2 contiene una sottolista di lunghezza 4 contenente solo
# elementi uguali a 4.



# itera per ogni elemento di L1
# cerca questo elemento in L2
# trova l'indice di questo elemento in L1
# prendi la sottolista con lunghezza "questo elemento"
# itera per ogni elemento in questa sottolista
# ogni elemento in questa sottolista deve essere uguale all'elemento di L1
# la prima volta che esiste un elemento diverso dall'elemento attuale di L1, ritorna falso
# altrimenti ritorna vero


# i: indice dal quale cominciare lo slicing
# x: indica sia il valore, che di quanti passi fare lo slicing
# assunzione: per "prossima sottolista" si intende anche l'elemento attuale
def sottolista_valida(lista, i, x):
    # la sottolista contiene x (l'elemento attuale incluso) piu' i prossimi x elementi
    sottolista = lista[i:i+x]
    for j in range(len(sottolista)):
        # se esiste un elemento nella sottolista che non e' uguale a x
        # cioe' testo la condizione negata
        if sottolista[j] != x:
            return False
    # se tutti gli elementi della sottolista sono uguali a x
    return True


def verifica_liste(L1, L2):
    for i in range(len(L1)):
        x = L1[i]
        x_exists = x in L2
        # se x non e' in L2
        if not x_exists:
            return False
        # se x e' in L2
        # ottieni l'indice di x in L2
        i_x = L2.index(x)
        # per ogni elemento di L1, se la sottolista non e' valida
        # i_x e' l'indice di x in L2
        if not sottolista_valida(L2, i_x, x):
            return False
    return True



L1 = [3, 1, 4]
L2 = [-3, 2, 1, 5, 4, 4, 4, 4, -1, 2, 3, 3, 3, 3]

print(verifica_liste(L1, L2))




