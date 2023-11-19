# Si scriva una funzione f che riceve in ingresso due liste L1 ed L2 di stringhe e restituisce una lista che contiene gli
# elementi di L1 ed L2 in ordine crescente, senza elementi duplicati. La funzione non deve utilizzare la funzione sort
# della libreria standard.
# Esempio: Se L1=[‘albero’, ‘mare’, ‘zebra’, ‘casa’] ed L2=[‘zebra’, ‘albero’, ‘barca’, ‘verde’, ‘abaco’], allora la funzione
# restituisce la lista [‘abaco’, ‘albero’, ‘barca’, ‘casa’, ‘mare’, ‘verde’, ‘zebra’].


# unisci L1 e L2 in una lista
# scrivi funzione che rimuove duplicati
# scrivi funzione che ordina in ordine crescente


# rimuovere duplicati significa che ogni elemento di L
# ci puo' essere una sola volta nella lista degli unici
def rimuovi_duplicati(L):
    unici = []
    for x in L:
        # se il generico elemento di L non c'e' nella lista degli unici
        if x not in unici:
            unici.append(x)
    return unici


# riceve in input una lista di elementi distinti (cioe' unici)
def ordina_crescente(L):
    risultato = []

    # funzione ricorsiva
    def trova_piu_piccola(lista):
        # quando non c'e' piu' nessun elemento
        if len(lista) == 0:
            return risultato
        stringa_piu_piccola = lista[0]
        # indice dove hai trovato stringa piu' piccola
        k = 0
        for i in range(0, len(lista)):
            # se la stringa attuale e' piu' piccola dell'ultima piu' piccola
            if lista[i] < stringa_piu_piccola:
                # allora la stringa attuale e' quella piu' piccola finora
                stringa_piu_piccola = lista[i]
                # salva l'indice dove hai trovato la stringa piu' piccola
                # quindi la stringa piu' piccola si trova all'indice k
                k = i
        # dopo il loop, sappiamo per certo qual e' la stringa piu' piccola e il suo indice
        risultato.append(stringa_piu_piccola)
        # fai lo stesso ragionamento per la lista che risulta togliendo la stringa piu' piccola
        # cioe' trova la prossima stringa piu' piccola senza l'attuale stringa piu' piccola
        return trova_piu_piccola( lista[:k] + lista[k+1:] )

    return trova_piu_piccola(L)



def f(L1, L2):
    # L e' una lista che contiente tutti gli elementi distinti (cioe' unici) di L1 e L2
    return ordina_crescente( rimuovi_duplicati(L1 + L2) )





L1=['albero', 'mare', 'zebra', 'casa']
L2=['zebra', 'albero', 'barca', 'verde', 'abaco']

print(f(L1,L2))



