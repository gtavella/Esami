# Si scriva una funzione verifica_lista che riceve in ingresso una lista L di stringhe ed un intero k.
# Si assuma che la lista L abbia lunghezza maggiore di k. La funzione restituisce True se e solo se ogni stringa di L avente k
# stringhe precedenti ha almeno una lettera in comune con tali stringhe.
# Esempio: Se L=['abcd', 'efgh', 'abe', 'af', 'bef'], allora verifica_lista(L,2) restituisce True perche':
# 'abe' ha almeno una lettera in comune sia con 'abcd' che con 'efgh'
# 'af' ha almeno una lettera in comune sia con 'efgh' che con 'abe'
# 'bef' ha almeno una lettera in comune sia con 'abe' che con 'af'



def verifica_lista(L,k):
    # parti dall'inizio piu' k
    # itero per ogni stringa campione, cioe' quella di cui voglio verificare le lettere
    for i in range(k, len(L)):
        # la stringa di cui vado a verificare tutte le lettere
        stringa_campione = L[i]
        # tutte le altre stringhe che vado a testare
        stringhe_target = L[i-k:i]
        # itero per ogni stringa target
        # per ogni stringa target, esiste almeno una lettera in comune con una lettera della stringa campione?
        for stringa_target in stringhe_target:
            # riaggiorno ad ogni nuova stringa target
            esiste_lettera = False
            # inizializzo, lo uso per iterare su ogni lettera della stringa campione
            j = 0
            # itero per ogni lettera della stringa campione
            while not esiste_lettera and j<len(stringa_campione):
                # ogni lettera della stringa campione
                l = stringa_campione[j]
                # se esiste almeno una lettera nella stringa target, questo mi basta,
                # puoi uscire dal while loop e passare alla prossima stringa target
                if l in stringa_target:
                    # esco dal loop perche' ho trovato almeno una lettera in comune in questa stringa target,
                    # quindi passa alla prossima stringa target
                    esiste_lettera = True
                j += 1
            # solo dopo il while loop, cioe' dopo che ho testato ogni lettera della stringa campione contro una stringa target
            # (una alla volta), posso dire per certo se c'era almeno una lettera in comune
            # se non c'era nessuna lettera in comune, allora ritorna falso
            if not esiste_lettera:
                return False
    # condizione richiesta dalla traccia soddisfatta
    return True


L=['abcd', 'efgh', 'abe', 'af', 'bef']
print(verifica_lista(L,2))
