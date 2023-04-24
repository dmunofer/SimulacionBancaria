import threading

saldo = 100  # Saldo inicial de la cuenta

class ProcesoIngreso(threading.Thread):
    def __init__(self, monto):
        threading.Thread.__init__(self)
        self.monto = monto

    def run(self):
        global saldo
        saldo += self.monto

class ProcesoRetiro(threading.Thread):
    def __init__(self, monto):
        threading.Thread.__init__(self)
        self.monto = monto

    def run(self):
        global saldo
        saldo -= self.monto

# Crear procesos de ingreso y retiro
procesos = []
for i in range(40):
    procesos.append(ProcesoIngreso(100))
for i in range(20):
    procesos.append(ProcesoIngreso(50))
for i in range(60):
    procesos.append(ProcesoIngreso(20))
for i in range(40):
    procesos.append(ProcesoRetiro(100))
for i in range(20):
    procesos.append(ProcesoRetiro(50))
for i in range(60):
    procesos.append(ProcesoRetiro(20))

# Ejecutar los procesos
for proceso in procesos:
    proceso.start()

# Esperar a que terminen todos los procesos
for proceso in procesos:
    proceso.join()

# Comprobar que el saldo final es el esperado
if saldo == 100:
    print("La simulación bancaria ha sido exitosa.")
else:
    print("La simulación bancaria ha fallado.")
