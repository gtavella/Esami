
# Si scriva una funzione verifica_liste che riceve due liste L1 ed L2 di interi e un intero k e restituisce True se e solo se L1
# contiene una sottolista di lunghezza k i cui elementi sono presenti in L2 nello stesso ordine (anche se in posizioni non
# consecutive).
# Esempio: Se L1 = [3, 1, 2, 5, 7, 3, 5, 3], L2 = [8, 1, 7, 4, 2, 6, 3, 5, 4] e k = 3, allora la funzione restituisce True perché la
# lista L1 contiene la sottolista [1, 2, 5] i cui elementi sono presenti in L2 nello stesso ordine.


def verifica_liste(L1, L2, k):
    # ultimo indice di L2 in cui hai trovato lo stesso numero in L1
    # inizializza -1 perche' ogni volta aggiungiamo 1, quindi indice parte da 0
    # e noi vogliamo che parta da 0, cioe' proprio dall'inizio
    last_i = -1
    # quanti match consecutivi hai trovato in L1 che esistono in L2 in modo non consecutivo
    n_matches = 0
    matches = []

    for i in range(len(L1)):
        # numero attuale
        l1 = L1[i]
        L2_right =  L2[last_i+1:]
        # il numero attuale esiste in L2, partendo dall'indice in cui hai trovato l'ultimo match?
        is_match_right = l1 in L2_right
        print(f'{l1} in {L2_right}? {is_match_right}')

        if is_match_right:
            # partendo da dove hai trovato l'ultimo match, ottieni l'indice dell'attuale match
            # che diventera' il nuovo ultimo indice
            last_i = L2.index(l1, last_i+1)
            matches.append(l1)
            n_matches += 1
            if n_matches == k: return True
        # altrimenti resetta l'ultimo indice (cioe' parti dall'inizio)
        # resetta il numero di match, vuol dire che si ricomincia a contare da capo
        # se non c'e' un match nella sottolista, e' probabile che ci sia partendo dall'inizio

        else:
            L2_left = L2[0:last_i]
            # se questo numero non e' nella sottolista di L2, allora prendi l'altra sottolista dall'inizio
            is_match_left = l1 in L2_left
            i_match_left = L2.index(l1, 0, last_i)
            print(f'..ma {l1} in {L2[:last_i]}')
            # se c'e' un match adesso, allora parti da qui

            # if is_match_left and i_match_left > last_i:
            #     last_i = i_match_left
            #     matches.append(l1)
            #     n_matches = 1
            #     if n_matches == k: return True
            # # altrimenti ricomincia veramente da 0
            # else:
            #     last_i = -1
            #     n_matches = 0
            last_i = -1
            n_matches = 0
        print('\n')

        # print(matches)
    return False







L1 = [3, 1, 2, 5, 7, 3, 5, 3]
L2 = [8, 1, 7, 4, 2, 6, 3, 5, 4]
k = 3

print( verifica_liste(L1, L2, k) )







# # SOTTOLISTA di L1: 1, 2, 5
# # EXPECTED OUTPUT: True
# L1 = [3, 1, 2, 5, 7, 3, 5, 3]
# L2 = [8, 1, 7, 4, 2, 6, 3, 5, 4]
# k = 3
#
# # SOTTOLISTA di L1: 9, 7, 5
# # EXPECTED OUTPUT: False
# # L1 = [6, 2, 9, 7, 5, 4, 7, 0]
# # L2 = [5, 9, 3, 7, 3, 1, 5]
# # k = 4
#
# # SOTTOLISTA di L1: 9, 7, 5
# # EXPECTED OUTPUT: True
# # L1 = [6, 2, 9, 7, 5, 4, 7, 0]
# # L2 = [5, 9, 3, 7, 3, 1, 5]
# # k = 3
#
#
# # SOTTOLISTA di L1: 7, 9
# # EXPECTED OUTPUT: False
# # L1 = [1, 5, 6, 0, 7, 9, 3, 4]
# # L2 = [7, 5, 7, 9, 1]
# # k = 3
#
#
# # SOTTOLISTA di L1: 7, 9
# # EXPECTED OUTPUT: True
# # L1 = [1, 5, 6, 0, 7, 9, 3, 4]
# # L2 = [7, 5, 7, 9, 1]
# # k = 2
#
#
# # L1 = [5, 6, 9, 4, 8]
# # L2 = [3, 6, 1]
# # k = 3
#
# print( verifica_lista(L1, L2, k) )
