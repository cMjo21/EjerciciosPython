from math import isqrt

class NumeroPerfecto:
    # Atributo de clase
    numero = int(input("Ingrese un número: "))

    # Método para validar si el número es perfecto
    def validar(self):
        suma_divisores = 1

        for i in range(2, isqrt(self.numero) + 1):
            if self.numero % i == 0:
                suma_divisores += i
                otro_divisor = self.numero // i
                if i != otro_divisor:
                    suma_divisores += otro_divisor

        es_perfecto = suma_divisores == self.numero
        if es_perfecto:
            print("El número es un número perfecto.")
        else:
            print("El número no es un número perfecto.")

# Crear una instancia de la clase NumeroPerfecto
numero_perfecto = NumeroPerfecto()

# Llamar al método para mostrar
numero_perfecto.validar()
