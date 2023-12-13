# Si scriva una funzione verifica_minimi che riceve in ingresso una matrice m e restituisce True se e solo se la lista dei
# valori minimi di ciascuna colonna di m è ordinata in modo non crescente.
# Esempio: Se m = [
# 9 10 42 3
# 22 33 55 4
# 42 7 7 6
# 30 44 8 3
# ] allora la funzione restituisce True poiché la lista [9, 7, 7, 3] dei valori minimi di
# ciascuna colonna è ordinata in modo non crescente.




def verifica_minimi(m):
    colonne=trova_colonne(m)
    lista_minimi=calcola_minimi(colonne)
    return sono_tutti_decrescenti(lista_minimi)


def trova_colonne(M):
    ret=[]
    for i in range(len(M)):
        riga=[]
        for j in range(len(M[0])):
            riga.append(M[j][i])
        ret.append(riga)
    return ret

def calcola_minimi(L):
    return [min(lista) for lista in L]


def sono_tutti_decrescenti(L):
    prec=L[0]
    for attuale in L[1:]:
        if attuale>prec:
            return False
        prec=attuale
    return True


# m = [[9, 10, 42, 3],
#      [22, 33, 55, 4],
#      [42, 7, 7, 6],
#      [30, 44, 8, 3]]
# 
# 
# print(verifica_minimi(m))
