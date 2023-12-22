class NumPos:

# Atributo de clase

    numero = int(input("Ingrese un número: "))
 
  # Método para validar si el numero es mayor que cero o menor 
 
    def validar(self):
         
        if  100 <= self.numero <=999 and self.numero>0:
          print(" numero positivo y mayor o igual a tres cifras ", self.numero)
        else : 
                 
         print("El número es negativo o menor a tres cifras", self.numero)

# Crear una instancia de la clase numPos
NumeroPositivo= NumPos()

# Llamar al método para mostrar
NumeroPositivo.validar() 
