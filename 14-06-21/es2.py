# Si scriva una funzione lettere_comuni che riceve in ingresso una lista L di stringhe e restituisce una lista che contiene
# le lettere presenti in tutte le stringhe in L (in qualsiasi ordine).
# Esempio: Se L=[‘abc', ‘bdecf', ‘cabe', ‘bcfeg'], allora la funzione restituisce la lista [‘b', ‘c'].


# la proprieta' "la lettera che e' presente in ogni stringa di una lista", significa che
# qualsiasi lettera di qualsiasi stringa in una lista, deve essere contenuta in tutte le altre stringhe della stessa lista
# questo per definizione di "ogni"
# quindi per semplicita' prendo la prima stringa della lista, e per dire che ogni altra stringa
# contiene almeno le lettere di questa prima stringa (scelta a caso) e quindi rispondere alla domanda,
# mi basta verificare che ogni altra stringa abbia all'interno tutte le lettere della stringa selezionata, cioe' la prima


def lettere_comuni(L):
    # la lista che conterra' tutte le lettere comuni
    matches = []
    # la mia stringa campione, scelta a caso
    # tutte le altre stringhe devono avere (almeno) ogni lettera di questa stringa
    # se ce ne hanno altre non ci interessa
    stringa_campione = L[0]
    # inizializzo ad 1 (cioe' comincio dal secondo elemento incluso della lista di stringhe)
    # perche' ho gia' selezionato il primo elemento
    # itera per ogni lettera nella stringa campione / selezionata
    for i in range(len(stringa_campione)):
        j = 1
        # ogni lettera della stringa campione che andremo a testare contro tutte le altre stringhe della lista
        lettera = stringa_campione[i]
        # per ogni lettera, sovrascrivo il valore di questa variabile, che poi mi permette di continuare o uscire dal while loop
        lettera_e_diversa = False
        # continua ad iterare finche' trovi che l'attuale lettera e' assente (cioe' non presente) in almeno un'altra stringa
        while not lettera_e_diversa and j<len(L):
            # L[j] e' la generica stringa che non e' mai quella campione
            if lettera not in L[j]:
                # cambiando il valore, usciamo dal while loop
                lettera_e_diversa = True
            j += 1
        # appena siamo usciti dal while loop (ma sempre per la stessa lettera, perche' siamo ancora nel for loop)
        # se tutte le altre stringhe contengono la lettera attuale, allora inseriscila nel risultato finale
        if not lettera_e_diversa:
            matches.append(lettera)
    return matches


L = ['abc', 'bdecf', 'cabe', 'bcfeg']
# L = ['abc', 'a', 'a', 'a']

print(lettere_comuni(L))
