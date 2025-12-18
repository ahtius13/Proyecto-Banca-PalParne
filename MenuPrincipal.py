# ===== MENÚ PRINCIPAL =====

saldo = 100  # saldo inicial
registro_gastos = []

def mostrar_menu():
    print("\n===== MENÚ BANCARIO =====")
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


# ===== BUCLE PRINCIPAL =====
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        consultar_saldo(saldo)

    elif opcion == "2":
        saldo = ingresar_dinero(saldo)

    elif opcion == "3":
        saldo = retirar_dinero(saldo)

    elif opcion == "4":
        saldo = transferir_dinero(saldo)

    elif opcion == "5":
        registrar_gasto()

    elif opcion == "6":
        mostrar_gastos()

    elif opcion == "7":
        calcular_media_gastos()

    elif opcion == "0":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")