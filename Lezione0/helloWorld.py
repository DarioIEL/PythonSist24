#Questo è un commento in python
print("Hello, World. Questo è il mio primo file in python")

#Dichiarazione e assegnamento variabili
nome = "Dario" #String
cognome = "Mennillo" #String
eta = 35  #int
lavoro="Docente"
presenza = True #boolean
pi = 3.14 #float

# Stampo queste info richiamando le variabili
#Sto utilizzando , per concatenare le variabili
print("ciao, \nmi chiamo", nome, cognome, eta, "anni")

#Utilizzo + come operatore di concatenzione per stringhe e solo per stringhe
presentazione = nome + " " + cognome + " " + lavoro + " ho " + str(eta)  +" anni"
print(presentazione)

#Cast del dato, ovvero forza un tipo specifico per una variabile
numero1 = 10
#Cast della variabile da numero -> String
numero1stringa = str(numero1);
#Posso anche verificare il type della variabile
print("La variabile numero1 è di tipo ", type(numero1), "e vale", numero1)
print("La variabile numero1stringa è di tipo ", type(numero1stringa), "e vale", numero1stringa)


numero2 = "123" #string
numero3 = "20" #string

somma2 = numero2 + numero3
# Att: questa è una somma tra stringhe
print("Il risultato della somma vale: " + somma2 ) #12320

#Cast del dato
somma = int(numero2) + int(numero3)
print("Il risultato della somma vale: ", somma); #143


#Esempio prima dichiaro poi leggo poi riassegno
oraDelGiorno = 15
oraDelGiorno = 16
oraDelGiorno = 18

print("Adesso sono le ore", oraDelGiorno)

oraDelGiorno = 19

print("Aedsso sono le ", oraDelGiorno)



