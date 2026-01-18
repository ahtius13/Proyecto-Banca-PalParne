# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# ui/menu.py Menú principal del sistema bancario PAL PARNE

# Este archivo SOLO contiene lógica de interfaz (inputs y prints)

# Trabaja con el objeto Usuario recibido desde el login

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def menu_principal(usuario): # Menú principal del sistema bancario. Recibe un objeto Usuario autenticado.

    salir = False

    print("\n==============================")

    print("BIENVENIDO A PAL PARNE")

    print("==============================")

    print(f"Usuario: {usuario.nombre}")

    print(f"Tipo de cuenta: {usuario.tipo_cuenta}")

    print("==============================")

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    while not salir:

        print("\nMENÚ BANCARIO")

        print("1. Consultar saldo")

        print("2. Ingresar dinero")

        print("3. Retirar dinero")

        print("4. Transferir dinero")

        print("5. Registrar gasto")

        print("6. Mostrar gastos")

        print("7. Calcular media de gastos")

        print("0. Salir")

        opcion = input("Elige una opción: ")

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        # OPCIÓN 1 - CONSULTAR SALDO _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        if opcion == "1":

            print(f"\nSaldo actual: {usuario.saldo} €")

        # OPCIÓN 2 - INGRESAR DINERO _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        elif opcion == "2":

            try:

                cantidad = float(input("Cantidad a ingresar: "))

                usuario.ingresar_dinero(cantidad)

            except ValueError:

                print("Cantidad no válida.")

        # OPCIÓN 3 - RETIRAR DINERO _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        elif opcion == "3":

            try:

                cantidad = float(input("Cantidad a retirar: "))

                usuario.retirar_dinero(cantidad)

            except ValueError:

                print("Cantidad no válida.")

        # OPCIÓN 4 - TRANSFERENCIA _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        elif opcion == "4":

            try:

                cantidad = float(input("Cantidad a transferir: "))

                cuenta = input("Número de cuenta destino: ")

                if cantidad <= 0:

                    print("La cantidad debe ser mayor que 0.")

                elif cantidad > usuario.saldo:

                    print("Saldo insuficiente.")

                else:

                    usuario.saldo -= cantidad

                    print(f"Transferencia de {cantidad} € realizada a {cuenta}.")

                    print(f"Saldo restante: {usuario.saldo} €")

            except ValueError:

                print("Cantidad no válida.")


        # OPCIÓN 5 - REGISTRAR GASTO _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        elif opcion == "5":

            try:

                cantidad = float(input("Monto del gasto: "))

                if cantidad <= 0:

                    print("El gasto debe ser mayor que 0.")

                else:

                    descripcion = input("Descripción del gasto: ")

                    usuario.registrar_gasto(descripcion, cantidad)

                    print("Gasto registrado correctamente.")

            except ValueError:

                print("Cantidad no válida.")

        # OPCIÓN 6 - MOSTRAR GASTOS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
       
        elif opcion == "6":
            
            if not usuario.gastos:
                
                print("No hay gastos registrados.")
           
            else:
                
                print("\n--- LISTA DE GASTOS ---")
                
                for i, gasto in enumerate(usuario.gastos, start=1):
                    
                    print(f"{i}. {gasto['descripcion']} - {gasto['cantidad']} €")

        # OPCIÓN 7 - MEDIA DE GASTOS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        elif opcion == "7":

            if not usuario.gastos:

                print("No hay gastos registrados.")

            else:

                total = sum(g["cantidad"] for g in usuario.gastos)

                media = total / len(usuario.gastos)

                print(f"Media de gastos: {media:.2f} €")

        # OPCIÓN 0 - SALIR _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        elif opcion == "0":

            print("\nGracias por usar PAL PARNE.")

            print("Sesión cerrada.\n")

            salir = True

        # OPCIÓN NO VÁLIDA _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        else:
            
            print("Opción no válida. Inténtalo de nuevo.")

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
