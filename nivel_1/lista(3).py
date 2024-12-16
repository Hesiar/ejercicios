
print("Escriba los numeros ganadores de la primitiva:")

combinacion_ganadora =[]

for i in range(6):
    num = int(input(f"Ingrese el número {i+1}: "))
    combinacion_ganadora.append(num)
    
print(f"Los numeros ganadores ordenados de menor a mayor son: {sorted(combinacion_ganadora)}")
