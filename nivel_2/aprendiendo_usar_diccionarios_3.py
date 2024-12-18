
frutas = {"Platano": 1.35, "Manzana": 1.15, "Naranja": 1.20}

fruta = input("¿Qué fruta quieres?    ").title()
kg= ""

if fruta in frutas:
    kg = float(input("¿Cuántos kilos quieres?    "))
    print(f"El precio de {fruta} es {frutas[fruta]} euros por kilo")
    print(f"El precio total es {frutas[fruta] * kg} euros")
else:
    print("No tenemos esa fruta disponible")