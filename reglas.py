import random


class Reglas():

    def __init__(self):
        VALOR_SIMBOLO = {
            "🍒": 2,
            "🍋": 2,
            "🔔": 3,
            "🍀": 3,
            "💎": 5,
            "💰": 5,
            "7️⃣": 7
        }
    VALOR_PATRON = {
        "H3_FILA_0": 1,
        "H3_FILA_1": 1,
        "H3_FILA_2": 1,
        "DIAGONAL_L": 1,
        "DIAGONAL_R": 1,
        "H4_FILA_0": 2,
        "H4_FILA_1": 2,
        "H4_FILA_2": 2,
        "H5_FILA_0": 3,
        "H5_FILA_1": 3,
        "H5_FILA_2": 3,
        "ZIG": 4,
        "ZAG": 4,
        "PATRON_ARRIBA": 7,
        "PATRON_ABAJO": 7,
        "OJO": 8,
        "JACKPOT": 10
    }
    lista_premios = []

    def generar_tirada(self, seis=False):
        simbolos = ["🍒", "🍋", "🔔", "🍀", "💎", "💰", "7️⃣"]
        # Seleccionamos 5 símbolos al azar
        pesos = [25, 25, 15, 15, 8, 8, 4]
        posicion = 1
        tirada = random.choices(simbolos, weights=pesos, k=5)
        if seis:
            for i in range(3):
                seises = random.uniform(0.0, 100.0)
                if seises <= 1.14471424255:
                    tirada[posicion] = "❌"
                posicion = posicion + 1
        return tirada

    def l_vertical(self, tirada=[], pos=0):
        try:
            if tirada[pos] == tirada[pos+5] == tirada[pos+10]:
                return tirada[pos]
            return None
        except IndexError:
            return None

    def l_horizontal3(self, tirada=[], pos=0):
        try:
            assert (pos in (0, 1, 2, 5, 6, 7, 10, 11, 12)
                    ), "posicion no válida"
            if tirada[pos] == tirada[pos+1] and tirada[pos] == tirada[pos+2]:
                return tirada[pos]
            return None
        except AssertionError as error:
            print(error)
            return None

    def l_horizontal4(self, tirada=[], pos=0):
        try:
            assert (pos in (0, 1, 5, 6, 10, 11)), "posicion no válida"
            if tirada[pos] == tirada[pos+1] and tirada[pos] == tirada[pos+2] and tirada[pos] == tirada[pos+3]:
                return tirada[pos]
            return None
        except AssertionError as error:
            print(error)
            return False

    def l_horizontal5(self, tirada=[], pos=0):
        try:
            assert (pos in (0, 5, 10)), "posicion no válida"
            if tirada[pos] == tirada[pos+1] and tirada[pos] == tirada[pos+2] and tirada[pos] == tirada[pos+3] and tirada[pos] == tirada[pos+4]:
                return tirada[pos]
            return None
        except AssertionError as error:
            print(error)
            return False

    def arriba(self, tirada=[]):
        if ((tirada[2] == tirada[6]) and
            (tirada[2] == tirada[8]) and
            (tirada[2] == tirada[10]) and
            (tirada[2] == tirada[11]) and
            (tirada[2] == tirada[12]) and
            (tirada[2] == tirada[13]) and
                (tirada[2] == tirada[14])):
            return tirada[2]

    def abajo(self, tirada=[]):
        if ((tirada[12] == tirada[0]) and
                (tirada[12] == tirada[1]) and
                (tirada[12] == tirada[2]) and
                (tirada[12] == tirada[3]) and
                (tirada[12] == tirada[4]) and
                (tirada[12] == tirada[6]) and
                (tirada[12] == tirada[8])):
            return tirada[12]

    def zig(self, tirada=[]):
        if ((tirada[2] == tirada[10]) and
                (tirada[2] == tirada[6]) and
                (tirada[2] == tirada[8]) and
                (tirada[2] == tirada[14])):
            return tirada[2]

    def zag(self, tirada=[]):
        if ((tirada[12] == tirada[0]) and
                (tirada[12] == tirada[4]) and
                (tirada[12] == tirada[6]) and
                (tirada[12] == tirada[8])):
            return tirada[12]

    def diagonal(self, tirada=[], pos=0, dire=None):
        try:
            assert dire == "r" or dire == "l", "No es una opción válida"
            # patron "/" es derecha o r
            # patron "\" es izquierda o l
            if (dire == "r"):
                if ((tirada[pos] == tirada[pos+4]) and
                        tirada[pos] == tirada[pos+8]):
                    return tirada[pos]
            if (dire == "l"):
                if ((tirada[pos] == tirada[pos+6]) and
                        tirada[pos] == tirada[pos+12]):
                    return tirada[pos]
        except AssertionError as error:
            print(error)
            return False

    def ojo(self, tirada=[]):
        if ((tirada[2] == tirada[1]) and
                (tirada[2] == tirada[3]) and
                (tirada[2] == tirada[5]) and
                (tirada[2] == tirada[6]) and
                (tirada[2] == tirada[8]) and
                (tirada[2] == tirada[9]) and
                (tirada[2] == tirada[11]) and
                (tirada[2] == tirada[12]) and
                (tirada[2] == tirada[13])):
            return tirada[2]

    def jackpot(self, tirada=[]):
        if ((tirada[0] == tirada[1]) and
                (tirada[0] == tirada[2]) and
                (tirada[0] == tirada[3]) and
                (tirada[0] == tirada[4]) and
                (tirada[0] == tirada[5]) and
                (tirada[0] == tirada[6]) and
                (tirada[0] == tirada[7]) and
                (tirada[0] == tirada[8]) and
                (tirada[0] == tirada[9]) and
                (tirada[0] == tirada[10]) and
                (tirada[0] == tirada[11]) and
                (tirada[0] == tirada[12]) and
                (tirada[0] == tirada[13]) and
                (tirada[0] == tirada[14])):
            return tirada[0]

    def evaluar_premios(self, tirada):
        premios_detectados = []

        # --- 1. EVALUAR JACKPOT (Prioridad Máxima) ---
        if self.jackpot(tirada):
            # Premio Jackpot
            self.lista_premios.append("JACKPOT", self.jackpot(tirada))

        # --- 2. EVALUAR HORIZONTALES (Por cada fila) ---
        # Fila 0: pos 0, Fila 1: pos 5, Fila 2: pos 10
        for fila_inicio in [0, 5, 10]:
            if self.l_horizontal5(tirada, fila_inicio):
                self.lista_premios.append(
                    f"H5_FILA_{fila_inicio//5}", self.l_horizontal5(tirada, fila_inicio))
            elif self.l_horizontal4(tirada, fila_inicio):
                self.lista_premios.append(
                    f"H4_FILA_{fila_inicio//5}", self.l_horizontal4(tirada, fila_inicio))
            elif self.l_horizontal3(tirada, fila_inicio):
                self.lista_premios.append(
                    f"H3_FILA_{fila_inicio//5}", self.l_horizontal3(tirada, fila_inicio))

        # --- 3. GRUPO ESPECIAL: ARRIBA ---
        gano_arriba = self.arriba(tirada)
        if gano_arriba:
            self.lista_premios.append("PATRON_ARRIBA", self.arriba(tirada))

        # --- 4. GRUPO ESPECIAL: ABAJO ---
        gano_abajo = self.abajo(tirada)
        if gano_abajo:
            self.lista_premios.append("PATRON_ABAJO", self.abajo(tirada))

        # --- 5. PATRONES DEPENDIENTES (Solo si no salieron los jefes) ---
        if not gano_arriba:
            if self.zig(tirada):
                self.lista_premios.append("ZIG", self.zig(tirada))
            # Aquí irían las diagonales que dependen de "arriba"
            if self.diagonal(tirada, pos=0, dire="l"):
                self.lista_premios.append(
                    "DIAGONAL_L", self.diagonal(tirada, pos=0, dire="l"))

        if not gano_abajo:
            if self.zag(tirada):
                self.lista_premios.append("ZAG", self.zag(tirada))
            # Aquí irían las diagonales que dependen de "abajo"
            if self.diagonal(tirada, pos=2, dire="r"):
                self.lista_premios.append(
                    "DIAGONAL_R", self.diagonal(tirada, pos=2, dire="r"))

        # El "OJO" parece ser independiente, lo evaluamos aparte
        if self.ojo(tirada):
            self.lista_premios.append("OJO", self.ojo(tirada))
        # Las verticales tambien son inependientes
        for i in range(5):
            if self.l_vertical(tirada, pos=i):
                self.lista_premios.append(
                    f"V_FILA_{i}", self.l_vertical(tirada, pos=i))
        return premios_detectados

    def jugar(self):
        while True:
            input("Presiona ENTER para tirar la maquinita...")
            tirada = []
            try:
                for i in range(3):
                    if i == 1:
                        tirada = tirada + self.generar_tirada(True)
                    else:
                        tirada = tirada + self.generar_tirada()

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
