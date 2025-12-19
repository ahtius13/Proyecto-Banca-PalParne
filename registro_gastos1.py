# REGISTRO DE GASTOS - NIVEL PRINCIPIANTE_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# Creamos una lista vacía donde se guardarán todos los gastos
# Cada gasto será una lista con dos datos:

# [dinero_gastado, descripcion_del_gasto]

registro_gastos = []

# FUNCIÓN PARA REGISTRAR UN GASTO _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def registrar_gasto(monto, descripcion):

    # Creamos una lista con el monto y la descripción
    gasto = [monto, descripcion]

    # Añadimos ese gasto a la lista de gastos
    registro_gastos.append(gasto)

    # Mostramos un mensaje para avisar al usuario
    print("Gasto registrado correctamente.")

# FUNCIÓN PARA MOSTRAR TODOS LOS GASTOS_ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _

def mostrar_gastos():
    
    # Comprobamos si la lista está vacía
    
    if len(registro_gastos) == 0:
        
        # Si no hay gastos
        
        print("No hay gastos registrados.")
        
    else:
        
        # Si hay gastos, los mostramos uno por uno
        
        print("\n--- LISTA DE GASTOS ---")
        

        # Recorremos la lista de gastos
        
        for gasto in registro_gastos:
            
            # gasto[0] es el dinero
            
            # gasto[1] es la descripción
            
            print("Monto:", gasto[0], "€ | Descripción:", gasto[1])


mostrar_gastos()
