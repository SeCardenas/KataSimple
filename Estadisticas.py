
class Estadisticas:
    def dar_estadisticas(self, cadena):
        if cadena=="":
            return [0,0,0]
        elif "," in cadena:
            numeros = cadena.split(",")
            minimo = int(numeros[0])
            maximo = int(numeros[0])
            for numero in numeros:
                minimo = min(int(numero),minimo)
                maximo = max(int(numero),maximo)
            return [len(numeros), minimo, maximo]
        else:
            return [1,int(cadena), int(cadena)]
