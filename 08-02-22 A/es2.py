# Si scriva una funzione verifica_lista che riceve in ingresso una lista L di stringhe ed un intero k.
# Si assuma che la lista L abbia lunghezza maggiore di k. La funzione restituisce True se e solo se ogni stringa di L avente k
# stringhe successive non ha lettere in comune con tali stringhe.
# Esempio: Se L=['abcd', 'efgh', 'ijk', 'ab', 'cdef'], allora verifica_lista(L,2) restituisce True perche':
# 'abcd' non ha lettere in comune con 'efgh' 'ijk'
# 'efgh' non ha lettere in comune con 'ijk' e 'ab'
# 'ijk' non ha lettere in comune con 'ab' e 'cdef'


# itera fino alla lunghezza di L meno k elementi
# itera su tutte le lettere della stringa attuale
# per ogni lettera, itera sulla sottolista composta dalle prossime k stringhe di L
# se in questa sottolista c'e' almeno una stringa che contiene la lettera attuale, ritorna falso


def esiste_lettera_in_stringhe(l,stringhe):
    for stringa in stringhe:
        # se la lettera della stringa attuale esiste in un'altra prossima stringa 
        if l in stringa:
            return True
    return False


def verifica_lista(L,k):
    # itera fino alla lunghezza di L meno k
    for i in range(len(L)-k):
        # per ogni lettera della stringa attuale
        prossime_stringhe = L[i + 1:i + k + 1]
        # L[i] e' la stringa attuale, testiamo che ogni lettera di questa stringa non esiste in tutte le altre stringhe
        for l in L[i]:
            # seleziona la sottolista composta da i prossimi k elementi
            if esiste_lettera_in_stringhe(l, prossime_stringhe):
                return False
    # vuol dire che non c'e' nessuna lettera in comune tra l'attuale stringa e le prossime stringhe
    return True


L=['abcd', 'efgh', 'ijk', 'ab', 'cdef']
print(verifica_lista(L,2))
