#!/usr/bin/python3
import sys
'''
Prueba de uso de lambda
La primera prueba crea una lambda donde obtiene la raiz cuadrada de un valor
deretminado.
'''
print(sys.version)
print("\n")
print("-" * 80)
x = lambda x: x ** 2

print(x(3), end=" ")

'''
Esta otra prueba crea una lista de la valores usando lambda y el metodo de
ternarios
'''

listado = [x(e) for e in range(1, 10)]

print(listado)

'''
Esto hace un listado con los valores mayores a 20 del listado
'''
lista_filtrada = [x for x in listado if x > 20]

print(lista_filtrada)
