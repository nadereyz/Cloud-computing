# Definición de las piezas
piezas = {
    'p': 'peón',
    't': 'torre',
    'c': 'caballo',
    'a': 'alfil',
    'd': 'dama',
    'r': 'rey',
    '.': 'casilla vacía'
}

# Inicialización del tablero
tablero = [
    [("negre", "t"), ("negre", "c"), ("negre", "a"), ("negre", "d"), ("negre", "r"), ("negre", "a"), ("negre", "c"), ("negre", "t")],
    [("negre", "p")]*8,
    [(" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", ".")],
    [(" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", ".")],
    [(" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", ".")],
    [(" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", "."), (" ", ".")],
    [("blanc", "p")]*8,
    [("blanc", "t"), ("blanc", "c"), ("blanc", "a"), ("blanc", "d"), ("blanc", "r"), ("blanc", "a"), ("blanc", "c"), ("blanc", "t")]
]

def dibujar_tablero(tablero):
    # Etiquetas de las columnas (letras)
    print("   1 2 3 4 5 6 7 8")
    print("  -----------------")

    for i, fila in enumerate(tablero):
        # Etiqueta de la fila (número)
        print(f"{8 - i}|", end=' ')

        for casilla in fila:
            if casilla[0] == "negre":
                print(casilla[1], end=' ')
            elif casilla[0] == "blanc":
                print(casilla[1].upper(), end=' ')
            else:
                print('.', end=' ')
        print()

    print("  -----------------")

def capturar(tablero, origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino

    if tablero[fila_origen][columna_origen][1] != "p":
        print("Solo los peones pueden capturar. Inténtalo de nuevo.")
        return False

    if tablero[fila_destino][columna_destino][0] == tablero[fila_origen][columna_origen][0]:
        print("No puedes capturar tu propia pieza.")
        return False

    tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
    tablero[fila_origen][columna_origen] = (" ", ".")

    print("Captura exitosa.")
    return True


def es_movimiento_valido(tablero, origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino

    # Verificar si las coordenadas están dentro del tablero
    if not (0 <= fila_origen < 8 and 0 <= columna_origen < 8 and 0 <= fila_destino < 8 and 0 <= columna_destino < 8):
        print("Coordenadas fuera del tablero. Inténtalo de nuevo.")
        return False

    # Verificar si hay una pieza en la casilla de origen
    if tablero[fila_origen][columna_origen] == (" ", "."):
        print("No hay una pieza en la casilla de origen. Inténtalo de nuevo.")
        return False

    # Verificar si el movimiento es válido para la pieza seleccionada
    pieza = tablero[fila_origen][columna_origen][1]
    color_pieza = tablero[fila_origen][columna_origen][0]
    
    if pieza == 'p':  # Peón
        # Movimiento básico para el peón (avance simple)
        if color_pieza == "negre" and fila_destino == fila_origen + 1 and columna_destino == columna_origen:
            return True
        elif color_pieza == "blanc" and fila_destino == fila_origen - 1 and columna_destino == columna_origen:
            return True

    # Agrega lógica para otras piezas según sea necesario

    # Si llegamos aquí, el movimiento no es válido
    print("Movimiento no válido para la pieza seleccionada. Inténtalo de nuevo.")
    return False
    
        


def es_jaque(tablero, color_rey):
    # Encontrar la posición del rey
    for fila in range(8):
        for columna in range(8):
            if tablero[fila][columna] == (color_rey, 'r'):
                posicion_rey = (fila, columna)

    # Verificar si alguna pieza del oponente amenaza al rey
    for fila in range(8):
        for columna in range(8):
            if tablero[fila][columna][0] != color_rey and es_movimiento_valido(tablero, (fila, columna), posicion_rey):
                return True

    return False

def jaque_mate(tablero, color_rey):
    # Encontrar la posición del rey
    posicion_rey = encontrar_posicion_rey(tablero, color_rey)

    # Verificar si el rey está en jaque
    if not es_jaque(tablero, color_rey):
        return False  

    # Verificar si el rey tiene algún movimiento legal
    for i in range(-1, 2):
        for j in range(-1, 2):
            nuevo_destino = (posicion_rey[0] + i, posicion_rey[1] + j)
            if es_movimiento_valido(tablero, posicion_rey, nuevo_destino):
                return False  

    print(f"¡Jaque mate! ¡Rey {color_rey} no tiene movimientos legales!")
    return True

def encontrar_posicion_rey(tablero, color_rey):
    # Encontrar la posición del rey
    for fila in range(8):
        for columna in range(8):
            if tablero[fila][columna] == (color_rey, 'r'):
                return (fila, columna)

# Juego principal
tablero_actual = tablero

while True:
    dibujar_tablero(tablero_actual)
    origen_fila = int(input("Fila de origen: "))
    origen_columna = int(input("Columna de origen: "))
    destino_fila = int(input("Fila de destino: "))
    destino_columna = int(input("Columna de destino: "))

    origen = (origen_fila, origen_columna)
    destino = (destino_fila, destino_columna)

    if es_movimiento_valido(tablero_actual, origen, destino):
        if capturar(tablero_actual, origen, destino):
            # Verificar si algún rey está en jaque o jaque mate
            pass
    else:
        print("Movimiento inválido. Inténtalo de nuevo.")

