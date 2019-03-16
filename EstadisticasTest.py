import unittest

from Estadisticas import Estadisticas

class TestEstadisticas(unittest.TestCase):
    def test_dar_estadisticas(self):
        self.assertEqual(Estadisticas().dar_estadisticas("")[0], 0, "String vacio")
