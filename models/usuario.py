# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# models/usuario.py Define la clase Usuario. _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# ESTE ARCHIVO NO DEBE PEDIR DATOS POR INPUT. _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# Clase que representa a un usuario del banco. _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

class Usuario:


    def __init__(self, nombre, tipo_cuenta):

        self.nombre = nombre            # Nombre del usuario

        self.tipo_cuenta = tipo_cuenta  # Tipo de cuenta

        self.saldo = 100.0              # Saldo inicial

        self.gastos = []                # Lista de gastos

    # MÉTODOS DE INFORMACIÓN _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    def mostrar_datos(self):

        print("\n--- DATOS DEL USUARIO ---")

        print(f"Usuario: {self.nombre}")

        print(f"Tipo de cuenta: {self.tipo_cuenta}")

        print(f"Saldo: {self.saldo} €")

    # OPERACIONES BANCARIAS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    def ingresar(self, cantidad):

        if cantidad > 0:

            self.saldo += cantidad

            print(f"Ingreso correcto. Saldo actual: {self.saldo} €")

        else:

            print("Cantidad no válida.")

    def retirar(self, cantidad):

        if cantidad <= 0:

            print("Cantidad no válida.")

        elif cantidad > self.saldo:

            print("Saldo insuficiente.")

        else:

            self.saldo -= cantidad

            print(f"Retiro correcto. Saldo actual: {self.saldo} €")

    # GASTOS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    def registrar_gasto(self, descripcion, monto):

        if monto > 0 and monto <= self.saldo:

            self.saldo -= monto

            self.gastos.append((descripcion, monto))

            print(f"Gasto registrado. Saldo actual: {self.saldo} €")

        else:

            print("No se pudo registrar el gasto.")
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

