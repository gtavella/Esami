# Si scriva una funzione verifica_sequenza che riceve una lista L di interi e un intero k e restituisce True se e solo se la
# lista contiene k elementi consecutivi la cui somma è pari a zero.
# Esempio: Se L = [6, 1, -5, 3, 1, -5, -1, 9] e k = 4, allora verifica_sequenza(L,k) restituisce True perché L contiene 4 elementi
# consecutivi (1, -5, 3 e 1) la cui somma è pari a zero.



def verifica_sequenza(L,k):
    # itera fino alla lunghezza di L meno k elementi
    # ad ogni iterazione aumenta indice mobile di 1
    for i in range(len(L)-k):
        # seleziona la sottolista dei prossimi k elementi
        sottolista = L[i:i+k]
        # se la loro somma e' uguale a 0, esci subito perche' hai soddisfatto la condizione
        if sum(sottolista) == 0:
            return True
    # se hai cercato per ogni sottolista e ancora non hai trovato una lista la cui somma e' uguale a zero, ritorna falso
    return False

L = [6, 1, -5, 3, 1, -5, -1, 9]
k = 4

print(verifica_sequenza(L,k))
