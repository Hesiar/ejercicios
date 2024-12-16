
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

notas = []

for i in range(len(asignaturas)):
    nota = float(input(f"¿Qué nota has obtenido en {asignaturas[i]}?       "))
    notas.append(nota)
    
for i in range(len(notas)):
    if notas[i] < 5:
        print(f"Debes repetir la asignatura de {asignaturas[i]}. Tienes una calificación de {notas[i]}")
