#Operatori di confronto. Tutti gli operatori producono dei boolean
# equal, not equal, less than, greater than ecc ecc
import random


x = 5
y = 30

print( x == y )
print (x != y )  #Not equal
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

if x > y:
    print("La variabile x è maggiore di y")
else :
    print("La variabile x è minore di y")

f = 10
g = 10

if x == y:
    print("I due numeri sono uguali")
else:
    print("I numeri sono diversi tra loro")

parola = "Ciao"
saluto = "Ciao"

if parola == saluto:
    print("le due stringhe sono identiche")

lunghezzaParola = len(parola) #estrae la lunghezza di una stringa
lunghezzaSaluto = len(saluto)


#OPERATORI LOGICI
#and - or - not
punteggio = 18
voto = 25

#Gioco: per poter superare l'esame il punteggio deve essere > 25 e il voto > 20
if (punteggio >= 25 and voto >= 20):
    print("Bravo, hai superato l'esame con i seguenti risultati:")
    print(punteggio, " punteggio")
    print(voto, " voto")
elif (punteggio < 25 and voto >= 20):
    print("Il tuo punteggio è sotto la soglia. Non hai superato l'esame")
elif (punteggio >=25 and voto < 20):
    print("Il tuo voto è sotto la soglia. Non hai superato l'esame")
else:
    print("Mi spiace, non hai superato l'esame. Entrambi i risultati sono sotto la soglia")

#Versione Easy: basta che uno dei due sia sopra la soglia e l'esame si passa
print("----EASY MODE----")

if(punteggio >= 25 or voto >= 20):
    print("Bravo, hai superato l'esame con i seguenti risultati:")
    print(punteggio, " punteggio")
    print(voto, " voto")
else:
    print("Fai schifo, se non ci riesci manco adesso...ahahahhahaha")

