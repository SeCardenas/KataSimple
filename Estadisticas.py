
class Estadisticas:
    def dar_estadisticas(self, cadena):
        if cadena=="":
            return [0,0,0,0]
        elif "," in cadena:
            numeros = cadena.split(",")
            suma=0.0
            minimo = int(numeros[0])
            maximo = int(numeros[0])
            for numero in numeros:
                minimo = min(int(numero),minimo)
                maximo = max(int(numero),maximo)
                suma=suma+int(numero)
            return [len(numeros), minimo, maximo, suma/len(numeros)]
        else:
            return [1,int(cadena), int(cadena), int(cadena)]
