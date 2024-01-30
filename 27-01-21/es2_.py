# Si scriva una funzione verifica_liste che riceve una lista L1 di interi positivi distinti ed una lista L2 di interi. La funzione
# restituisce True se e solo se per ogni elemento x = L1[i], la lista L2 contiene una sottolista di lunghezza almeno x
# contenente solo elementi uguali ad x.
# Esempio: Se L1 = [3, 1, 4] ed L2 = [-3, 2, 1, 5, 4, 4, 4, 4, -1, 2, 3, 3, 3, 3], allora la funzione restituisce True perché
# l’elemento L[0] ha valore pari a 3 e la lista L2 contiene una sottolista di lunghezza 4 contenente solo elementi uguali
# a 3, l’elemento L1[1] ha valore pari ad 1 e la lista L2 contiene una sottolista di lunghezza 1 contenente solo elementi
# uguali a 1 e l’elemento L[2] ha valore pari a 4 e la lista L2 contiene una sottolista di lunghezza 4 contenente solo
# elementi uguali a 4.



def verifica_liste(L1,L2):
    for x in L1:
        if not condition(x,L2):
            return False
    return True


# condition: list L2 contains sublist of x's of x length
def condition(x,L):
    c=0
    for el in L:
        if el==x:
            c+=1
            if c == x:
                return True
        else:
            c=0
    return False


L1 = [3, 1, 4]
L2 = [-3, 2, 1, 5, 4, 4, 4, 4, -1, 2, 3, 3, 3, 3]
print(verifica_liste(L1,L2))
