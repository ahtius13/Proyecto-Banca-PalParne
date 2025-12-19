# Retirar Dinero.py
# Este archivo permite al usuario retirar dinero de su cuenta.

# 1. FUNCIÓN PARA RETIRAR DINERO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def retirar_dinero():

    global saldo  # Usamos la variable saldo global

    # Pedimos la cantidad a retirar

    cantidad = int(input("Introduce la cantidad que deseas retirar: "))

    # Comprobamos que la cantidad sea válida

    if cantidad <= 0:

        print("\nLa cantidad debe ser mayor que 0.\n")

    elif cantidad > saldo:

        print("\nFondos insuficientes. No tienes tanto dinero.\n")

    else:

        saldo -= cantidad  # Restamos el dinero del saldo

        print("\nRetiro realizado correctamente.")

        print("Tu saldo actual es:", saldo, "euros\n")

# 2. MENÚ PRINCIPAL

def menu_principal():
    while True:

        print("MENÚ PRINCIPAL")
        print("1. Consultar saldo")
        print("3. Retirar dinero")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nTu saldo actual es:", saldo, "euros\n")

        elif opcion == "2":
            cantidad = int(input("Cantidad a ingresar: "))
            if cantidad > 0:
                global saldo
                saldo += cantidad
                print("Ingreso realizado.\n")
            else:
                print("Cantidad inválida.\n")

        elif opcion == "3":
            retirar_dinero()
            # Al terminar, vuelve automáticamente al menú

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida\n")
