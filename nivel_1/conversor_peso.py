
peso = float(input("Introduzca su peso: "))
peso_unidad = input("¿El peso introducido está en Kilos o en Libras? (Pulse K para Kilos o L para Libras): ").upper()

if peso_unidad == "K":
    peso_libras = peso * 2.20462  
    print(f"Su peso de {peso:.2f} Kg en Libras es {peso_libras:.2f} Lb")
elif peso_unidad == "L":
    peso_kilos = peso * 0.453592  
    print(f"Su peso de {peso:.2f} Lb en Kilos es {peso_kilos:.2f} Kg")
else:
    print("Unidad no válida. Por favor, introduzca K para Kilos o L para Libras.")
