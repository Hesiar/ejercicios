
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

print("Yo estudio", end=" ")
for asignatura in asignaturas:
    print(asignatura, end=", " if asignatura != asignaturas[-1] else "")

