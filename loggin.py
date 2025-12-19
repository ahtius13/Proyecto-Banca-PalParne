# loggin.py
# Controla el registro y el inicio de sesión de los usuarios

import random  # Para generar códigos de seguridad

# LISTAS DE USUARIOS_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

usuarios = []

contrasenas = []

tipos_cuenta = []

tipos_disponibles = ["joven", "jubilado", "empresa", "ong"]


# REGISTRO DE USUARIO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def registrar_usuario():
  
    print("REGISTRO DE USUARIO")

    usuario = input("Introduce un nombre de usuario: ")

    if usuario in usuarios:
       
        print("Este usuario ya existe.")
       
        return

    contrasena = input("Introduce una contraseña: ")

    print("Tipos de cuenta disponibles:", tipos_disponibles)
 
    tipo = input("Elige tu tipo de cuenta: ")

    if tipo not in tipos_disponibles:
      
        print("Tipo de cuenta no válido.")
     
        return

  
    usuarios.append(usuario)
   
    contrasenas.append(contrasena)
   
    tipos_cuenta.append(tipo)

    print("Usuario registrado correctamente.")
    
# CÓDIGO DE SEGURIDAD_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def codigo_seguridad():
    
    codigo = random.randint(1000, 9999)
   
    print(f"Código de seguridad enviado: {codigo}")

    codigo_usuario = input("Introduce el código recibido: ")

    if codigo_usuario == str(codigo):
      
        print("Código correcto.")
       
        return True
    else:
       
        print("Código incorrecto.")
       
        return False

# INICIO DE SESIÓN_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def iniciar_sesion():
    
    print("\nINICIO DE SESIÓN")

    usuario = input("Usuario: ")
    
    contrasena = input("Contraseña: ")

    if usuario in usuarios:
      
        indice = usuarios.index(usuario)

        if contrasenas[indice] == contrasena:
           
            print("Usuario y contraseña correctos.")

            if codigo_seguridad():
             
                return True
            else:
             
                return False
        else:
            print("Contraseña incorrecta.")
          
            return False
    else:
        print("Usuario no encontrado.")
       
        return False


# FUNCIÓN PRINCIPAL DE LOGIN_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def loggin():
   
    while True:
        
        print("\n1. Registrarse")
        
        print("2. Iniciar sesión")
       
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            
            registrar_usuario()

        elif opcion == "2":
           
            if iniciar_sesion():
                
                print("Acceso permitido.")

#  AQUÍ ES DONDE SE ENTRA AL MENÚ PRINCIPAL_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
                
                from MenuPrincipal import menu_principal
                
                menu_principal()

                break
            else:
                
                print("Acceso denegado.")

        elif opcion == "0":
            
            print("Saliendo del sistema.")
            
            break

        else:
            
            print("Opción no válida.")


# Este archivo controla el registro y el inicio de sesión de los usuarios

import random  # Para generar códigos de seguridad

# 1. LISTAS PARA GUARDAR DATOS DE USUARIOS_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __

import random

usuarios = []
contrasenas = []
tipos_cuenta = []

tipos_disponibles = ["joven", "jubilado", "empresa", "ong"]


def registrar_usuario():

    print("\nREGISTRO DE USUARIO")

    usuario = input("Usuario: ")

    if usuario in usuarios:

        print("Este usuario ya existe.")

        return

    contrasena = input("Contraseña: ")

    print("Tipos de cuenta:", tipos_disponibles)

    tipo = input("Tipo de cuenta: ")

    if tipo not in tipos_disponibles:

        print("Tipo no válido.")

        return

    usuarios.append(usuario)

    contrasenas.append(contrasena)

    tipos_cuenta.append(tipo)

    print("Usuario registrado correctamente.\n")


def codigo_seguridad():

    codigo = random.randint(1000, 9999)

    print(f"Código enviado: {codigo}")
    
    entrada = input("Introduce el código: ")

    return entrada == str(codigo)


def iniciar_sesion():
    print("\nINICIO DE SESIÓN")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario in usuarios:
        i = usuarios.index(usuario)
        if contrasenas[i] == contrasena:
            if codigo_seguridad():
                return True
    print("Acceso denegado.")
    return False


def loggin():
    while True:
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            if iniciar_sesion():
                print("\nAcceso permitido.\n")
                from menu_principal import menu_principal
                menu_principal()
                break

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

     
