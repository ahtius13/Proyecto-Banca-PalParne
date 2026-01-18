# IngresarDinero.py

# Este archivo permite al usuario ingresar dinero en su cuenta.

# 1. FUNCIÓN PARA INGRESAR DINERO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def ingresar_dinero():

    global saldo  # Usamos la variable saldo global

    # Pedimos la cantidad a ingresar

    cantidad = int(input("Introduce la cantidad que deseas ingresar: "))

    # Comprobamos que la cantidad sea válida

    if cantidad > 0:

        saldo += cantidad  # Sumamos el dinero al saldo

        print("\nIngreso realizado correctamente.")

        print("Tu nuevo saldo es:", saldo, "euros\n")

    else:

        print("\nLa cantidad debe ser mayor que 0.\n")
   
# 2. MENÚ PRINCIPAL_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def menu_principal():

    while True:

        print("MENÚ PRINCIPAL")

        print("1. Consultar saldo")

        print("2. Ingresar dinero")

        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            print("\nTu saldo actual es:", saldo, "euros\n")

        elif opcion == "2":

            ingresar_dinero()

            # Al terminar, vuelve automáticamente al menú

        elif opcion == "0":

            print("Saliendo del programa...")

            break

        else:
            print("Opción no válida\n")