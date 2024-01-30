# Si scriva una funzione verifica_lista che riceve in ingresso una lista
# L di interi ed un intero k. La funzione restituisce True se e solo se la lista L
# non contiene nessuna sotto-lista di lunghezza k avente valori strettamente crescenti
# Esempio: Se L=[4,5,5,6,1,1,2,2,5,3] allora verifica_lista(L,3) restituisce True perche' nessuna
# delle sotto-liste di lunghezza 3 [4,5,5], [5,5,6], [5,6,1], [6,1,1], [1,1,2], [1,2,2], [2,2,5], [2,5,3]
# ha valori strettamente crescenti.


def verifica_lista(L,k):
    for i in range(0,len(L)-k+1):
        sublist=L[i:i+k]
        if not condition(sublist):
            return False
    return True


# condition: all as
def condition(L):
    i=0
    flag=False
    while i<len(L)-1 and not flag:
        if L[i]>=L[i+1]:
            flag=True
        i+=1
    return flag

L=[4,5,5,6,1,1,2,2,5,3]
print(verifica_lista(L,3))
