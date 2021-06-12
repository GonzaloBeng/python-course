# Tipos de numeros

print(type(2))  # Entero o integer
print(type(2.0))  # Flotante o float
print(2 + 2.0)  # Pueden sumarse entre ambos pero siempre devuelve un float
print(type(2 + 2.0))  # Ejemplo

print(2 ** 3)  # Para hacer calculos exponenciales se usa **

print(3 % 2)  # El operador % te permite obtener el resto de la division

# Como pedir que el usuario inserte un numero
# Input pide el ingreso, age determina el nombre de la variable
age = input("Insert your age:")
print(f"Your age is {age}")

# Todo lo que recibe un input es un string
# Puedo convertirlo en un numero si es lo que necesito
new_age = int(age) + 4
print(f"In four years you will have {new_age} years")
old_age = int(age) - 4
print(f"Your age was {old_age} four years ago")
