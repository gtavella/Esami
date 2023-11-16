# Si	scriva	una	 funzione	azzera_duplicati che	riceve	una	lista	L1 di	interi positivi	e restituisce	una	lista	L2 della	stessa
# lunghezza	di	L1 tale	che, per	ogni	elemento	L1[i],
# • se	L1[i] non	ha	elementi	uguali che	lo	precedono,	allora	L2[i] dev’essere	uguale	a	L1[i];
# • altrimenti,	L2[i] dev’essere	pari	a	zero.
# Esempio:	Se	L1 =	[2,	1,	5,	2,	7,	5,	1,	9]	allora
# azzera_duplicati(L1) restituisce	la	lista	L2 =	[2,	1,	5,	0,	7,	0,	0,	9].



# M matrice
# x is current number 
# end is current index
def all_previous_different(M, x, curr_index):
    for i in range(curr_index):
        # if there's just one previous number equal to x
        if M[i] == x:
            return False    
    return True


def azzera_duplicati(L1):
    # inizializza lista nulla
    L2 = [0] * len(L1)
    # itera su L1
    for i in range(len(L1)):
        if all_previous_different(L1, L1[i], i):
            L2[i] = L1[i]
        else:
            L2[i] = 0
    return L2



L1 = [2, 1, 5, 2, 7, 5, 1, 9]

print( azzera_duplicati(L1) )
