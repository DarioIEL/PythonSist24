# Funzioni di ordine superiore 
def applicaFunzione(funzione, valore):
    """
    Commento Multiline
    Questa funzione usa un'altra funzione come parametro in ingresso
    e un valore 
    """
    risultato = funzione(valore)
    return risultato


def raddoppia(numero):
    return numero * 2

def triplica(numero):
    return numero * 3

# Nel richiamare la funzione come parametro non utilizzo le () 
risultato1 = applicaFunzione(raddoppia, 7)
print(risultato1)

risultato2 = applicaFunzione(triplica,7)
print(risultato2)


