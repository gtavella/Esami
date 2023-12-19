#
# Si scriva una funzione verifica che riceve una matrice M di interi e restituisce True se e solo se, per ogni generico
# elemento x = M[i][j], il valore x compare almeno x volte in M.
# Esempio: Se M = [
# 2 5 2 5 5
# 5 3 3 4 3
# 4 2 4 5 4
# ] allora la funzione restituisce True perché il valore 2 è presente 3 volte, il valore 3 è
# presente 3 volte, il valore 4 è presente 4 volte e il valore 5 è presente 5 volte.



def verifica(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            x=M[i][j]
            if not totale_occorrenze(x,M) >= x:
                return False
    return True


def totale_occorrenze(x,M):
    c=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j]==x:
                c+=1
    return c


M = [[2, 5, 2, 5, 5],
     [5, 3, 3, 4, 3],
     [4, 2, 4, 5, 4]]

print(verifica(M))
