# Distintas formas de declarar una tupla
# Puede tener varios tipos de variables
# La tupla posee elementos que no cambian
demo_tupla = (11)
months = ("January", "February", "March", "April", "May")
# No reconoce como tupla, tienen que ser multiples elementos
print(type(demo_tupla))
print(type(months))

# Se usa una tupla en un comando tuple() para crear una
numbers_tupla = tuple((1, 2, 3, 4))
print(numbers_tupla)
print(type(numbers_tupla))

# Consultar una posicion en especifico de la tupla
print(months[3])

# BORRAR UNA TUPLA
del months
