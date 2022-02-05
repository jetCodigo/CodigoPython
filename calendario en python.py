#Ejemplo de calendario en python con la libreria calendar.

#Importacion de la libreria calendar
import calendar

#preguntar por el mes y el año

year = int(input('Por favor ingrese el año \n'))
month = int(input('Por favor ingrese el mes \n'))

print(calendar.month(year, month))
