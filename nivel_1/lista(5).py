
abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

nuevo_abecedario = []

for i in range(len(abecedario)):
    if (i+1) % 3 != 0:
        nuevo_abecedario.append(abecedario[i])
        
print("El nuevo abecedario es: ", nuevo_abecedario)