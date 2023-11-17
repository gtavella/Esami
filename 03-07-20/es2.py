# Si scriva una funzione verifica_liste che riceve due liste L1 ed L2 di interi e un intero k e restituisce True se e solo se L1
# contiene una sottolista di lunghezza k i cui elementi sono presenti in L2 nello stesso ordine (anche se in posizioni non
# consecutive).
# Esempio: Se L1 = [3, 1, 2, 5, 7, 3, 5, 3], L2 = [8, 1, 7, 4, 2, 6, 3, 5, 4] e k = 3, allora la funzione restituisce True perché la
# lista L1 contiene la sottolista [1, 2, 5] i cui elementi sono presenti in L2 nello stesso ordine.



def verifica_liste(l1,l2,k):
    # itera dall'inizio e fermati all'inizio dell'ultima sottolista
    for i in range(len(l1)-k+1):
        # seleziona sottoliste di k elementi ciascuna
        # poi controllale una per una
        if sottolista_trovata(l1[i:i+k],l2):
            return True
    # se nessuna sottolista di k elementi di l1 contiene elementi non consecutivi (ma con indice crescente) in l2
    return False


def sottolista_trovata(l_target,l2):
    j=0
    matches=[]
    # per ogni elemento in l1
    for elem in l_target:
        trovato=False
        # itera su l2 finche' non hai trovato un match
        while not trovato and j<len(l2):
            # se l'elemento attuale di l1 matcha un elemento di l2
            # (cioe' se l'elemento generico di l1 esiste in l2)
            if elem==l2[j]:
                matches.append(elem)
                # significa che esci dal loop perche' hai trovato il match
                trovato=True
            j+=1
        # se non hai trovato un match dopo aver iterato tutto l2, allora l'elemento non esiste in l2
        if not trovato:
            return False
    print(matches)
    # hai trovato una sottolista (quindi elementi consecutivi) di l1
    # i cui elementi non sono necessariamente consecutivi in l2 (quindi con indice crescente in l2)
    return True



L1 = [3, 1, 2, 5, 7, 3, 5, 3]
L2 = [8, 1, 7, 4, 2, 6, 3, 5, 4]
k = 3

print( verifica_liste(L1, L2, k) )
