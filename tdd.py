#!/usr/bin/python
# -*- coding: utf-8 *-*


import unittest
import Clase_testeo_tdd


class TesteaNumeros(unittest.TestCase):

    def test_verifica_suma(self):
        print("verifica la suma")
        self.assertEquals(Clase_testeo_tdd.suma_numeros(2, 2),
            4,
            "error no son iguales")

if __name__ == "__main__":
    unittest.main()
