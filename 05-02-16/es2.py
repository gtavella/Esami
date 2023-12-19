# Data una matrice quadrata di interi M, un elemento M[i,j] è detto “punto di sella” se risulta essere
# contemporaneamente il minimo della riga i e il massimo della colonna j.
# Si scriva una funzione Python punti_di_sella che riceve una matrice quadrata di interi M e restituisce una lista di coppie
# di indici (i,j) che individuano la riga e la colonna in cui si trovano i punti di sella in M (se esistono).
# Esempio: se M = [
# 4 5 5 9
# 6 7 6 7
# 6 8 6 9
# 5 2 3 3
# ] allora punti_di_sella(M) restituisce [(1,0), (1,2), (2,0), (2,2)].



def punti_di_sella(M):
    ret=[]
    max_colonne=calcola_massimi_colonne(M)
    min_righe=calcola_minimi_righe(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == min_righe[i] and M[i][j] == max_colonne[j]:
                ret.append([i,j])
    return ret


def calcola_massimi_colonne(M):
    ret=[]
    for i in range(len(M)):
        colonna=[]
        for j in range(len(M[0])):
            colonna.append(M[j][i])
        ret.append(max(colonna))
    return ret


def calcola_minimi_righe(M):
    ret=[]
    for riga in M:
        ret.append(min(riga))
    return ret


M = [[4, 5, 5, 9],
     [6, 7, 6, 7],
     [6, 8, 6, 9],
     [5, 2, 3, 3]]


print(punti_di_sella(M))
