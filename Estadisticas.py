
class Estadisticas:
    def dar_estadisticas(self, cadena):
        if cadena=="":
            return [0,0]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros), min(int(numeros[0]), int(numeros[1]))]
        else:
            return [1,int(cadena)]
