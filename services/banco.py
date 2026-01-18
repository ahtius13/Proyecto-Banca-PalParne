# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# banco.py Este archivo contiene las funciones relacionadas con las operaciones bancarias. Aquí se maneja el saldo del usuario.



def consultar_saldo(usuario): #  Muestra el saldo actual del usuario.
    """
   

    Parámetro:
    - usuario: objeto de tipo Usuario
    """

    print(f"Su saldo actual es: {usuario.saldo} euros.")


def ingresar_dinero(usuario, cantidad):
    """
    Ingresa dinero en la cuenta del usuario.

    Parámetros:
    - usuario: objeto Usuario
    - cantidad: cantidad de dinero a ingresar
    """

    # Comprobamos que la cantidad sea válida
    if cantidad <= 0:
        print("La cantidad a ingresar debe ser mayor que 0.")
        return

    # Sumamos la cantidad al saldo
    usuario.saldo += cantidad

    print(f"Ingreso realizado correctamente.")
    print(f"Nuevo saldo: {usuario.saldo} euros.")


def retirar_dinero(usuario, cantidad):
    """
    Retira dinero de la cuenta del usuario.

    Parámetros:
    - usuario: objeto Usuario
    - cantidad: cantidad de dinero a retirar
    """

    # Validamos la cantidad
    if cantidad <= 0:
        print("La cantidad a retirar debe ser mayor que 0.")
        return

    # Comprobamos si hay saldo suficiente
    if cantidad > usuario.saldo:
        print("Fondos insuficientes.")
        return

    # Restamos la cantidad del saldo
    usuario.saldo -= cantidad

    print("Retiro realizado correctamente.")
    print(f"Saldo actual: {usuario.saldo} euros.")


def transferir_dinero(usuario, cantidad, cuenta_destino):
    """
    Transfiere dinero desde la cuenta del usuario a otra cuenta.

    Parámetros:
    - usuario: objeto Usuario
    - cantidad: cantidad de dinero a transferir
    - cuenta_destino: número o identificador de la cuenta destino
    """

    # Validamos la cantidad
    if cantidad <= 0:
        print("La cantidad a transferir debe ser mayor que 0.")
        return

    # Comprobamos si hay saldo suficiente
    if cantidad > usuario.saldo:
        print("Fondos insuficientes para realizar la transferencia.")
        return

    # Restamos la cantidad del saldo
    usuario.saldo -= cantidad

    print(f"Transferencia realizada correctamente a la cuenta {cuenta_destino}.")
    print(f"Saldo restante: {usuario.saldo} euros.")
