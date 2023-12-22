

import time
from datetime import datetime

class RelojTerminal:
    def mostrar_reloj(self):
        while True:
            tiempo_actual = datetime.now().strftime('%H:%M:%S %p')
            print(tiempo_actual, end='\r')  # La opción end='\r' imprime en la misma línea
            time.sleep(1)  # Pausa durante 1 segundo

if __name__ == "__main__":
    reloj_terminal = RelojTerminal()
    reloj_terminal.mostrar_reloj()
