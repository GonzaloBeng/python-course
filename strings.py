# String
myStr = "Hello World"

# Dir permite ver todo lo que se puede hacer con la variable
print(dir(myStr))

# Title y Upper

print(myStr.title())  # Mayus en la primera letra

print(myStr.upper())  # Todo en mayuscula
print(myStr.lower())  # Todo en minuscula
print(myStr.swapcase())  # Alterna mayus y minus
print(myStr.capitalize())  # Vuelve mayus solo la primera letra del texto
print(myStr.replace("Hello", "Goodbye"))  # Reemplaza una palabra por otra

# Los metodos se pueden anidar
print(myStr.replace("Hello", "Goodbye").upper())

print(myStr.count("l"))  # Permite contar cuantas veces se repite el caracter

print(myStr.startswith("Hola"))  # Permite consultar como arranca el string
print(myStr.startswith("World"))  # Permite consultar como termina el string

# Como dividir un string en una list
print(myStr.split())  # Basado en los " ".
print(myStr.split("l"))  # Tambien se puede separar por caracter

# Buscar un caracter en particular
print(myStr.find("o"))  # Devuelve la POSICION del caracter
# Para saber el tamaño completo del string
print(len(myStr))
# Buscar el indice de un caracter
print(myStr.index("r"))
# Para saber si es numerico o alfanumerico
print(myStr.isnumeric())
print(myStr.isalpha())

# Consultar posiciones especificas del string
print(myStr[7], myStr[3], myStr[4], myStr[8])
# Con los numeros negativos puedo hacerlo de modo inverso
print(myStr[-7], myStr[-2], myStr[-4], myStr[-3])

# Final: Texto y string en un solo print
print(myStr + "," + " my name is Gonzalo")
# El f determina que voy a unar una variable que se pone entre {}
print(f"{myStr}, my name is Gonzalo")
print("{0}, my name is Gonzalo".format(myStr))
