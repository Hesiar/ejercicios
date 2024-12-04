import random
def maquina():
    opciones = ["piedra", "papel", "tijera"]
    opcion = random.choice(opciones)
    return opcion
def ganador(jugador, bot):
    if jugador == bot:
        return "Empate"
    elif (
        (jugador == "piedra" and bot == "tijera") or
        (jugador == "papel" and bot == "piedra") or
        (jugador == "tijera" and bot == "papel")
    ):
        return "Ganaste"
    else:
        return "Alexa ganó"
while True:
    print("Piedra, Papel o Tijera. 1, 2, 3")
    jugador = input("Elige una opción (piedra, papel, tijera): ").lower()
    if jugador not in ["piedra", "papel", "tijera"]:
        print("¡Opción inválida! Elige nuevamente.")
        continue
    bot = maquina()
    print(f"Alexa eligió: {bot}")
    resultado = ganador(jugador, bot)
    print(f"Resultado: {resultado}")
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar_nuevamente.lower() != "s":
        break