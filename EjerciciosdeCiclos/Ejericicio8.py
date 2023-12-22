import time 

class Tiempo:
    
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos 
        
    def conteoregresivo(self):
        tiempo_total = self.horas * 3600 + self.minutos * 60 + self.segundos
        
        while tiempo_total > 0:
            horas_actuales, remainder = divmod(tiempo_total, 3600)
            minutos_actuales, segundos_actuales = divmod(remainder, 60)
            print(f"{horas_actuales:02d}:{minutos_actuales:02d}:{segundos_actuales:02d}")
            time.sleep(1)  # Esperar 1 segundo
            tiempo_total -= 1

        print("¡Tiempo finalizado!")

# Crear una instancia de la clase Tiempo
tiempo = Tiempo(horas=2, minutos=30, segundos=15)
tiempo.conteoregresivo()
