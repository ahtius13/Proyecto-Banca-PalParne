import time   # para simular tiempo real
import math   # para redondear

print("=== SISTEMA DE CUENTAS Y DIVIDENDOS (NIVEL BÁSICO) ===")

# 1. Diccionario con tipos de cuenta (NO afectan al dividendo según tus nuevas reglas)
tipos_de_cuenta = {
    "joven": 0.02,       # ya no se usa para intereses
    "jubilado": 0.002,   # ya no se usa
    "empresa": 0.02,     # ya no se usa
    "ong": 0.002         # ya no se usa
}

# 2. Pedimos datos al usuario
nombre = input("Escribe tu nombre: ")

print("Tipos de cuenta disponibles: joven, jubilado, empresa, ong")
tipo = input("Escribe tu tipo de cuenta: ")

# 3. NUEVA REGLA: saldo base fijo de 100 €
saldo = 100.0
print("\nTu saldo inicial es 100€ por regla del sistema.")

# 4. NUEVA REGLA: dividendo fijo del 0.2% (0.002)
dividendo = 0.002

print("\nCada 5 segundos se aplicará un dividendo del 0.2%.\n")

# 5. Bucle que aplica dividendos sin preguntar meses
while True:
    time.sleep(5)   # para pruebas: 5 segundos (en la vida real sería 300 segundos)

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

