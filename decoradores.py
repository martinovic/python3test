#!/usr/bin/python3
# -*- coding: utf-8 *-*
'''
Esto es para aprender a usar los decoradores.
'''


def decorador_avisar(f):
    def inner(*args, **kwargs):
        f(*args, **kwargs)
        print("Se ha ejecutado la funcion: %s" % f.__name__)
        print("%i" % args[0])
    return inner


@decorador_avisar
def primera_def(i):
    print("Hola soy la primera def")


@decorador_avisar
def segunda_def(i):
    print("Hola soy la segunda def")


primera_def(1)

segunda_def(0)
