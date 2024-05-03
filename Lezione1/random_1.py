import random


#Genera un num casuale tra 1, 100
random_number = random.randint(1,100)
print(random_number)

#Genera un numero float tra 0 e 1
float_random = random.random()
print(float_random)

#Estrazione casuale da una lista
my_list = ["Mela", "Pera", "Pesca", "Banana"]
elemento_random = random.choice(my_list)
print(elemento_random)

#genera una lista di 10 numeri presi tra 1 e 100
numeri_10_aCaso = random.sample(range(1,101), 5)
print(numeri_10_aCaso)

#Voglio 6 numeri da giocare al lotto
num_6_aCaso = random.sample(range(1,91), 6)
print(num_6_aCaso)