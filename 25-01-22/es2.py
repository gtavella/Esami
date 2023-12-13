# Si scriva una funzione verifica_dati che riceve in ingresso una lista L di stringhe ed un dizionario d le cui chiavi sono
# stringhe ed i valori ad esse associati sono array di interi. La funzione restituisce True se e solo se ogni chiave k di d
# occorre nella lista L, ma non nelle posizioni contenute in d[k].
# Esempio: Se L = [‘ciao’, ‘mondo’, ‘luce’] e d = { ‘ciao’:[1,2], ‘mondo’:[0]}, allora verifica_dati(L,d) restituisce True poiché
# sia ‘ciao’ sia ‘mondo’ compaiono nella lista L; inoltre ‘ciao’ si trova in L in posizione 0, che non è in d[‘ciao’]=[1,2], e
# ‘mondo’ si trova in posizione 1, che non è in d[‘mondo’]=[0]



def verifica_dati(L,d):
    for k in d.keys():
        if k not in L:
            return False
        indice=L.index(k)
        if indice in d[k]:
            return False
    return True


print(verifica_dati( ['ciao', 'mondo', 'luce'], { 'ciao':[1,2], 'mondo':[0]} ))
