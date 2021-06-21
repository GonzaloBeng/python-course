
#El lenguaje ya trae sus propias funciones predeterminadas con las que trabaje
#Ejemplos
#print()
#dir()
#type()

#Tambien se puden crear funciones propias
def hello(name="Voldemort"): #El def define que es una funcion, lo proximo es el nombre que va a llevar. Los parentesis definen el parametro
   print('Hello ' + name) 


hello() #Para utilizarlas es necesario "Llamarlas"

#Funcion de suma
def add(numberOne = 0, numberTwo = 0):
    return numberOne + numberTwo


print(add(123, 321))

#   Funciones Lambda (funciones anonimas que toman un numero de argumentos pero solo pueden ser escritas utilizando una sola expresion)
add2 = lambda numberOne, numbreTwo: numberOne + numbreTwo

print(add2(345, 543))