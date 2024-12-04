num = 8
mensaje = int(input("Pienso en un numero entre el 1 y el 10. Adivinalo: "))

'''
Para un solo intento 

if mensaje == num:
    print("Correcto")
else:
    print("Se te acabaron los intentos")
'''
'''Para 10 intentos
intentos = 0
while mensaje != num and intentos < 10:
    if mensaje == num:
        print("Correcto")
    else:
        print("Prueba otra vez")
    intentos += 1    
    if mensaje ==num and intentos == 10:
        print("Correcto")
    else:
        print("Se te acabaron los intentos")
'''
# Sin limite
while mensaje != num:
    if mensaje == num:
        print("Correcto")
    else:
        print("Prueba otra vez")