#Istanzio variabili 
nome = "Anna"
cognome = "Verdi"
password = "qwerty123"
eta = 30
altezza = 1.7

flagPass = False

print("Utente: " + nome + " " + cognome)
richiestaPass = input("Digita la pass per conoscere altre info: ")

if( richiestaPass == password):
    print("La password è corretta. Altre info: \n" +str(altezza) + " altezza \n" + str(eta) + " età")
    flagPass = True
else:
    print("Mi spiace, non puoi accedere")

print("Adesso verificheremo la tua età...")
nuovaEta = int( input("Devi digitare di nuovo la tua età") )

if(flagPass and nuovaEta >= 18 ):
    print("Bene, hai accesso a tutta la piattaforma")
elif(not flagPass and nuovaEta >= 18 ):
    print("Non puoi accedere perché la pass è sbagliata ma l'età è giusta")
elif(flagPass and nuovaEta < 18):
    print("Non puoi accedere poiché non sei abbastanza grande")
else:
    print("Password ed età sono sbagliate")





