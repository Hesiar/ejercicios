
fechaHoy = input("Escriba la fecha de hoy en formato DD/MM/AAAA:    ")

meses = {1:"Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
dia = int(fechaHoy.split("/")[0])
mes = int(fechaHoy.split("/")[1])
año = int(fechaHoy.split("/")[2])

# También se puede poner como:       dia, mes, año = fechaHoy.split("/")

if (mes in meses):
    print(f"La fecha de hoy es {dia} de {meses[mes]} de {año}")
else:
    print("La fecha introducida no es válida")