# MenuPrincipal.py
# Este archivo contiene el menú principal del sistema bancario

# FUNCIÓN QUE MUESTRA EL MENÚ_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def mostrar_menu():
    print("MENÚ BANCARIO")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Transferir dinero")
    print("5. Registrar gasto")
    print("6. Mostrar gastos")
    print("7. Calcular media de gastos")
    print("0. Salir")

# FUNCIÓN PRINCIPAL DEL MENÚ_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def MenuPrincipal():
    salir = False  # Controla cuándo salir del menú

    while not salir:
        mostrar_menu()  # Mostramos el menú

        opcion = input("Elige una opción: ")

        if opcion == "1":

            print("Has elegido: Consultar saldo")

        elif opcion == "2":
            print("Has elegido: Ingresar dinero")

        elif opcion == "3":
            print("Has elegido: Retirar dinero")

        elif opcion == "4":
            print("Has elegido: Transferir dinero")

        elif opcion == "5":
            print("Has elegido: Registrar gasto")

        elif opcion == "6":
            print("Has elegido: Mostrar gastos")

        elif opcion == "7":
            print("Has elegido: Calcular media de gastos")

        elif opcion == "0":
            print("Saliendo del sistema...")
            salir = True  # Salimos del menú

        else:
            print("Opción no válida. Intenta de nuevo.")