class TrianguloRectangulonum:
    def __init__(self):
        self.numero = int(input("Ingrese un número: "))

    def tabla(self):
        # Imprimir un triángulo rectángulo con el patrón específico
        for i in range(1, self.numero + 1):
            # Imprimir números en cada línea según el patrón
            for j in range(i, 0, -1):
                print(j, end='')
            # Cambiar de línea después de imprimir los números
            print()

# Crear una instancia de la clase TrianguloRectangulonum
triangulo = TrianguloRectangulonum()

# Llamar al método para imprimir el triángulo
triangulo.tabla()
