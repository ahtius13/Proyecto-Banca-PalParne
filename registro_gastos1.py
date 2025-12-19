# Lista donde se guardarán los gastos
registro_gastos = []

def registrar_gasto(monto, descripcion):
    # Crea un gasto y lo guarda en la lista
    gasto = [monto, descripcion]
    registro_gastos.append(gasto)
    print("Gasto registrado.")

def mostrar_gastos():
    # Muestra todos los gastos guardados
    if len(registro_gastos) == 0:
        print("No hay gastos registrados.")
    else:
        print("Registro de gastos:")
        for gasto in registro_gastos:
            print(gasto)
