import unittest

from Estadisticas import Estadisticas

class TestEstadisticas(unittest.TestCase):
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

    def test_dar_estadiciticas_string_vacio_minimo_maximo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("")[0], 0, "String vacio")
        self.assertEqual(Estadisticas().dar_estadisticas("")[1], 0, "Minimo")
        self.assertEqual(Estadisticas().dar_estadisticas("")[2], 0, "Maximo")

    def test_dar_estadiciticas_un_numero_maximo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1")[2], 1, "Maximo")
        self.assertEqual(Estadisticas().dar_estadisticas("2")[2], 2, "Maximo")

    def test_dar_estadiciticas_dos_numeros_maximo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1,5")[2], 5, "Maximo")
        self.assertEqual(Estadisticas().dar_estadisticas("2,6")[2], 6, "Maximo")

    def test_dar_estadiciticas_n_numeros_maximo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("3,4,6,9,6")[2], 9, "Maximo")
        self.assertEqual(Estadisticas().dar_estadisticas("7,3,5,2,1,4")[2], 7, "Maximo")

    def test_dar_estadiciticas_string_vacio_promedio(self):
        self.assertEqual(Estadisticas().dar_estadisticas("")[3], 0, "String vacio")
