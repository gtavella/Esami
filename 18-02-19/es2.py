# Si scriva una funzione elabora_lista che riceve una lista L1 di interi positivi e restituisce una lista L2 della stessa
# lunghezza di L1, il cui generico elemento L2[i] contiene il massimo tra spi ed ssi, dove spi è la somma degli elementi di
# L1 in posizione precedente a i ed ssi è la somma degli elementi di L1 in posizione successiva a i. Ovviamente, se i = 0 si
# ha spi = 0, mentre se i = len(L1)-1 si ha ssi = 0.
# Esempio: Se L1 = [7, 4, 7, 3, 6, 8], allora la funzione restituisce la lista L2 = [28, 24, 17, 18, 21, 27].



def somma_precedenti(M, curr_index): 
    s = 0
    for i in range(0, curr_index):
        s += M[i]
    return s



def somma_successivi(M, curr_index):
    s = 0
    for i in range(curr_index+1, len(M)):
        s += M[i]
    return s 



def elabora_lista(L1):
    L2 = [0] * len(L1)
    for i in range(len(L1)):
        # somma precedenti
        spi = somma_precedenti(L1, i)
        # somma successivi   
        ssi = somma_successivi(L1, i)

        if spi > ssi:
            max_somma = spi
        else:
            max_somma = ssi
        L2[i] = max_somma 
    return L2



L1 = [7, 4, 7, 3, 6, 8]
print( elabora_lista(L1) )
