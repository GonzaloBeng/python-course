# Set: Coleccion desordenada y sin indice

colors = {"Red", "Blue", "Green"}

print(type(colors))
print("Red" in colors)  # Consulta si un dato esta en el Set (Booleano)

# Agregar un dato
colors.add("Violet")  # Lo agrega de forma ramdom porque el Set no tiene indice
print(colors)

# Remover un dato
colors.remove("Red")
print(colors)

# Limpiar el Set
colors.clear()
print(colors)

# Eliminar el Set
del colors
