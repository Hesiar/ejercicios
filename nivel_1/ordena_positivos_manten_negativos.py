def ordena_positivos(lista):
    positivos_ordenados = sorted([num for num in lista if num > 0])
    resultado = []
    indice_positivos = 0

    for num in lista:
        if num > 0:
            resultado.append(positivos_ordenados[indice_positivos])
            indice_positivos += 1
        else:
            resultado.append(num)

    return resultado

lista = [3, -1, 4, 0, -2, 5, 1]
resultado = ordena_positivos(lista)
print("Lista original:", lista)
print("Lista ordenada:", resultado)
