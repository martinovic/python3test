#!/usr/bin/python3
# -*- coding: utf-8 *-*
'''
Documenacion de test1
'''
SUBFIJOS = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
        1024: ['KiB', 'MiB', 'GiB', 'TiB ', 'PiB', 'EiB', 'ZiB', 'YiB']}


def tamanio_aproximado(tamanio, un_kilobyte_es_1024_bytes=True):
    '''
    documentacion
    '''
    if tamanio < 0:
        raise ValueError('El numero no puede ser negativo')

    multiplo = 1024 if un_kilobyte_es_1024_bytes else 1000
    for sufijo in SUBFIJOS[multiplo]:
        tamanio /= multiplo
        if tamanio < multiplo:
            return '{0:.1f}{1}'.format(tamanio, sufijo)

    raise ValueError('El numero es muy grande')


#if __name__ == '__main__':
#    print(tamanio_aproximado(tamanio=1000000000,
#                un_kilobyte_es_1024_bytes=False))
#    print(tamanio_aproximado(1000000000))
