#Chiedi all'utente di fornirti 6 numeri. Successivamente estrai 6 numeri su un set di 90 e controlla.
#stampa una notifica tutte le volte che trova un numero uguale. Se sono 6 numeri uguali sei superlucky

numeri_utente = []

while(len(numeri_utente) < 6):
    numeroScelto =int( input("Inserisci un numero"))
    numeri_utente.append(numeroScelto);


    