# MenuPrincipal.py
# Este archivo contiene el menú principal del sistema bancario

# FUNCIÓN QUE MUESTRA EL MENÚ_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

import random
import math

saldo = 100
registro_gastos = []

# FUNCIÓN PRINCIPAL DEL MENÚ_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def mostrar_menu():
    
    print(" BANCO PALPARNÉ ")
    
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Enviar dinero")
    print("5. Registrar gasto")
    print("6. Ver gastos")
    print("7. Media de gastos")
    print("0. Salir")

def consultar_saldo():
    
    print(f"Saldo actual: {saldo} €")

def ingresar_dinero():
    
    global saldo
    cantidad = int(input("Cantidad a ingresar: "))
    
    if cantidad > 0:
        
        saldo += cantidad
        
        print("Ingreso realizado.")
        
    else:
        
        print("Cantidad no válida.")

def retirar_dinero():
    
    global saldo
    
    cantidad = int(input("Cantidad a retirar: "))
    
    if 0 < cantidad <= saldo:
        
        saldo -= cantidad
        
        registro_gastos.append(cantidad)
        
        print("Retiro realizado.")
        
    else:
        
        print("Fondos insuficientes.")

def enviar_dinero():
    
    global saldo
    
    cantidad = int(input("Cantidad a enviar: "))
    
    if cantidad <= saldo:
        
        codigo = random.randint(1000, 9999)
        
        print(f"Código de confirmación: {codigo}")
        
        confirmar = int(input("Introduce el código: "))
        
        if confirmar == codigo:
            
            saldo -= cantidad
            
            print("Transferencia realizada.")
            
        else:
            
            print("Código incorrecto.")
            
    else:
        
        print("Saldo insuficiente.")

def registrar_gasto():
    
    gasto = int(input("Importe del gasto: "))
    
    if gasto > 0:
        
        registro_gastos.append(gasto)
        
        print("Gasto registrado.")

def mostrar_gastos():
    
    if not registro_gastos:
        
        print("No hay gastos.")
        
    else:
        
        print("Gastos:", registro_gastos)

def media_gastos():
    
    if registro_gastos:
        
        media = math.fsum(registro_gastos) / len(registro_gastos)
        
        print(f"Media de gastos: {media:.2f} €")
        
    else:
        
        print("No hay gastos registrados.")

def menu_principal():

continuar = "si"

    while True and continuar.lower() == "si":
        
        mostrar_menu()
        
        opcion = input("Opción: ")

        if opcion == "1":
            
            consultar_saldo()
            
        elif opcion == "2":
            
            ingresar_dinero()
            
        elif opcion == "3":
            
            retirar_dinero()
            
        elif opcion == "4":
            
            enviar_dinero()
            
        elif opcion == "5":
            
            registrar_gasto()
            
        elif opcion == "6":
            
            mostrar_gastos()
            
        elif opcion == "7":
            
            media_gastos()
            
        elif opcion == "0":
            
            print("Sesión cerrada.")
            
            break
            
        else:
            
            continuar = input("\n¿Desea realizar otra consulta? (si/no): ")

            print("Opción no válida.")
