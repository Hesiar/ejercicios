
divisas = {"Euro" : "€", "Dolar" : "$", "Yen" : "¥" }


respuesta = input("¿Cuál es tu divisa?       ").title()

match respuesta:
    case "Euro":
        print(f"El simbolo de su divisa es {divisas['Euro']}")
    case "Dolar":
        print(f"El simbolo de su divisa es {divisas['Dolar']}")
    case "Yen":
        print(f"El simbolo de su divisa es {divisas['Yen']}")
    case "Yenes":
        print(f"El simbolo de su divisa es {divisas['Yen']}")
    case _:
        print("No tenemos esa divisa en nuestro sistema")