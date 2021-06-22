#Distintos tipos de modulos

#Modulos propios
import fmath #Archivo creado por mi con dunciones dentro

fmath.add(123, 321)
fmath.substract(321, 123)
    #Para importar de forma as especifica
from fmath import add, substract
add(123, 321)
substract(321, 123)

#Modulos de las bibliotecas de python (python modules index)
import datetime #Importar modulo para consultar la hora

print(datetime.date.today()) #Consultar el dia actual
print(datetime.timedelta(minutes = 100)) #Convertir minutos en horas

    #Para importar de forma mas especifica
from datetime import date, timedelta
print(date.today())
print(timedelta(minutes = 100))

#Modulos que podemos descargar (pip modules)

    #Se instalan por comandos en la terminal "pip install..."