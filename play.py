import reglas

# _________REVISAR COMPROVACIÓN DE PATRONES_________#


def evaluar_premios(tirada):
    premios_detectados = []

    # --- 1. EVALUAR JACKPOT (Prioridad Máxima) ---
    if reglas.jackpot(tirada):
        # Premio Jackpot
        premios_detectados.append("JACKPOT")

    # --- 2. EVALUAR HORIZONTALES (Por cada fila) ---
    # Fila 0: pos 0, Fila 1: pos 5, Fila 2: pos 10
    for fila_inicio in [0, 5, 10]:
        if reglas.l_horizontal5(tirada, fila_inicio):
            premios_detectados.append(f"H5_FILA_{fila_inicio//5}")
        elif reglas.l_horizontal4(tirada, fila_inicio):
            premios_detectados.append(f"H4_FILA_{fila_inicio//5}")
        elif reglas.l_horizontal3(tirada, fila_inicio):
            premios_detectados.append(f"H3_FILA_{fila_inicio//5}")

    # --- 3. GRUPO ESPECIAL: ARRIBA ---
    gano_arriba = reglas.arriba(tirada)
    if gano_arriba:
        premios_detectados.append("PATRON_ARRIBA")

    # --- 4. GRUPO ESPECIAL: ABAJO ---
    gano_abajo = reglas.abajo(tirada)
    if gano_abajo:
        premios_detectados.append("PATRON_ABAJO")

    # --- 5. PATRONES DEPENDIENTES (Solo si no salieron los jefes) ---
    if not gano_arriba:
        if reglas.zig(tirada):
            premios_detectados.append("ZIG")
        # Aquí irían las diagonales que dependen de "arriba"
        if reglas.diagonal(tirada, pos=0, dire="l"):
            premios_detectados.append("DIAGONAL_L")

    if not gano_abajo:
        if reglas.zag(tirada):
            premios_detectados.append("ZAG")
        # Aquí irían las diagonales que dependen de "abajo"
        if reglas.diagonal(tirada, pos=2, dire="r"):
            premios_detectados.append("DIAGONAL_R")

    # El "OJO" parece ser independiente, lo evaluamos aparte
    if reglas.ojo(tirada):
        premios_detectados.append("OJO")
    # Las verticales tambien son inependientes
    for i in range(5):
        if reglas.l_vertical(tirada, pos=i):
            premios_detectados.append(f"V_FILA_{i}")

    return premios_detectados
# _________BLOQUE PRINCIPAL DE LA MÁQUINA TRAGAPERRAS_________#


while True:
    input("Presiona ENTER para tirar la maquinita...")
    tirada = []
    try:
        for i in range(3):
            if i == 1:
                tirada = tirada + reglas.generar_tirada(True)
            else:
                tirada = tirada + reglas.generar_tirada()

        for i in range(3):
            pos = i*5
            print(
                f"||{tirada[pos]}|{tirada[pos+1]}|{tirada[pos+2]}|{tirada[pos+3]}|{tirada[pos+4]}||")

        assert not (
            tirada[6] == "❌" and
            tirada[7] == "❌" and
            tirada[8] == "❌"
        ), "Has perdido"

    except AssertionError as error:
        print(error)
        break


# HAY QUE ASEGURARSE DE DEVOLVER EL SIMBOLO DEL PATRÓN EN LAS FUNCIONES QUE DETECTAN PATRONES, ALMACENARLOS EN LISTA DE LISTAS, PARA ASÍ RECORRERLAS Y CONSULTAR LOS DICCIONARIOS.
