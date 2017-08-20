import random

casillas = [0,0,0,              # 0 1 2
            0,0,0,              # 3 4 5
            0,0,0]              # 6 7 8

filas = [[0,0,0],
        [0,0,0],
        [0,0,0]]

columnas = [[0,0,0],
        [0,0,0],
        [0,0,0]]

diagonales= [[0,0,0],
        [0,0,0]]

juegoTerminado = False

def actualizarDatos():
    global filas
    global columnas
    global diagonales
    filas = [[casillas[0],casillas[1],casillas[2]],
            [casillas[3],casillas[4],casillas[5]],
            [casillas[6],casillas[7],casillas[8]]]

    columnas = [[casillas[0],casillas[3],casillas[6]],
            [casillas[1],casillas[4],casillas[7]],
            [casillas[2],casillas[5],casillas[8]]]

    diagonales = [[casillas[0],casillas[4],casillas[8]],
            [casillas[2],casillas[4],casillas[6]]]

def comprobarPropio():
    # Filas
    for y in range(3):
        contadorPropio=0
        contadorRival=0
        for i in range(3):
            if filas[y][i]==2:
                contadorPropio+=1
            elif filas[y][i]==1:
                contadorRival+=1
            if i==2 and contadorPropio==2 and contadorRival==0:
                print "WIN en fila:" + str(y+1)
                return ["f", y]
                break

    # columnas
    for y in range(3):
        contadorPropio=0
        contadorRival=0
        for i in range(3):
            if columnas[y][i]==2:
                contadorPropio+=1
            elif columnas[y][i]==1:
                contadorRival+=1
            if i==2 and contadorPropio==2 and contadorRival==0:
                print "WIN en columna:" + str(y+1)
                return ["c", y]
                break

    # diagonales
    for y in range(2):
        contadorPropio=0
        contadorRival=0
        for i in range(3):
            if diagonales[y][i]==2:
                contadorPropio+=1
            elif diagonales[y][i]==1:
                contadorRival+=1
            if i==2 and contadorPropio==2 and contadorRival==0:
                print "WIN en diagonal:" + str(y+1)
                return ["d", y]
                break

    return ["n",0]

def comprobarRival():
    # Filas
    for y in range(3):
        contadorPropio=0
        contadorRival=0
        for i in range(3):
            if filas[y][i]==1:
                contadorRival+=1
            elif filas[y][i]==2:
                contadorPropio+=1
            if i==2 and contadorRival==2 and contadorPropio==0:
                print "Mover a fila:" + str(y+1)
                return ["f", y]
                break

    # columnas
    for y in range(3):
        contadorPropio=0
        contadorRival=0
        for i in range(3):
            if columnas[y][i]==1:
                contadorRival+=1
            elif columnas[y][i]==2:
                contadorPropio+=1
            if i==2 and contadorRival==2 and contadorPropio==0:
                print "Mover a columna:" + str(y+1)
                return ["c", y]
                break

    # diagonales
    for y in range(2):
        contadorPropio=0
        contadorRival=0
        for i in range(3):
            if diagonales[y][i]==1:
                contadorRival+=1
            elif diagonales[y][i]==2:
                contadorPropio+=1
            if i==2 and contadorRival==2 and contadorPropio==0:
                print "Mover a diagonal:" + str(y+1)
                return ["d", y]
                break
    return ["n",0]


def ganarFila(f):
    global casillas
    if f==0:
        for win in [casillas[0], casillas[1],casillas[2]]:
            if win != 2:
                win = 2

    elif f==1:
        for win in [casillas[3], casillas[4],casillas[5]]:
            if win != 2:
                win = 2
    else:
        for win in [casillas[6], casillas[7],casillas[8]]:
            if win != 2:
                win = 2
    print "Thor wins"
    juegoTerminado = True

def ganarColumna(c):
    global casillas
    if c==0:
        for win in [casillas[0], casillas[3],casillas[6]]:
            if win != 2:
                win = 2

    elif c==1:
        for win in [casillas[1], casillas[4],casillas[7]]:
            if win != 2:
                win = 2
    else:
        for win in [casillas[2], casillas[5],casillas[8]]:
            if win != 2:
                win = 2
    print "Thor wins"
    juegoTerminado = True

def ganarDiagonal(d):
    global casillas
    if d==0:
        for win in [casillas[0], casillas[4],casillas[8]]:
            if win != 2:
                win = 2

    else:
        for win in [casillas[2], casillas[4],casillas[6]]:
            if win != 2:
                win = 2

    print "Thor wins"
    juegoTerminado = True

def bloquearFila(f):
    global casillas
    if f==0:
        for bloq in [casillas[0], casillas[1],casillas[2]]:
            if bloq != 1:
                bloq = 2

    elif f==1:
        for bloq in [casillas[3], casillas[4],casillas[5]]:
            if bloq != 1:
                bloq = 2
    else:
        for win in [casillas[6], casillas[7],casillas[8]]:
            if bloq != 1:
                bloq = 2
    print "Thor bloks"

def bloquearColumna(c):
    global casillas
    if c==0:
        for win in [casillas[0], casillas[3],casillas[6]]:
            if bloq != 1:
                bloq = 2

    elif c==1:
        for bloq in [casillas[1], casillas[4],casillas[7]]:
            if bloq != 1:
                bloq = 2
    else:
        for bloq in [casillas[2],casillas[5],casillas[8]]:
            if bloq != 1:
                bloq = 2
    print "Thor bloks"

def bloquearDiagonal(d):
    global casillas
    if d==0:
        for bloq in [casillas[0],casillas[4],casillas[8]]:
            if bloq != 1:
                bloq = 2

    else:
        for bloq in [casillas[2],casillas[4],casillas[6]]:
            if bloq != 1:
                bloq = 2

    print "Thor bloks"

def pedirDatos():
    global casillas
    print "Casilla?"
    casilla = input()
    numerocasilla = int(casilla)
    casillas[numerocasilla]=1
    actualizarDatos()

def moverAleatorio():
    global casillas
    casillasvacias=[]
    for casilla in casillas:
        if casilla==0:
            casillasvacias.append(casilla)
    randomnum = random.randrange(len(casillasvacias))
    casillasvacias[randomnum]=2
    actualizarDatos()

def printTablero():
    print str(casillas[0]) + ' | ' + str(casillas[1]) + ' | ' + str(casillas[2])
    print "---------"
    print str(casillas[3]) + ' | ' + str(casillas[4]) + ' | ' + str(casillas[5])
    print "---------"
    print str(casillas[6]) + ' | ' + str(casillas[7]) + ' | ' + str(casillas[8])

while juegoTerminado==False:
    pedirDatos()
    actualizarDatos()
    checkPropio = comprobarPropio()
    if checkPropio[0]!="n":
        if checkPropio[0]=="f":
            ganarFila(checkPropio[1])
        if checkPropio[0]=="c":
            ganarColumna(checkPropio[1])
        if checkPropio[0]=="d":
            ganarDiagonal(checkPropio[1])
    else:
        checkRival = comprobarRival()
        if checkRival[0]!="n":
            if checkRival[0]=="f":
                bloquearFila(checkRival[1])
            if checkRival[0]=="c":
                bloquearColumna(checkRival[1])
            if checkRival[0]=="d":
                bloquearDiagonal(checkRival[1])
        else:
            moverAleatorio()
    printTablero()
