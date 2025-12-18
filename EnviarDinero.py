# EnviarDinero.py
# Este archivo contiene funciones relacionadas con el dinero:
# consultar saldo, ingresar, retirar y transferir dinero

# ---------------------------------------- ---------------------------------------- ---------------------------------------- ----------------------------------------
# FUNCIÓN PARA CONSULTAR EL SALDO FUNCIÓN PARA CONSULTAR EL SALDO FUNCIÓN PARA CONSULTAR EL SALDO FUNCIÓN PARA CONSULTAR EL SALDO FUNCIÓN PARA CONSULTAR EL SALDO
# ---------------------------------------- ---------------------------------------- ---------------------------------------- ----------------------------------------

def consultar_saldo(saldo):
    
    # Muestra por pantalla el saldo actual del usuario
    print(f"Saldo actual es: {saldo} euros.")


# FUNCIÓN PARA INGRESAR DINERO----------------------------------------------------------------------------------------------------------------------------------------------------------------

def ingresar_dinero(saldo):
    
    # Pedimos al usuario la cantidad que quiere ingresar
    
    cantidad_ingreso = int(input("Cantidad de Ingresar: "))

    # Sumamos la cantidad ingresada al saldo actual
    
    saldo = saldo + cantidad_ingreso

    # Mostramos el nuevo saldo
    
    print(f"Has ingresado {cantidad_ingreso} euros.")
    
    print(f"Tu nuevo saldo es: {saldo} euros.")

    # Devolvemos el saldo actualizado
    
    return saldo

# FUNCIÓN PARA RETIRAR DINERO----------------------------------------------------------------------------------------------------------------------------------------------------------------


def retirar_dinero(saldo):
    
    # Pedimos la cantidad que el usuario quiere retirar
    
    cantidad_retiro = int(input("Cantidad desea retirar: "))

    # Comprobamos si hay suficiente saldo
    
    if cantidad_retiro > saldo:
        
        # Si no hay saldo suficiente, avisamos al usuario
        
        print("Fondos insuficientes. No se puede realizar la retirada.")
        
    else:
        
        # Si hay saldo suficiente, restamos la cantidad
        
        saldo = saldo - cantidad_retiro
        
        print(f"Ha retirado {cantidad_retiro} euros.")
        
        print(f"Su saldo actual es de {saldo} euros.")

    # Devolvemos el saldo
    
    return saldo

# FUNCIÓN PARA TRANSFERIR DINERO----------------------------------------------------------------------------------------------------------------------------------------------------------------

def transferir_dinero(saldo):
    
    # Pedimos la cantidad que se quiere transferir
    
    cantidad_transferencia = int(input("Cantidad desea transferir?: "))

    # Pedimos el número de cuenta destino
    cuenta_destino = input("Ingrese el número de cuenta destino: ")

    # Comprobamos si hay suficiente saldo
    
    if cantidad_transferencia > saldo:
        
        # Si no hay saldo suficiente, mostramos un mensaje de error
        
        print("Fondos insuficientes. No se puede realizar la transferencia.")
        
    else:
        
        # Si hay saldo suficiente, restamos la cantidad transferida
        
        saldo = saldo - cantidad_transferencia
        
        print(f"Ha transferido {cantidad_transferencia} euros a la cuenta {cuenta_destino}.")
        
        print(f"Su saldo actual es de {saldo} euros.")

    # Devolvemos el saldo actualizado
    
    return saldo
