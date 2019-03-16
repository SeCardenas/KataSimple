
class Estadisticas:
    def dar_estadisticas(self, cadena):
        if cadena=="":
            return [0]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros)]
        else:
            return [1]
