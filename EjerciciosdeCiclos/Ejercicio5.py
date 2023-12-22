class Palabra:
    # Método constructor
    def __init__(self, palabra):
        self.palabra = palabra

    def ingresarpalabra(self):
        # metodo para ingresar la palabra 
        self.palabra = input("Ingrese una palabra: ")

    def mostrar(self):
        for i in range(1, 11):
            print(self.palabra)

# Crear una instancia de la clase Palabra
palabra = Palabra("")
palabra.ingresarpalabra()

# Llamar al método para mostrar
palabra.mostrar()