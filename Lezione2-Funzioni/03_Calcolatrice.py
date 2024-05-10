
def calcolatore(operazione, num1, num2):
    if(operazione == "+" or operazione == "-" or operazione == "*" or operazione =="/"):
       print("Ok, adesso calcolerò la tua operazione...")
       match operazione:
          case "+":
               somma(num1, num2)
          case "*":
               moltiplica(num1, num2)
          case "/":
               dividi(num1, num2)
          case "-":
               sottrai(num1, num2)
          case _:
               print("Operazione non riconosciuta")
    else:
        print("Mi spiace, non ho capito il comando")
    
    

def somma(num1, num2):
    print(num1+num2)

def sottrai(num1, num2):
    print( num1 - num2)

def moltiplica(num1, num2):
    print( num1 * num2)

def dividi(num1, num2):
    print( num1 / num2)



print("Benvenuto nel calcolatore, mi servono 2 numeri e una operazione")
num1 = float(input("Inserisci il primo numero:"))
num2 = float(input("Inserisci il secondo numero:"))
operazione = input("Quale operazione vuoi eseguire ? ")

calcolatore(operazione, num1, num2)

