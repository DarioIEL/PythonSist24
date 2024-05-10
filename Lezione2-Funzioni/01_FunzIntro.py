# Definisco una funzione senza parametri, senza argomenti
def saluta():
    print("Ciao, come stai ?")
    print("Tutto bene, grazie")

# Per poter eseguire il codice nella funzione la devo richiamare
saluta()

# Dichiaro una funzione con parametro
def saluta_nome(nomePersona):
    print("Ciao", nomePersona)

# Adesso che richiamo saluta_nome devo per forza passare il parametro
saluta_nome("Dario")
saluta_nome(42)
saluta_nome(False)

def sommaNumeri(a,b):
    somma = a+b
    return somma

print("Il risultato finale", sommaNumeri(6,7))

risultato = sommaNumeri(5,789.9)
print("Il secondo risultatto è:", risultato)


# Creo una funzione con doppio valore restituito
def calcolaOperazioni(a,b):
    somma = a+b
    differenza = a-b
    moltiplicazione = a*b
    divisione = a/b
    return somma, differenza, divisione, moltiplicazione

num1 = int( input("Inserisci un numero"))
num2 = int( input("Inserisci un numero"))

risultatoSomma, risultatoDiff, risultatoDiv, risultatoMolt = calcolaOperazioni(num1,num2)

# risultatoSomma, risultatoDiff, risultatoDiv, risultatoMolt = calcolaOperazioni(50,24)
print("La somma vale",risultatoSomma)
print("La differenza vale", risultatoDiff)
print("Il prodotto vale", risultatoMolt)
print("IL quoziente vale", risultatoDiv)