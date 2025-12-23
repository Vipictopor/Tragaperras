import random
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


def generar_tirada(seis=False):
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


def l_vertical(tirada=[], pos=0):
    try:
        if tirada[pos] == tirada[pos+5] == tirada[pos+10]:
            return tirada[pos]
        return None
    except IndexError:
        return None


def l_horizontal3(tirada=[], pos=0):
    try:
        assert (pos in (0, 1, 2, 5, 6, 7, 10, 11, 12)), "posicion no válida"
        if tirada[pos] == tirada[pos+1] and tirada[pos] == tirada[pos+2]:
            return tirada[pos]
        return None
    except AssertionError as error:
        print(error)
        return None


def l_horizontal4(tirada=[], pos=0):
    try:
        assert (pos in (0, 1, 5, 6, 10, 11)), "posicion no válida"
        if tirada[pos] == tirada[pos+1] and tirada[pos] == tirada[pos+2] and tirada[pos] == tirada[pos+3]:
            return tirada[pos]
        return None
    except AssertionError as error:
        print(error)
        return False


def l_horizontal5(tirada=[], pos=0):
    try:
        assert (pos in (0, 5, 10)), "posicion no válida"
        if tirada[pos] == tirada[pos+1] and tirada[pos] == tirada[pos+2] and tirada[pos] == tirada[pos+3] and tirada[pos] == tirada[pos+4]:
            return tirada[pos]
        return None
    except AssertionError as error:
        print(error)
        return False


def arriba(tirada=[]):
    if ((tirada[2] == tirada[6]) and
        (tirada[2] == tirada[8]) and
        (tirada[2] == tirada[10]) and
        (tirada[2] == tirada[11]) and
        (tirada[2] == tirada[12]) and
        (tirada[2] == tirada[13]) and
            (tirada[2] == tirada[14])):
        return tirada[2]


def abajo(tirada=[]):
    if ((tirada[12] == tirada[0]) and
            (tirada[12] == tirada[1]) and
            (tirada[12] == tirada[2]) and
            (tirada[12] == tirada[3]) and
            (tirada[12] == tirada[4]) and
            (tirada[12] == tirada[6]) and
            (tirada[12] == tirada[8])):
        return tirada[12]


def zig(tirada=[]):
    if ((tirada[2] == tirada[10]) and
            (tirada[2] == tirada[6]) and
            (tirada[2] == tirada[8]) and
            (tirada[2] == tirada[14])):
        return tirada[2]


def zag(tirada=[]):
    if ((tirada[12] == tirada[0]) and
            (tirada[12] == tirada[4]) and
            (tirada[12] == tirada[6]) and
            (tirada[12] == tirada[8])):
        return tirada[12]


def diagonal(tirada=[], pos=0, dire=None):
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


def ojo(tirada=[]):
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


def jackpot(tirada=[]):
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
