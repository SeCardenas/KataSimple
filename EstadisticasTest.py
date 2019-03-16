import unittest

from Estadisticas import Estadisticas

class TestEstadisticas(unittest.TestCase):
    def test_dar_estadiciticas_string_vacio_y_minimo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("")[0], 0, "String vacio")
        self.assertEqual(Estadisticas().dar_estadisticas("")[1], 0, "Minimo")

    def test_dar_estadiciticas_un_string_y_minimo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1")[0], 1, "Un solo numero")
        self.assertEqual(Estadisticas().dar_estadisticas("1")[1], 1, "Minimo")
        self.assertEqual(Estadisticas().dar_estadisticas("2")[1], 2, "Minimo")

    def test_dar_estadiciticas_dos_numeros_y_minimo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("3,5")[0], 2, "Dos")
        self.assertEqual(Estadisticas().dar_estadisticas("3,5")[1], 3, "Minimo")

    def test_dar_estadiciticas_n_numeros_y_minimo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("3,5,2,1")[0], 4, "Cuatro")
        self.assertEqual(Estadisticas().dar_estadisticas("3,5,2,1")[1], 1, "Minimo")