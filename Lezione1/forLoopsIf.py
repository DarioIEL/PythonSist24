colors = ["azzurro", "rosso", "verde", "viola", "rosa"]

print("Stampo solo con un indice", colors[0])

for c in colors:
    if (c == "verde"):
        break
    print(c)
    

for c in colors:
    if (c == "verde"):
        continue
    print(c)

# Range, elabora una lista di numeri
# Range (start, end, passo). Attenzione, end non viene incluso

for y in range(6):
    if y == 3:
        continue
    print(y)


print("Stampo un range da 3 a 18")
for t in range(3,18):
    print(t)

print("Stampo un range da 20 a 100 con passo 5")
for p in range(20, 100, 4):
    print(p)