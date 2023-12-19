# Si scriva una funzione verifica che riceve una matrice M di interi e restituisce True se e solo se il primo elemento di
# ogni riga i è il massimo oppure il minimo della riga i.
# Esempio: Se M = [
# 2 5 3 5 5
# 5 3 3 4 3
# 9 2 4 5 4
# ] allora la funzione restituisce True perché il primo elemento della riga 0 è il minimo
# della riga, il primo elemento della riga 1 è il massimo della riga e il primo elemento della riga 2 è il massimo della riga.



def verifica(M):
    for riga in M:
        primo=riga[0]
        massimo=max(riga)
        minimo=min(riga)
        if not primo == massimo and not primo == minimo:
            return False
    return True


M = [[2, 5, 3, 5, 5],
     [5, 3, 3, 4, 3],
     [9, 2, 4, 5, 4]]

print(verifica(M))
