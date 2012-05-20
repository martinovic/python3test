#!/usr/bin/python
# -*- coding: utf-8 -*-

from test1 import tamanio_aproximado
print(tamanio_aproximado(tamanio=1000000000, un_kilobyte_es_1024_bytes=False))
print(tamanio_aproximado(tamanio=1000000000, un_kilobyte_es_1024_bytes=True))
