# ================================ ================================ ================================ ================================
# ARCHIVO PRINCIPAL DEL PROGRAMA ARCHIVO PRINCIPAL DEL PROGRAMA ARCHIVO PRINCIPAL DEL PROGRAMA ARCHIVO PRINCIPAL DEL PROGRAMA
# ================================ ================================ ================================ ================================

# Esta línea importa la función Loggin del menú desde el archivo Loggin.py

from loggin import loggin

# Esta condición especial sirve para indicar que este archivo es el que se va a ejecutar
# directamente desde la terminal con: python main.py Si este archivo se importa desde otro archivo,
# el código que está dentro NO se ejecutará

if __name__ == "__main__":

    # Aquí llamamos a la función principal del menú Esta función es la que muestra las opciones
    # al usuario (consultar saldo, ingresar dinero, etc.) A partir de aquí empieza todo el programa
    loggin()
