# Si scriva una funzione calcola_lista che riceve una lista L di interi ed un intero x e restituisce una lista
# contenente tutti gli indici i che soddisfano le seguenti condizioni:
# • l'elemento L[i] ha almeno x elementi successivi;
# • nessuno degli x elementi successivi ad L[i] ha valore maggiore di L[i].
# Esempio: Se L = [3, 1, 2, 1, 2, 2, -1, 4] e x = 3, allora la funzione restituisce la lista [0, 2] perché:
# • l'elemento L[0] = 3 ha 7 (>=x) elementi successivi e i primi x di essi sono <= 3 (1, 2 ed 1);
# • l'elemento L[1] = 1 ha 6 (>=x) elementi successivi, ma almeno uno tra i primi x è > 1 (L[2] = 2);
# • l'elemento L[2] = 2 ha 5 (>=x) elementi successivi e i primi x di essi sono <= 2 (1, 2 e 2);
# • l'elemento L[3] = 1 ha 4 (>=x) elementi successivi, ma almeno uno tra i primi x è > 1 (L[4] = 2);
# • l'elemento L[4] = 2 ha 3 (>=x) elementi successivi, ma almeno uno tra i primi x è > 2 (L[7] = 4);
# • gli elementi L[5], L[6] ed L[7] non hanno 3 elementi successivi.


def calcola_lista(L,x):
    ret=[]
    for i in range(0,len(L)-x):
        if condition(L[i], L[i+1:i+1+x]):
            ret.append(i)
    return ret


# condition: x >= all elements in L
def condition(x,L):
    for el in L:
        if el>x:
            return False
    return True



L = [3, 1, 2, 1, 2, 2, -1, 4]
x = 3
print(calcola_lista(L,x))
