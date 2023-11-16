# Si scriva una funzione elabora_lista che riceve una lista L1 di interi e restituisce una lista L2 della stessa lunghezza di
# L1 così costruita:
#  se il generico elemento L1[i] è pari, allora l’elemento L2[i] contiene la somma dei tre elementi di L1 successivi
# all’i-esimo;
#  se L1[i] è dispari, allora l’elemento L2[i] contiene la somma dei tre elementi di L1 precedenti all’i-esimo.
# Se gli elementi precedenti o successivi all’i-esimo sono meno di tre, si considerino nella somma solo quelli presenti.
# Esempio: Se L1 = [7, 4, 7, 3, 6, 8], allora la funzione restituisce la lista L2 = [0, 16, 11, 18, 8, 0].


def somma_lista(lista):
    s = 0
    for i in range(len(lista)): 
        s += lista[i]
    return s


def elabora_lista(L1):
    # inizializza lista con valori nulli
    L2 = [0] * len(L1)
    for i in range(len(L1)):
        l1 = L1[i]
        # se pari
        if l1 % 2 == 0:
            # lista di prossimi 3 valori (al massimo)
            sublist = L1[i+1:i+4]
            # somma 3 numeri succssivi
            L2[i] = somma_lista(sublist)
        # se dispari
        else:
            # lista di 3 precedenti valori (al massimo)
            if i < 3:
                sublist = L1[0: i]
            else:
                sublist = L1[i-3:i]
            # somma 3 numeri precedenti
            L2[i] = somma_lista(sublist)
    return L2


L1 = [7, 4, 7, 3, 6, 8]
print( elabora_lista(L1) )
