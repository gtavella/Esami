# Si scriva una funzione verifica_liste che riceve una lista L1 di interi e una lista L2 di booleani. La funzione restituisce
# True se e solo se per tutti gli indici i tali che L2[i]==True, la lista L1 non contiene elementi di valore uguale a L1[i] in
# posizione diversa da i.
# Esempio: Se L1 = [7, 4, 7, 3, 5, 6] ed L2 = [False, True, False, True, True, False], allora la funzione restituisce True perché:
#  gli indici tali che L2[i]==True sono 1, 3 e 4;
#  la lista L1 non contiene elementi di valore uguale a L1[1] (cioè pari a 4) in posizione diversa da 1;
#  la lista L1 non contiene elementi di valore uguale a L1[3] (cioè pari a 3) in posizione diversa da 3;
#  la lista L1 non contiene elementi di valore uguale a L1[4] (cioè pari a 5) in posizione diversa da 4.



# L1 e' la lista di interi
# L2 e' la lista di booleani
def verifica_liste(L1, L2):
    for i in range(len(L2)):
        # se e' vero
        if L2[i]:
            # allora prendi il numero corrispondente all'indice attuale in L1
            x = L1[i]
            # selezione l'elemento che corrisponde all'indice attuale in L1
            # parti dall'inizio e fermati prima dell'indice attuale, quindi da 0 a i
            sottolista_sinistra = L1[0:i]
            # comincia dal prossimo dell'indice attuale e fermati alla fine, quindi da i+1 alla fine
            sottolista_destra = L1[i+1:]
            # se questo numero e' presente o a sinistra o a destra
            # questo e' equivalente a dire "L1 non contiene un'altra volta lo stesso numero"
            # che in poche parole significa che c'e' solo una volta nell'intera lista, cioe' che e' unico
            # uso la condizione negata per uscire dalla verifica con falsa alla prima occorrenza della condizione non soddisfata
            if x in sottolista_sinistra or x in sottolista_destra:
                return False
    return True


L1 = [7, 4, 7, 3, 5, 6]
L2 = [False, True, False, True, True, False]

print(verifica_liste(L1, L2))
