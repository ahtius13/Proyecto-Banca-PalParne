# REGISTRO DE GASTOS 2 - NIVEL PRINCIPIANTE
# Creamos una lista vacía
# Aquí se guardarán todos los gastos que introduzca el usuario
# Cada gasto será una lista con:
# [cantidad_de_dinero, descripcion_del_gasto]

registro_gastos = []

# FUNCIÓN PARA REGISTRAR UN GASTO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def registrar_gasto(monto, descripcion):

    # Creamos una lista con el dinero y la descripción
    gasto = [monto, descripcion]

    # Añadimos el gasto a la lista de gastos
    registro_gastos.append(gasto)

    # Avisamos al usuario
    print("Gasto registrado correctamente.")

# FUNCIÓN PARA CALCULAR LA MEDIA DE LOS GASTOS_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def calcular_media_gastos():

    # Comprobamos si la lista está vacía
    
    if len(registro_gastos) == 0:
        
        print("No hay gastos registrados.")
        
    else:
        
        # Creamos una variable para sumar los gastos
        
        suma = 0

        # Recorremos la lista de gastos
        
        for gasto in registro_gastos:
            
            # gasto[0] es el dinero gastado
            
            suma = suma + gasto[0]

        # Calculamos la media
        
        media = suma / len(registro_gastos)

        # Mostramos el resultado
        
        print("La media de gastos es:", media)

# FUNCIÓN PARA MOSTRAR TODOS LOS GASTOS_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def mostrar_gastos():

    # Comprobamos si hay gastos
    
    if len(registro_gastos) == 0:
        
        print("No hay gastos registrados.")
        
    else:
        
        print("\n--- LISTA DE GASTOS ---")

        # Recorremos la lista de gastos
        
        for gasto in registro_gastos:
            
            # Mostramos cada gasto
            
            print("Monto:", gasto[0], "€ | Descripción:", gasto[1])

