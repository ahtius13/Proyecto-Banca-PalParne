# USUARIOS Y SISTEMA DE CUENTAS Y DIVIDENDOS

import time   # para simular tiempo
import math   # para los numeros entteros y decimales.

# 1. Diccionario con tipos de cuenta _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

tipos_de_cuenta = {
    
    "joven": 0.02,       
    "jubilado": 0.002,   
    "empresa": 0.02,     
    "ong": 0.002         
}

# 2. Pedimos datos al usuario _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

nombre = input("Escribe tu nombre: ")

print("Tipos de cuenta disponibles: joven, jubilado, empresa, ong")
tipo = input("Escribe tu tipo de cuenta: ")

# 3. Saldo base de 100 €_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

saldo = 100.0

print("Tu saldo es 100€.")

# 4. Dividendo fijo del 0.2%

dividendo = 0.002

print("Cada 5 segundos se aplicará un dividendo del 0.2%.")

# 5. Bucle que aplica dividendos sin preguntar meses _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

while True:

    time.sleep(5)   # 5 segundos

    # cálculo del dividendo

    incremento = saldo * dividendo
    incremento = round(incremento, 2)

    # suma al saldo

    saldo += incremento

    # mostramos cambios

    print("=== DIVIDENDO APLICADO ===")
    print("Usuario:", nombre)
    print("Tipo de cuenta:", tipo)
    print("Dividendo recibido:", incremento, "€")
    print("Saldo actualizado:", round(saldo, 2), "€")
    print("------------------------------")

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _