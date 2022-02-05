#Programa en python para calcular el cubo de un numero.

number = float(input('Ingrese un numero \n'))

cube = number * number * number

print('El cubo del numero dado {0} es {1} '.format(number, cube))


#Programa en python para calcular el cubo de un numero ejemplo 2.

number = float(input('Ingrese un numero \n'))

cube = number**3

print('El cubo del numero dado {0} es {1} '.format(number, cube))

#Programa en python para calcular el cubo de un numero ejemplo 3 funciones.
def cube(num):
    return num**3

number = float(input('Ingrese un numero \n'))

cub = cube(number)
print('El cubo del numero dado {0} es {1} '.format(number, cub))
