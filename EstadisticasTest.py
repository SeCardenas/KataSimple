import unittest

from Estadisticas import Estadisticas

class TestEstadisticas(unittest.TestCase):
    def test_dar_estadisticas(self):
        self.assertEqual(Estadisticas().dar_estadisticas("")[0], 0, "String vacio")

    def test_dar_estadiciticas_un_solo_numero(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1")[0], 1, "Un solo numero")

    def test_dar_estadiciticas_dos_numeros(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1,2")[0], 2, "Dos numeros")

    def test_dar_estadiciticas_n_numeros(self):
        self.assertEqual(Estadisticas().dar_estadisticas("1,2,4,3")[0], 4, "N numeros")
        self.assertEqual(Estadisticas().dar_estadisticas("1,2,7,5,6,1")[0], 6, "N numeros")