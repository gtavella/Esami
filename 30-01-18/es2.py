# Si scriva una funzione elabora_lista che riceve una lista L1 di interi, la cui media indichiamo con m, e restituisce una
# lista L2 contenente gli elementi di L1 posizionati in modo tale che gli elementi minori o uguali ad m precedano i valori
# maggiori di m. Si noti che sono possibili diversi risultati corretti, purché sia rispettata la suddetta condizione.
# Esempio: Se L1 = [7, 4, 7, 3, 6, 8, 9, 1], allora un possibile risultato di elabora_lista(L1) è la lista L2 = [4, 3, 1, 7, 7, 6, 8,
# 9], perché la media dei valori in L1 è 5,625

# calcola la media di L1

def calcola_media(L):
    s=0
    for i in range(len(L)):
        s += L[i]
    return s/len(L)


def elabora_lista(L1):
    minori_di_m=[]
    maggiori_di_m=[]
    m=calcola_media(L1)
    # itera per ogni elemento di di L1
    for i in range(len(L1)):
        # generico elemento di L1
        x = L1[i]
        if x <= m:
            minori_di_m.append(x)
        else:
            maggiori_di_m.append(x)
    # concatena le due liste
    L2 = minori_di_m + maggiori_di_m
    return L2


L1 = [7, 4, 7, 3, 6, 8, 9, 1]

print(elabora_lista(L1))
