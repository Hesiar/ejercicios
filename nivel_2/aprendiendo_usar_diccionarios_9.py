
clientes = {}

print("¿Qúe desea hacer?")
print("1. Añadir cliente")
print("2. Eliminar cliente")
print("3. Buscar cliente")
print("4. Listar todos los clientes")
print("5. Listar clientes preferentes")
print("6. Salir")

opcion = input("")

while opcion != "6":

    match opcion:
        case "1":
            NIF = input("Ingrese el NIF del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            telefono = input("Ingrese el telefono del cliente: ")
            correo = input("Ingrese el email del cliente: ")
            preferente = input("¿Es preferente? (s/n): ")
            if preferente.lower() == "s":
                preferente = True
            elif preferente.lower() == "n":
                preferente = False
            
            datos_clientes = {"Nombre": nombre, "Direccion": direccion, "Telefono": telefono, "Correo": correo, "Preferente": preferente}
            clientes = {NIF : datos_clientes}   # Es equivalente a    --->     clientes[NIF] = datos_clientes
            
            print("Cliente añadido correctamente")
        
        case "2":
            NIF = input("Ingrese el NIF del cliente a eliminar: ")
            if NIF in clientes:
                del clientes[NIF]
                print("Cliente eliminado correctamente")
            else:
                print("El NIF introducido no está registrado.")
        
        case "3":
            NIF = input("Ingrese el NIF del cliente a buscar: ")
            if NIF in clientes:
                print("Nombre:", clientes[NIF]["Nombre"])
                print("Direccion:", clientes[NIF]["Direccion"])
                print("Telefono:", clientes[NIF]["Telefono"])
                print("Correo:", clientes[NIF]["Correo"])
                print("Preferente:", clientes[NIF]["Preferente"])
            else:
                print("El NIF introducido no está registrado.")
                
        case "4":
            for cliente in clientes:
                print("NIF:", cliente)
                print("Nombre:", clientes[cliente]["Nombre"])
                print("Direccion:", clientes[cliente]["Direccion"])
                print("Telefono:", clientes[cliente]["Telefono"])
                print("Correo:", clientes[cliente]["Correo"])
                print("Preferente:", clientes[cliente]["Preferente"])
                print("")
        
        case "5":
            for cliente in clientes:
                if clientes[cliente]["Preferente"] == True:
                    print("NIF:", cliente)
                    print("Nombre:", clientes[cliente]["Nombre"])
                    print("Direccion:", clientes[cliente]["Direccion"])
                    print("Telefono:", clientes[cliente]["Telefono"])
                    print("Correo:", clientes[cliente]["Correo"])
                    print("")
        
        case "6":
            print("Hasta luego")
            
        case _:
            print("Opción no válida")
            exit()
        
