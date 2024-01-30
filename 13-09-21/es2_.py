# Si scriva una funzione verifica_coppie che riceve in ingresso una lista L di interi positivi ed un intero k. La funzione
# verifica se esiste un valore n tale che L contiene almeno k coppie di elementi consecutivi uguali ad n (si noti che una
# sequenza di x valori uguali consecutivi equivale a x-1 coppie). Se tale valore esiste, la funzione lo restituisce. Se esiste
# più di un valore che soddisfa la condizione, la funzione ne restituisce uno qualsiasi. Se nessun valore soddisfa la
# condizione, la funzione restituisce -1.
# Esempio: Se L = [5, 5, 7, 1, 1, 7, 5, 7, 5, 5, 5, 1, 1, 3] e k = 3, allora la funzione restituisce 5



def verifica_coppie(L,k):
    c=1
    prev=L[0]
    if k==1: return prev
    
    for i in range(1,len(L)):
        curr=L[i]
        if curr==prev:
            c+=1
        else:
            c=1
        if c==k:
            return curr
        prev=curr
        
    return -1


L=[5, 5, 7, 1, 1, 7, 5, 7, 5, 5, 5, 1, 1, 3]
k=3
print(verifica_coppie(L,k))
