#!/usr/bin/python3
# -*- coding: utf-8 *-*
'''
Esto es para aprender a usar los argumentos que se le pasan a una funcion
*args es una lista de parametros 1,2,3
*kwargs es un lista con keywords a=1, b=2, c=3
'''


def saludo(*args, **kwargs):
    for r in args:
        print(r)

    for k in kwargs:
        print(k, " - ", kwargs[k])

saludo(primera="aa", segunda="bb")
