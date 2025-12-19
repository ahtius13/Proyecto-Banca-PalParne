# Lista donde se guardarán los gastos
registro_gastos = []

def registrar_gasto(monto, descripcion):
    # Guarda un gasto en la lista
    gasto = [monto, descripcion]
    registro_gastos.append(gasto)
    print("Gasto registrado.")

def calcular_media_gastos():
    # Calcula la media de los gastos
    if len(registro_gastos) == 0:
        print("No hay gastos registrados.")
    else:
        # sumamos solo los montos (primer elemento de cada gasto)
        suma = 0
        for gasto in registro_gastos:
            suma += gasto[0]
        
        media = suma / len(registro_gastos)
        print("La media de gastos es:", media)

def mostrar_gastos():
    # Muestra todos los gastos guardados
    if len(registro_gastos) == 0:
        print("No hay gastos registrados.")
    else:
        print("Registro de gastos:")
        for gasto in registro_gastos:
            print(gasto)
