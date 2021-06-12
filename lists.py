# Distintas formas de declarar una lista
# Puede tener varios tipos de variables
demo_list = [11, "Blue", 3, "Green", [1, 2, 3]]
colors = ["Blue", "Green", "Red", "Orange", "Yellow"]

# Se usa una tupla en un comando list() para crear una
numbers_list = list((1, 2, 3, 4))
print(numbers_list)
print(type(numbers_list))

# Rango permite crear listas de un punto a otro
r = list(range(0, 10))
s = list(range(0, 11))  # Siempre termina un numero antes del declarado
print(r)
print(s)

print(dir(colors))  # Me muestra todas las acciones que puedo hacer con la lista
print(type(colors))  # Me dice que tipo de variable es general

# Me dice que tipo de variable es en esa posicion especifica
print(type(colors[0]))

# Consultar si algo especifico esta en la list
print("Green" in colors)  # True
print("green" in colors)  # False (ojo las mayusculas)
print("violet" in colors)  # False


# Como cambiar una variable del arreglo
print(colors)
colors[0] = colors[4]
colors[1] = colors[3]
colors[3] = "Green"
colors[4] = "Blue"  # Buscar la forma de invertir sin que la cronologia me afecte

print(colors)


# Metodos

colors.append("Violet")  # Permite agregar al final un elemento

# Para agregar mas de un elemento, siempre dentro de una tupla () o list []
colors.extend(("Brown", "Gray"))
print(colors)
colors.extend(["Black", "Pink"])
print(colors)

# Agregar un elemento en una posicion en especifico
colors.insert(1, "White")
print(colors)
# Otra forma de insentar un elemento al final del array
colors.insert(len(colors), "Grape")
print(colors)

# Quitar el ultimo elemento o por indice
colors.pop()
colors.pop(2)
print(colors)

# Quitar un elemento en especifico
colors.remove("Green")
print(colors)

# Limpiar una list
# colors.clear()
# print(colors)

# Ordenamiento de una list
colors.sort()  # Alfabeticamente
print(colors)

colors.sort(reverse=True)  # Alfabeticamente inverso
print(colors)

# Obtener indice de un elemento
print(colors.index("Gray"))
# Cuantas veces esta el elemento en el arreglo
print(colors.count("Blue"))
