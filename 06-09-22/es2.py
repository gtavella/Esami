
# Si scriva una funzione codifica_lista che riceve una lista a e restituisce una lista che contiene tutti i valori
# distinti di a seguiti dal numero delle loro occorrenze.
# Esempio: Se a = [1,2,3,4,1,1,2,3,5,4,5,2,8], codifica_lista(a) restituisce [1,3,2,3,3,2,4,2,5,2,8,1] perché il valore
# 1 compare 3 volte, il valore 2 compare 3 volte, il valore 3 compare 2 volte, il valore 4 compare 2 volte, ecc




# VERSIONE CON DIZIONARIO
def codifica_lista1(a):
    ret=[]
    unici_dict = {}
    for x in a:
        if x in unici_dict:
            unici_dict[x] += 1
        else:
            unici_dict[x] = 1
    for x in unici_dict.keys():
        ret.append(x)
        ret.append(unici_dict[x])
    return ret

# print(codifica_lista1([1,2,3,4,1,1,2,3,5,4,5,2,8]))


# VERSIONE CON LISTE

def codifica_lista2(a):
    ret=[]
    unici=calcola_unici(a)
    for x in unici:
        ret.append(x)
        ret.append(calcola_occorrenze(x,a))
    return ret

def calcola_unici(L):
    ret=[]
    for x in L:
        if x not in ret:
            ret.append(x)
    return ret

def calcola_occorrenze(x,L):
    c=0
    for el in L:
        if el == x:
            c += 1
    return c


print(codifica_lista2([1,2,3,4,1,1,2,3,5,4,5,2,8]))
