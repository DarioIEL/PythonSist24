# Parliamo di Array. Sono dei contenitori di elementi simili tra loro, vuol dire che sono tutti dello stesso tipo

# Creo un Array vuoto. Creo una List vuota
my_list = [] # con le [] definisco gli array o liste

#Creo una lista di cose
numbers = [1,2,5,4,7,8,1,1,0] #int[]
words = ["Ciao", "Come", "Stai", "Bene", "Grazie", "Dario"] #string[]

#Posso anche fare un array misto  però NO
mixed_list = [5, True, "Ciao", "Pippo", 32, False]
person = ["Dario", "Mennillo", 35, True]

#Gli Array sono 0-based, vuol dire che la conta parte da 0
#indice       0        1         2        3        4
studenti = ["Beppe", "Andrea", "Salvo", "Sara", "Giulia"]
#calcolo la lunghezza dell'array
studentiLength = len(studenti) #5 --- len = length

print("In classe ci sono " + str(len(studenti)) + " studenti")
print("In clasee ci sono", studentiLength, "studenti")

print(studenti) #molto brutto da vedere

# Per poter leggere singolarmente i nomi degli studenti utilizzo un forLoop, ciclo For in

for x in studenti:
    print(x)

amici = ["Flic", "Floc", "Flac", "Teresa"]

for x in amici:
    print("Primo", x)
    print("Secondo",x)