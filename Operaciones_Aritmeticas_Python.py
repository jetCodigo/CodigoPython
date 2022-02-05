#Programa en python que realiza varias operaciones aritmeticas.

number_1 = float(input('Ingrese el primer numero \n'))
number_2 = float(input('Ingrese el segundo numero \n'))

#Suma de dos numeros
suma = number_1 + number_2

#Resta de dos numeros
resta = number_1 - number_2

#producto de dos numeros
multiplicacion = number_1 * number_2

#division de dos numeros
division = number_1 / number_2

print('la suma de {0} y {1} es {2} '.format(number_1,number_2,suma))
print('la resta de {0} y {1} es {2} '.format(number_1,number_2,resta))
print('la multiplicacion de {0} y {1} es {2} '.format(number_1,number_2,multiplicacion))
print('la division de {0} y {1} es {2} '.format(number_1,number_2,division))

