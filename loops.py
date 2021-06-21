foods = ['apples', 'bread', 'cheese', 'milk']

#Forma que funciona pero poco eficiente
#print(foods[0])
#print(foods[1])
#print(foods[2])
#print(foods[3])

#Haciendo lo mismo con LOOP
for food in foods: #Bucle "Para"
    if food == 'cheese': #pueden agregarse condicionales dentro
        break #Se puede romper el ciclo del bucle
    print(food)

for food in foods:
    if food == 'cheese':
        continue #Se puede dar continuacion a un bucle
    print(food)

#Se puede recorrer un rango
for number in range(1,8):
    print(number)

#Iterar un string
for letter in 'Hello':
    print(letter)

#Bucle while o "Mientras"
count = 4

while count <= 10:
    print(count)
    count = count + 1 #Si no agrego esto caigo en un bucle infinito PRECAUCION