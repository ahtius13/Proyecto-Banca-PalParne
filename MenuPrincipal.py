# MENÚ PRINCIPAL 

saldo = 100  # saldo inicial

registro_gastos = []

def mostrar_menu():

    print("\n MENÚ BANCARIO")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Transferir dinero")
    print("5. Registrar gasto")
    print("6. Mostrar gastos")
    print("7. Calcular media de gastos")
    print("0. Salir")


def consultar_saldo(saldo):
    print(f"Su saldo actual es: {saldo} €")


def ingresar_dinero(saldo):
    cantidad = int(input("Cantidad a ingresar: "))
    saldo += cantidad
    print(f"Ingreso realizado. Nuevo saldo: {saldo} €")
    return saldo


def retirar_dinero(saldo):
    cantidad = int(input("Cantidad a retirar: "))
    if cantidad > saldo:
        print("Fondos insuficientes")
    else:
        saldo -= cantidad
        print(f"Retiro realizado. Nuevo saldo: {saldo} €")
    return saldo


def transferir_dinero(saldo):
    cantidad = int(input("Cantidad a transferir: "))
    cuenta = input("Número de cuenta destino: ")
    if cantidad > saldo:
        print("Fondos insuficientes")
    else:
        saldo -= cantidad
        print(f"Transferencia a {cuenta} realizada. Saldo restante: {saldo} €")
    return saldo


def registrar_gasto():
    monto = int(input("Monto del gasto: "))
    descripcion = input("Descripción del gasto: ")
    registro_gastos.append([monto, descripcion])
    print("Gasto registrado correctamente.")


def mostrar_gastos():
    if not registro_gastos:
        print("No hay gastos registrados.")
    else:
        print("\n--- GASTOS ---")
        for gasto in registro_gastos:
            print(f"Monto: {gasto[0]} € | Descripción: {gasto[1]}")


def calcular_media_gastos():
    if not registro_gastos:
        print("No hay gastos registrados.")
    else:
        suma = sum(gasto[0] for gasto in registro_gastos)
        media = suma / len(registro_gastos)
        print(f"Media de gastos: {media:.2f} €")


# BUCLE PRINCIPAL

continuar = "si"



while continuar.lower() == "si":



        print("\nSeleccione una opción:")

        print("1. Consultar saldo")

        print("2. Ingresar dinero")

        print("3. Retirar dinero")

        print("4. Transferir dinero")

        print("5. Registrar gasto")

        print("6. Mostrar gastos")

        print("7. Calcular media de gastos")

        print("8. Salir")



        opcion = input("Ingrese el número de la opción deseada: ")



        if opcion == "1":

            print(f"Su saldo actual es: {saldo} euros.")



        elif opcion == "2":

            cantidad = int(input("Teclee la cantidad a ingresar: "))



            if cantidad <= 0:

                print("Ha introducido un importe en numeros negativos, porfavor introduzca un importe correcto")

            else:

                saldo += cantidad

                print(f"Has ingresado {cantidad} euros. Su nuevo saldo es: {saldo} euros.")



        elif opcion == "3":

            cantidad = int(input("¿Qué cantidad desea retirar?: "))



            if cantidad <= 0:

                print("Ha introducido un importe en numeros negativos, porfavor introduzca un importe correcto")

            elif cantidad > saldo:

                print("Fondos insuficientes.")

            else:

                saldo -= cantidad

                print(f"Ha retirado {cantidad} euros. Su saldo actual es: {saldo} euros.")



        elif opcion == "4":

            cantidad = int(input("Cantidad a transferir: "))

            cuenta = input("Número de cuenta destino: ")



            if cantidad <= 0:

                print("Ha introducido un importe en numeros negativos, porfavor introduzca un importe correcto")

            elif cantidad > saldo:

                print("Fondos insuficientes.")

            else:

                saldo -= cantidad

                print(f"Transferencia a {cuenta} realizada. Saldo restante: {saldo} euros.")



        elif opcion == "5":

            monto = int(input("Monto del gasto: "))



            if monto <= 0:

                print("Ha introducido un importe en numeros negativos, porfavor introduzca un importe correcto")

            else:

                descripcion = input("Descripción del gasto: ")

                registro_gastos.append([monto, descripcion])

                print("Gasto registrado correctamente.")



        elif opcion == "6":

            if not registro_gastos:

                print("No hay gastos registrados.")

            else:

                print("\n--- GASTOS ---")

                for gasto in registro_gastos:

                    print(f"Monto: {gasto[0]} euros | Descripción: {gasto[1]}")


        elif opcion == "7":

            if not registro_gastos:

                print("No hay gastos registrados.")

            else:

                suma = sum(gasto[0] for gasto in registro_gastos)

                media = suma / len(registro_gastos)

                print(f"Media de gastos: {media:.2f} euros")



        elif opcion == "8":

            print("Hasta pronto 👋")

            break



        else:

            print("Opción no válida.")



        continuar = input("\n¿Desea realizar otra consulta? (si/no): ")



print("Gracias por usar el cajero automático, vuelva pronto.")
