#
# Si scriva una funzione verifica_matrice che riceve una matrice di interi M di dimensioni n x n e due indici ir e jc, compresi
# tra 0 e n-1, e restituisce True se e solo se, per ogni elemento x presente nella riga ir, M contiene almeno due elementi
# uguali ad x al di fuori sia della riga ir che della colonna jc.
# Esempio: se M = [
# 8 0 3 −9 3
# 2 3 6 3 −1
# 1 2 5 7 −1
# 6 9 2 5 3
# 3 2 4 −1 6 ]
# , ir = 1 e jc = 2, allora la funzione restituisce True perché, per ogni elemento x nella
# riga 1 (gli elementi sono 2, 3, 6 e -1), M contiene almeno due elementi uguali ad x al di fuori sia della riga 1 che della
# colonna 2.



def verifica_matrice(M,ir,ic):
    unici_riga=ottieni_unici(M[ir])
    for x in unici_riga:
        if not esistono_due(x,M,ir,ic):
            return False
    return True


def esistono_due(x,M,ir,ic):
    c=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i != ir and j != ic and M[i][j]==x:
                c+=1
            if c == 2:
                return True
    return False


def ottieni_unici(L):
    ret=[]
    for x in L:
        if x not in ret:
            ret.append(x)
    return ret


M = [[8, 0, 3, -9, 3],
    [2, 3, 6, 3, -1],
    [1, 2, 5, 7, -1],
    [6, 9, 2, 5, 3],
    [3, 2, 4, -1, 6]]


# M = [[8, 0, 3, -9, 7],
#     [7, 3, 7, 2, 7],
#     [1, 1, 5, 7, -1],
#     [2, 9, 2, 9, 3],
#     [3, 1, 4, -1, 2]]


print(verifica_matrice(M,1,2))
