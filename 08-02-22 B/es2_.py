# Si scriva una funzione verifica_lista che riceve in ingresso una lista L di stringhe ed un intero k.
# Si assuma che la lista L abbia lunghezza maggiore di k. La funzione restituisce True se e solo se ogni stringa di L avente k
# stringhe precedenti ha almeno una lettera in comune con tali stringhe.
# Esempio: Se L=['abcd', 'efgh', 'abe', 'af', 'bef'], allora verifica_lista(L,2) restituisce True perche':
# 'abe' ha almeno una lettera in comune sia con 'abcd' che con 'efgh'
# 'af' ha almeno una lettera in comune sia con 'efgh' che con 'abe'
# 'bef' ha almeno una lettera in comune sia con 'abe' che con 'af'


def verifica_lista(L,k):
    for i in range(k,len(L)):
        if not condition(L[i], L[i-k:i]):
            return False
    return True


def condition(A,Z):
    # when is the condition false?
    # when after each string X of a list of strings Z is such that there's no letter in common between X and A
    for X in Z:
        found=False
        i=0
        while i<len(A) and not found:
            l=A[i]
            if l in X:
                found=True
            i+=1
        if not found:
            return False
    return True





L=['abcd', 'efgh', 'abe', 'af', 'bef']
print(verifica_lista(L,2))
