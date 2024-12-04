import random

num = random.randint(1, 100)
intentos = 0
adivinado = False
while not adivinado:
    mensaje = int(input("Adivina el número secreto entre 1 y 100: "))
    intentos += 1
    if mensaje == num:
        adivinado = True
    elif mensaje < num:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

print(f"Has usado {intentos} intentos.")