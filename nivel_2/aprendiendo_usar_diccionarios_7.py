import string
traductor_ingles = {"hola": "hello", "mi": "my", "nombre": "name", "es": "is"}

mensaje = input("Escribe algo para traducir al inglés:    ").lower()
palabras = mensaje.split()
traduccion = []

# Para tener en cuenta las comas y demas signos de puntuación hemos mirado ChatGPT y hemos dejado sus comentarios para 
# entender el código

for palabra in palabras:
    # Eliminar signos de puntuación al inicio y al final de la palabra
    palabra_sin_puntuacion = palabra.strip(string.punctuation)

    if palabra_sin_puntuacion in traductor_ingles:
        # Si la palabra está en el diccionario, traducirla y agregar la puntuación original
        palabra_traducida = traductor_ingles[palabra_sin_puntuacion]
        # Verificar si la palabra original tiene puntuación y agregarla de nuevo
        if palabra != palabra_sin_puntuacion:
            palabra_traducida += palabra[len(palabra_sin_puntuacion):]
        traduccion.append(palabra_traducida)
    else:
        traduccion.append(palabra)  # Si no está en el diccionario, mantener la palabra original

frase_traducida = " ".join(traduccion)

print(f"Traducción: {frase_traducida}")
    
    