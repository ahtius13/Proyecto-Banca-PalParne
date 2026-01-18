# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# login.py Este archivo gestiona el registro y el inicio de sesión de los usuarios. _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

import random                       # Se usa para generar el código de seguridad _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

from models.usuario import Usuario  # Importamos la clase Usuario _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


# Diccionario donde se guardarán los usuarios registrados La clave será el nombre de usuario _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# El valor será otro diccionario con contraseña y objeto Usuario _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

usuarios = {}

# Tipos de cuenta disponibles _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

tipos_disponibles = ["joven", "jubilado", "empresa", "ong"]

# Función para registrar un nuevo usuario. Pide nombre, contraseña y tipo de cuenta. _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def registrar_usuario():
    
    print("\--- REGISTRO DE USUARIO ---")

    nombre = input(" Usuario: ")

# Comprobamos si el usuario ya existe _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    if nombre in usuarios:

        print("Este usuario ya existe.")

        return

    contrasena = input("Contraseña: ")

    print("Tipos de cuenta disponibles:", tipos_disponibles)

    tipo = input("Tipo de cuenta: ")

# Validamos el tipo de cuenta _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    if tipo not in tipos_disponibles:

        print("Tipo de cuenta no válido.")

        return

# Creamos el objeto Usuario _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    usuario = Usuario(nombre, tipo)

# Guardamos el usuario en el diccionario _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    usuarios[nombre] = {

        "password": contrasena,

        "usuario": usuario

    }

    print("Usuario registrado correctamente.\n")

# Genera un código de seguridad de 4 cifras y lo compara con el introducido por el usuario. _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def codigo_seguridad():
  
    codigo = random.randint(1000, 9999)

    print(f"Código enviado: {codigo}")

    entrada = input("Introduce el código: ")

    return entrada == str(codigo)

# Función para iniciar sesión. Devuelve el objeto Usuario si el login es correcto. Devuelve None si falla. _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def iniciar_sesion():

    print("\--- INICIO DE SESIÓN ---")

    nombre = input("Usuario: ")

    contrasena = input("Contraseña: ")

# Comprobamos si el usuario existe _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    if nombre in usuarios:

# Comprobamos la contraseña _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        if usuarios[nombre]["password"] == contrasena:

# Comprobamos el código de seguridad _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

            if codigo_seguridad():

                print("Acceso permitido.\n")

                return usuarios[nombre]["usuario"]

    print("Acceso denegado.\n")

    return None

# Función principal del sistema de autenticación. Muestra el menú de login y redirige al menú principal. _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def loggin():

    from ui.menu import menu_principal

    while True:

        print("1. Registrarse")

        print("2. Iniciar sesión")

        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            registrar_usuario()

        elif opcion == "2":

            usuario = iniciar_sesion()

# Si el login es correcto, entramos al menú principal _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

            if usuario:

                menu_principal(usuario)

                break

        elif opcion == "0":

            print("Saliendo...")

            break

        else:

            print("Opción no válida.\n")

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _