
continuar = True

while continuar:

    print("Hola. Le vamos a preguntar un par de cosas.")
    print("")

    nombre = input("¿Cuál es tu nombre?    ")
    edad = input("¿Cuál es tu edad?    ")
    direccion = input("¿Cuál es tu dirección?    ")
    telefono = input("¿Cuál es tu número de teléfono?    ")

    usuarios = { "Nombre" : nombre, "Edad" : edad, "Direccion" : direccion, "Telefono" : telefono }    

    print("\nNuevo usuario registrado con éxito:")
    print(f"Nombre: {usuarios['Nombre']}, Edad: {usuarios['Edad']}, Direccion: {usuarios['Direccion']}, Telefono: {usuarios['Telefono']}")
    print("")
        
    respuesta = input("¿Desea introducir un nuevo usuario? (Y/N): ").upper()
    if respuesta == "N":
        continuar = False
        break
    else:
        print("")
        print("")
    
    