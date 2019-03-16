
class Estadisticas:
    def dar_estadisticas(self, cadena):
        if cadena=="":
            return [0,0]
        elif "," in cadena:
            numeros = cadena.split(",")
            minimo = int(numeros[0])
            for numero in numeros:
                if minimo > int(numero):
                    minimo = int(numero)
            return [len(numeros), minimo]
        else:
            return [1,int(cadena)]
