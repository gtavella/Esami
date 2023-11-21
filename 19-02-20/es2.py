# Si scriva una funzione verifica_liste che riceve due liste L1 ed L2 di interi e un intero k e restituisce True se e solo se L1
# ed L2 contengono due sottoliste uguali di lunghezza k.
# Esempio: Se L1 = [1, 2, 3, 7, 3, 5, 3], L2 = [8, 7, 3, 5, 4] e k = 3, allora la funzione restituisce True perché le liste contengono
# entrambe la sottolista [7, 3, 5].

# itera in L1 fino alla lunghezza di L1 meno k
# per ogni iterazione di L1, seleziona la sottolista con k elementi
# per ogni iterazione di L1, seleziona la sottolista con k elementi di L2
# relazione dei loop: per ogni iterazione di L1, itera in tutto L2

def hanno_sottoliste_uguali(lista1, lista2):
    # itera per ogni elemento di lista1
    # ogni elemento nella lista1 deve essere all'elemento allo stesso indice in lista2
    for i in range(len(lista1)):
        # se esiste almeno un elemento all'indice i che non e' diverso dall'elemento allo stesso indice in lista2
        if lista1[i] != lista2[i]:
            return False
    return True


def verifica_liste(L1,L2,k):
    esiste_sottolista_uguale = False
    # siccome voglio selezionare la sottolista anche dell'ultimo elemento, allora aggiungo 1 come indice dove fermare l'iterazione
    for i in range(len(L1)-k+1):
        # seleziona k elementi di L1
        sottolista1 = L1[i:i+k]
        # per ogni sottolista di L1, verifico ogni sottolista di L2
        # relazione dei loop: una sottolista di L1 - ogni sottolista di L2
        j=0
        while not esiste_sottolista_uguale and j<len(L2)-k+1:
            sottolista2 = L2[j:j+k]
            if hanno_sottoliste_uguali(sottolista1, sottolista2):
                # hai trovato due sottoliste uguali, quindi ritorna subito vero
                return True
            j += 1
    # se dopo aver comparato tutte le sottoliste di L1 ed L2 non ne esiste nessuna uguale, allora ritorna falso
    if not esiste_sottolista_uguale:
        return False



L1 = [1, 2, 3, 7, 3, 5, 3]
L2 = [8, 7, 3, 5, 4]
k = 3

print(verifica_liste(L1,L2,k))
