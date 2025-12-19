# funciones.py
# Este archivo contiene funciones básicas para manejar el dinero
# consultar saldo, ingresar, retirar y transferir

# FUNCIÓN PARA CONSULTAR EL SALDO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ 

def consultar_saldo(saldo):
    
    # Muestra por pantalla el saldo actual
    
    print(f"Su saldo actual es: {saldo} euros.")

# FUNCIÓN PARA INGRESAR DINERO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def ingresar_dinero(saldo):
    
    # Pedimos al usuario la cantidad que quiere ingresar
    
    cantidad = int(input("Teclee la cantidad a ingresar: "))

    # Sumamos la cantidad al saldo
    
    saldo = saldo + cantidad

    # Mostramos el resultado
    
    print(f"Has ingresado {cantidad} euros.")
    
    print(f"Tu nuevo saldo es: {saldo} euros.")

    # Devolvemos el saldo actualizado
    
    return saldo


# FUNCIÓN PARA RETIRAR DINERO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def retirar_dinero(saldo):
    
    # Pedimos la cantidad que el usuario quiere retirar
    
    cantidad = int(input("¿Qué cantidad desea retirar?: "))

    # Comprobamos si hay saldo suficiente
    
    if cantidad > saldo:
        
        print("Fondos insuficientes.")
        
    else:
        saldo = saldo - cantidad
        
        print(f"Has retirado {cantidad} euros.")
        
        print(f"Tu saldo actual es de {saldo} euros.")

    # Devolvemos el saldo (modificado o no)
    
    return saldo

# FUNCIÓN PARA TRANSFERIR DINERO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def transferir_dinero(saldo):
    
    # Pedimos la cantidad a transferir
    
    cantidad = int(input("¿Qué cantidad desea transferir?: "))

    # Pedimos la cuenta de destino
    
    cuenta_destino = input("Introduce el número de cuenta destino: ")

    # Comprobamos si hay saldo suficiente
    
    if cantidad > saldo:
        
        print("Fondos insuficientes.")
        
    else:
        saldo = saldo - cantidad
        
        print(f"Has transferido {cantidad} euros a la cuenta {cuenta_destino}.")
        
        print(f"Tu saldo actual es de {saldo} euros.")

    # Devolvemos el saldo actualizado
    
    return saldo

import sys

def consultar_saldo(saldo):
  
    print(f"Su saldo actual es: {saldo} euros.")


def ingresar_dinero(saldo):
  
    cantidad_ingreso = input("Teclee la cantidad a ingresar: ")
    
    saldo = int(saldo) + int(cantidad_ingreso)
    
    print(f"Has ingresado {cantidad_ingreso} euros. Su nuevo saldo es: {saldo} euros.")
    return saldo

def retirar_dinero(saldo):
    cantidad_retiro = int(input("Que cantidad desea retirar: ")) 
    
    if cantidad_retiro > saldo:
      
        print("Fondos insuficientes")
        
    else:
      
        saldo = saldo - cantidad_retiro
        
        print(f"Ha retirado {cantidad_retiro}, su saldo actual es de {saldo}")
        
    return saldo

def transferir_dinero(saldo):
  
    cantidad_transferencia = int(input("Que cantidad desea transferir: ")) 
    
    cuenta_destino = input("Ingrese el número de cuenta destino: ")
    
    if cantidad_transferencia > saldo:
      
        print("Fondos insuficientes")
        
    else:
      
        saldo = saldo - cantidad_transferencia
        
        print(f"Ha transferido {cantidad_transferencia} a la cuenta {cuenta_destino}, su saldo actual es de {saldo}")
        
    return saldo
 
