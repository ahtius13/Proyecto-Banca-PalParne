----------------------------------------------------------------------------------

# Proyecto-Banca-PalParne

Proyecto-Banca-PalParne es una aplicación sencilla desarrollada en Python
que simula el funcionamiento básico de un banco.

Este proyecto ha sido creado como práctica para aprender y reforzar
conceptos básicos de Python como:
- funciones
- módulos
- condicionales
- bucles
- organización de archivos

----------------------------------------------------------------------------------

# ¿Qué permite hacer esta aplicación?

Con esta aplicación el usuario puede:

- Registrarse e iniciar sesión
- Consultar el saldo de su cuenta
- Ingresar dinero
- Retirar dinero
- Transferir dinero a otra cuenta
- Registrar gastos personales
- Ver el listado de gastos
- Calcular la media de los gastos

----------------------------------------------------------------------------------

# ¿Cómo ejecutar el programa?

1. Abre una terminal o PowerShell
2. Accede a la carpeta del proyecto
3. Ejecuta el archivo principal con el siguiente comando:

----------------------------------------------------------------------------------

python main.py
```
Proyecto-Banca-PalParne/
│
├── main.py                 # Archivo principal del programa
├── README.md               # Documentación del proyecto
│
├── auth/                   # Gestión de autenticación
│   └── login.py            # Registro e inicio de sesión
│
├── models/                 # Modelos de datos
│   └── usuario.py          # Clase Usuario
│
├── services/               # Lógica del negocio
│   ├── banco.py            # Operaciones bancarias
│   └── gastos.py           # Gestión de gastos
│
└── ui/                     # Interfaz de usuario
    └── menu.py             # Menú principal
```

----------------------------------------------------------------------------------

# EXPLICACIÓN POR SECCIONES (igual que con `main.py`)

# 🔹 Título y descripción
Explica **qué es el proyecto** y **para qué sirve**.

----------------------------------------------------------------------------------

# 🔹 Funcionalidades
Lista clara de lo que el programa puede hacer.

 Importante para profesores y compañeros.

----------------------------------------------------------------------------------

# 🔹 Ejecución
Deja claro:
- qué archivo se ejecuta
- cómo se ejecuta
- sin confusión

----------------------------------------------------------------------------------

### 🔹 Estructura
Muy importante:
- demuestra que sabes organizar un proyecto
- ayuda a entender el código rápido

----------------------------------------------------------------------------------

### 🔹 Notas importantes
Evita errores comunes:
- ejecutar archivos incorrectos
- tocar módulos internos

----------------------------------------------------------------------------------

### 🔹 Objetivo
Demuestra que el proyecto **tiene intención educativa**, no solo código.

----------------------------------------------------------------------------------

# ¿POR QUÉ ESTE README ESTÁ BIEN?

º Claro  
º Ordenado  
º No tiene errores de Git  
º No menciona archivos que no existen  
º Nivel perfecto para clase  
º Profesional sin ser complejo  

----------------------------------------------------------------------------------

# SIGUIENTE PASO

El siguiente archivo **en la jerarquía lógica** es:

**`models/usuario.py`**

Es el **corazón del proyecto**, donde vive:
- el saldo
- los gastos
- el tipo de cuenta

Dime:

- **“seguimos con usuario”** 

o  

- si quieres cambiar algo del README

Y continuamos paso a paso

----------------------------------------------------------------------------------
