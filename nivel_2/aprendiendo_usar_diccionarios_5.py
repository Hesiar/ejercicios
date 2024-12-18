
creditos = {"Matemáticas": 6, "Física": 4, "Quimica": 5}
total_creditos = 0

for credito in creditos:
    print(f"La asignatura {credito} tiene {creditos[credito]} créditos.")
    total_creditos += creditos[credito]    
    
print(f"El total de créditos del curso es {total_creditos}.")

"""
for asignatura, credito in creditos.items():
    print(f"La asignatura {asignatura} tiene {credito} créditos.")
    
"""