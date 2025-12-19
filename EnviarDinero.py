
#Consultar Saldo, Enviar Saldo,, Ingresar Saldo, Retirar Saldo, 

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