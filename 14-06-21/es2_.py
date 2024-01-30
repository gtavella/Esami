# Si scriva una funzione lettere_comuni che riceve in ingresso una lista L di stringhe e restituisce una lista che contiene
# le lettere presenti in tutte le stringhe in L (in qualsiasi ordine).
# Esempio: Se L=[‘abc', ‘bdecf', ‘cabe', ‘bcfeg'], allora la funzione restituisce la lista [‘b', ‘c'].


def lettere_comuni(L):
    ret=[]
    source=L[0]
    for l in source:
        if condition(l,L[1:]):
            ret.append(l)
    return ret


# condition: l is in all strings in LL
def condition(l,LL):
    in_all=True
    i=0
    while i<len(LL) and in_all:
        if l not in LL[i]:
            in_all=False
        i+=1
    return in_all


L=['abc', 'bdecf', 'cabe', 'bcfeg']
print(lettere_comuni(L))
