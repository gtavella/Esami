# Si scriva una funzione verifica_liste che riceve due liste L1 ed L2 di interi e un intero k e restituisce True se e solo se
# ogni elemento L1[i] è presente in L2 in i-esima posizione oppure in una posizione che dista al più k posizioni dall’iesima.
# Esempio: Se L1 = [3, 1, 8, 5, 4], L2 = [8, 1, 3, 4, 5] e k = 2, allora la funzione restituisce True perché l’elemento L1[0] è
# presente in L2 in posizione 2, l’elemento L1[1] è presente in L2 in posizione 1, l’elemento L1[2] è presente in L2 in
# posizione 0 e così via.


# itera su ogni elemento di L1
# seleziona lo stesso elemento di L2
# prendi la sottolista a sinistra e a destra dell'i-esimo elemento di L2, incluso l'i'esimo elemento
# verifica condizione negata: se l'i-esimo elemento non esiste ne' nella sottolista sinistra ne' destra, allora ritorna falso
# fai attenzione all'indice agli estremi della lista (inizio e fine)


# accetta in input la
# lista: su cui iterare
# i: l'indice dell'elemento che vogliamo verificare
# x: l'elemento che vogliamo verificare
# k: di quanti 'passi' fare lo slicing per ottenere la sottolista
def sottolista_valida(lista, i, x, k):
    # per non prendere valori partendo dalla fine, devi assicurarti che
    # il minimo indice puo' essere al massimo 0 (cioe' non puo' essere mai negativo, altrimenti farebbe lo slicing partendo dalla fine)
    if i-k < 0:
        sottolista = lista[0:i+k+1]
    # invece non ci sono problemi se fai lo slicing di una lista con un upper indice che non esiste
    else:
      sottolista = lista[i-k:i+k+1]
    # esci al soddisfacimento della condizione negata
    if x not in sottolista:
        return False
    return True



def verifica_liste(L1, L2, k):
    # itera per ogni elemento di L1
    for i in range(len(L1)):
        # il numero che voglio verificare
        x = L1[i]
        # sottolista di L2 a sinistra e destra inclusa dell'indice i, incluso l'elemento all'indice i
        if not sottolista_valida(L2, i, x, k):
            return False
    return True



L1 = [3, 1, 8, 5, 4]
L2 = [8, 1, 3, 4, 5]
k = 2

print(verifica_liste(L1, L2, k))
