class Primoparimp:

    def __init__(self):
        self.numero = int(input("Ingrese un número: "))

    def es_primo(self):
        if self.numero < 2:
            return False
        for i in range(2, int(self.numero**0.5) + 1):
            if self.numero % i == 0:
                return False
        return True

    def es_par_impar(self):
        if self.numero % 2 == 0:
            return "par"
        else:
            return "impar"

    def analizar_numero(self):
        if self.es_primo():
            print(f"{self.numero} es primo.")
        else:
            print(f"{self.numero} no es primo.")

        par_impar = self.es_par_impar()
        print(f"{self.numero} es {par_impar}.")

# Crear una instancia de la clase Primoparimp
number = Primoparimp()

# Llamar al método para analizar el número
number.analizar_numero()
