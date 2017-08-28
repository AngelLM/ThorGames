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

moverPiezaCodes=["Thor mueve pieza a casilla 0",
                "Thor mueve pieza a casilla 1",
                "Thor mueve pieza a casilla 2",
                "Thor mueve pieza a casilla 3",
                "Thor mueve pieza a casilla 4",
                "Thor mueve pieza a casilla 5",
                "Thor mueve pieza a casilla 6",
                "Thor mueve pieza a casilla 7",
                "Thor mueve pieza a casilla 8"]



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
                # print "WIN en fila:" + str(y+1)
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
                # print "WIN en columna:" + str(y+1)
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
                # print "WIN en diagonal:" + str(y+1)
                return ["d", y]
                break

    return ["n",0]

def comprobarRival():
    global juegoTerminado
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
                # print "Mover a fila:" + str(y+1)
                return ["f", y]
                break
            if contadorRival==3:
                print "Human wins"
                juegoTerminado = True
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
                # print "Mover a columna:" + str(y+1)
                return ["c", y]
                break
            if contadorRival==3:
                print "Human wins"
                juegoTerminado = True
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
            if contadorRival==3:
                print "Human wins"
                juegoTerminado = True
                break

    return ["n",0]


def ganarFila(f):
    global casillas
    global juegoTerminado
    if f==0:
        for i in [0,1,2]:
            if casillas[i] != 2:
                casillas[i] = 2
                moverPieza(i)

    elif f==1:
        for i in [3,4,5]:
            if casillas[i] != 2:
                casillas[i] = 2
                moverPieza(i)
    else:
        for i in [6,7,8]:
            if casillas[i] != 2:
                casillas[i] = 2
                moverPieza(i)

    print "Thor wins"
    juegoTerminado = True

def ganarColumna(c):
    global casillas
    global juegoTerminado
    if c==0:
        for i in [0,3,6]:
            if casillas[i] != 2:
                casillas[i] = 2
                moverPieza(i)

    elif c==1:
        for i in [1,4,7]:
            if casillas[i] != 2:
                casillas[i] = 2
                moverPieza(i)
    else:
        for i in [2,5,8]:
            if casillas[i] != 2:
                casillas[i] = 2
                moverPieza(i)

    print "Thor wins"
    juegoTerminado = True

def ganarDiagonal(d):
    global casillas
    global juegoTerminado
    if d==0:
        for i in [0,4,8]:
            if casillas[i] != 2:
                casillas[i] = 2
                moverPieza(i)

    else:
        for i in [2,4,6]:
            if casillas[i] != 2:
                casillas[i] = 2
                moverPieza(i)

    print "Thor wins"
    juegoTerminado = True

def bloquearFila(f):
    global casillas
    if f==0:
        for i in [0,1,2]:
            if casillas[i] != 1:
                casillas[i] = 2
                moverPieza(i)

    elif f==1:
        for i in [3,4,5]:
            if casillas[i] != 1:
                casillas[i] = 2
                moverPieza(i)
    else:
        for i in [6,7,8]:
            if casillas[i] != 1:
                casillas[i] = 2
                moverPieza(i)
    # print "Thor bloks"

def bloquearColumna(c):
    global casillas
    if c==0:
        for i in [0,3,6]:
            if casillas[i] != 1:
                casillas[i] = 2
                moverPieza(i)

    elif c==1:
        for i in [1,4,7]:
            if casillas[i] != 1:
                casillas[i] = 2
                moverPieza(i)
    else:
        for i in [2,5,8]:
            if casillas[i] != 1:
                casillas[i] = 2
                moverPieza(i)
    # print "Thor bloks"

def bloquearDiagonal(d):
    global casillas
    if d==0:
        for i in [0,4,8]:
            if casillas[i] != 1:
                casillas[i] = 2
                moverPieza(i)

    else:
        for i in [2,4,6]:
            if casillas[i] != 1:
                casillas[i] = 2
                moverPieza(i)

    # print "Thor bloks"

def pedirDatos():
    global casillas
    print "Casilla?"
    casilla = input()
    numerocasilla = int(casilla)
    casillas[numerocasilla]=1
    actualizarDatos()

def mover():
    if jugadaDetect():
        moverBordes()
    else:
        if not moverCentro():
            if not moverEsquinas():
                moverBordes()

def moverCentro():
    global casillas
    if casillas[4]==0:
        casillas[4]=2
        moverPieza(4)
        return True
    return False

def moverEsquinas():
    global casillas
    for i in [0,2,6,8]:
        if casillas[i]==0:
            casillas[i]=2
            moverPieza(i)
            return True
    return False

def jugadaDetect():
    global casillas
    contador=0
    for i in range(len(casillas)):
        if casillas[i]!=0:
            contador += 1
    if contador == 3:
        contadoresquinas=0
        for i in [0,2,6,8]:
            if casillas[i]==1:
                contadoresquinas += 1
        if contadoresquinas == 2:
            return True
    return False

def moverBordes():
    global casillas
    casillasvacias=[]
    for i in [1,3,5,7]:
        if casillas[i]==0:
            casillasvacias.append(i)
    randomnum = random.randrange(len(casillasvacias))
    k = casillasvacias[randomnum]
    casillas[k]=2
    moverPieza(k)
    actualizarDatos()

def printInicial():
    print ""
    print '0 | 1 | 2'
    print "---------"
    print '3 | 4 | 5'
    print "---------"
    print '6 | 7 | 8'
    print ""

def printTablero():
    print ""
    print str(casillas[0]) + ' | ' + str(casillas[1]) + ' | ' + str(casillas[2])
    print "---------"
    print str(casillas[3]) + ' | ' + str(casillas[4]) + ' | ' + str(casillas[5])
    print "---------"
    print str(casillas[6]) + ' | ' + str(casillas[7]) + ' | ' + str(casillas[8])
    print ""

def checkFinal():
    global casillas
    global juegoTerminado

    if juegoTerminado==False:
        contador=False
        for i in range(len(casillas)):
            if casillas[i]==0:
                contador=True
        if contador==False:
            juegoTerminado=True
            print "Empate"

def moverPieza(pos):
    print moverPiezaCodes[pos]


printInicial()
while juegoTerminado==False:
    pedirDatos()
    actualizarDatos()
    comprobarRival()
    checkFinal()
    if juegoTerminado==False:
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
                mover()
    printTablero()
    checkFinal()
