import unittest

from Estadisticas import Estadisticas

class TestEstadisticas(unittest.TestCase):
    def test_dar_estadiciticas_un_solo_numero(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1")[0], 1, "Un solo numero")

    def test_dar_estadiciticas_dos_numeros(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1,2")[0], 2, "Dos numeros")

    def test_dar_estadiciticas_n_numeros(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1,2,4,3")[0], 4, "N numeros")
        self.assertEqual(Estadisticas().dar_estadisticas("1,2,7,5,6,1")[0], 6, "N numeros")

    def test_dar_estadiciticas_string_vacio_y_minimo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("")[0], 0, "String vacio")
        self.assertEqual(Estadisticas().dar_estadisticas("")[1], 0, "Minimo")

    def test_dar_estadiciticas_un_string_y_minimo(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1")[0], 1, "Un solo numero")
        self.assertEqual(Estadisticas().dar_estadisticas("1")[1], 1, "Minimo")
        self.assertEqual(Estadisticas().dar_estadisticas("2")[1], 2, "Minimo")

