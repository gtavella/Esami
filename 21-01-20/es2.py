# Si scriva una funzione filtra_lista che riceve una lista L1 di interi non negativi e restituisce una lista L2 costruita come
# segue:
#  la funzione verifica se ogni elemento di L1 avente valore x > 0 è preceduto da almeno x zeri e seguito da almeno
# x zeri;
#  se tale condizione è vera, allora L2 contiene tutti gli elementi maggiori di zero presenti in L1; altrimenti, L2 è
# vuota.
# Esempio: Se L1 = [0, 1, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 1, 0, 0], allora la funzione restituisce la lista L2 = [1, 3, 2, 1].


# x e' sia un valore numerico, sia i passi per fare lo slicing
# caso limite: quando lo slicing comincia dall'inizio, assicurati che l'indice minimo sia sempre al piu' 0
# perche' altrimenti python comincierebbe dalla fine e noi vogliamo solo valori che cominciano dall'inizio


# ogni sottolista deve contenere 0
def sottolista_valida(L):
    if len(L) == 0:
        return False
    for i in range(len(L)):
        # testo la condizione negata
        if L[i] != 0:
            return False
    return True


def filtra_lista(L1):
    L2 = []
    # itera per ogni elemento di L1
    for i in range(len(L1)):
        # numero attuale
        x = L1[i]
        if x > 0:
            # casi limite: se da sinistra o da destra la sottolista e' piu' piccola del numero di passi x,
            # significa che in nessun caso conterra' un numero sufficiente di 0, quindi termina e ritorna lista vuota
            if (i-x >= 0) or (i+x <= len(L1)-1):
                sottolista_sinistra = L1[i-x:i]
                sottolista_destra = L1[i+1:i+x+1]
                if sottolista_valida(sottolista_sinistra) and sottolista_valida(sottolista_destra):
                    L2.append(x)
                # se anche una sola sottolista non e' valida (cioe' con almeno un elemento diverso da 0 o vuota)
                else:
                    return []
            # se non ci saranno comunque numero sufficiente di elementi
            else:
                return []
    return L2



L1 = [0, 1, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 1, 0, 0]
print(filtra_lista(L1))
