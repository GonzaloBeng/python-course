# Tipo de dato que permite almacenar cualquier tipo de dato
# Permite identificar cada elemento con una Key

# Ejemplo de un producto
product = {
    "name": "Book",
    "quantity": 3,
    "price": 4.99
}

# Ejemplo de un diccionario de personas
person = {
    "name": "Gonzalo",
    "last_name": "Beng"

}

print(type(product))
print(type(person))

# Que puede hacerse con un diccionario
print(dir(person))

# Metodos
print(person.keys())  # Obtiene las Keys del diccionario
# Obtiene los items con cada Key del diccionario en una tupla
print(person.items())

# Borrar el contenido de un diccionario
person.clear()

# Borrar un diccionario entero
del person

# Los diccionarios pueden estar dentro de una lista
products = [
    {"name": "Book", "price": 3.99},
    {"name": "Laptop", "price": 499.99},
    {"name": "Car", "price": 7999.99},
]

print(products)
