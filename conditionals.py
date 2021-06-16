# Se pueden usar muchos simbolos para hacer comparaciones
2 < 3  # Menor
2 > 3  # Mayor
2 == 2  # Se utiliza == para preguntar si es "Igual a"

# Ejemplo de varible y comparacion

x = 40
if x < 30:  # El if y el : funcionan como "Si x < 30 entonces..."
    print("x is less than 30")
else:  # "SINO"
    print("x is greater than 30")

# Tambien puede hacerse con un string
color = "Blue"

if color == "blue":  # OJO las mayusculas
    print("The color is Blue")
else:
    print("Any color except Blue")

color = "blue"

if color == "red":
    print("The color is red")
elif color == "Blue":  # Sirve para hacer una comparacion adicional
    print("The color is blue")
else:
    print("Any color except red and blue")

# Ejemplo de un usuario
name = "John"
last_name = "Johnson"

if name == "John":
    if last_name == "Johnson":
        print("You are John Johnson")
    else:
        print("You are not John Johnson")
else:
    print("You are not John Johnson")

# Example with a pasta recipe

# Ingredients
egg = 2
flour_gr = 200
olive_oil_ml = 10

if egg >= 2:
    print("You have enough eggs")
    if flour_gr >= 200:
        print("You have enough flour")
        if olive_oil_ml >= 10:
            print("You have all the ingredients. Let's Cook!!")
        else:
            print("You have to buy olive oil")
    else:
        print("You have to buy flour")
else:
    print("You have to buy eggs")


# Comprobar que un numero esta entre dos numeros
x = 8

if 2 < x and x < 10:  # Con una de las dos opciones es suficiente
    print("X es mayor a 2 Y menor que 10")
if 2 < x or x < 10:  # Ambas son necesarias que ocurran
    print("X es menor a 2 O mayor a 10")
if (not(x == 5)):  # Para negacion
    print("X no es igual a 5")
