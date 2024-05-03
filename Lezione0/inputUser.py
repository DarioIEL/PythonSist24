
#Chiediamo qualcosa al nostro utente
nome = input("Come ti chiami ?")
eta = input("Quanti anni hai ? ")

print("Ciao", nome, "hai", eta, "anni")

print("Vediamo se sei bravo in matematica con i numeri interi")
num1 = input("Inserisci un numero:")
num2 = input("Inserisci un secondo numero: ")

somma = int( num1 ) + int( num2 )
print("La somma vale: ", somma)

moltiplica = int(num1) * int(num2)
print("La moltiplicazione vale", moltiplica)


print("Adesso un po' di calcoli con numeri float..")
#Att: cast del dato all'ingresso
num3 = float( input("Dammi un numero, anche con la virgola: ") )
num4 = float( input("Dammi un altro numero, anche con la virgola: "))

somma = num3 + num4
prodotto = num3 * num4
differenza = num3 - num4
divisione =  num3 / num4
potenza = num3 ** num4
restoDellaDivisione = num3 % num4
divisioneIntera = num3 // num4

#Stampo tutti i risultati
print("Somma:", somma)
print("Prodotto:", prodotto)
print("Differenza:", differenza)
print("Divisone:", divisione)
print("Potenza:", potenza)
print("Resto della divisione:", restoDellaDivisione)
print("Divisione Intera:", divisioneIntera)

#Altri operatori matematici
x = 9
x += 1 # x = x + 1 operatore di autoincremento
x -= 5 # x = x - 5
x *= 2 # x = x * 2
x /= 3 # x = x / 3 
