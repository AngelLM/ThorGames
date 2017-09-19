import random
import math
import time

import sys
import serial
import glob

puerto0='/dev/ttyACM0'


gameArray = [0,0,0,0,0,0,0,0,0]

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

empiezaThor = False
turnoNumero = 0
turnoThor = False
turnoRival = True
juegoTerminado = False

moverPiezaCodesUno=["G0A10B-35C-35D-85X0Y-2.3Z-2.3 \n",
                    "G0A-2B-30C-30D-90X0Y-2.6Z-2.6 \n",
                    "G0A-13.5B-33C-33D-88X0Y-2.35Z-2.35 \n",
                    "G0A7B-45C-45D-70X0Y-2Z-2 \n",
                    "G0A-3B-45C-45D-70X0Y-2Z-2 \n",
                    "G0A-12B-45C-45D-70X0Y-2Z-2 \n",
                    "G0A6B-70C-70D-30X0Y-0.5Z-0.5 \n",
                    "G0A-2B-65C-65D-34.5X0Y-0.7Z-0.7 \n",
                    "G0A-10B-70C-70D-28X0Y-0.35Z-0.35 \n"]

moverPiezaCodesDos=["G0A10B-38C-38D-92X0Y-2.3Z-2.3 \n",
                    "G0A-2B-34C-34D-98X0Y-2.6Z-2.6 \n",
                    "G0A-13.5B-37C-37D-92X0Y-2.35Z-2.35 \n",
                    "G0A7B-49C-49D-75X0Y-2Z-2 \n",
                    "G0A-3B-49C-49D-75X0Y-2Z-2 \n",
                    "G0A-12B-49C-49D-75X0Y-2Z-2 \n",
                    "G0A6B-74C-74D-35X0Y-0.5Z-0.5 \n",
                    "G0A-2B-72C-72D-38.5X0Y-0.7Z-0.7 \n",
                    "G0A-10B-75C-75D-32X0Y-0.35Z-0.35 \n"]

moverPiezaCodesTres=["G0A-2B-40C-40D90X3Y-9Z-9 \n",
                    "G0A-2B-40C-40D90X3Y-9Z-9 \n",
                    "G0A-2B-40C-40D90X3Y-9Z-9 \n",
                    "G0A-2B-40C-40D90X3Y-9Z-9 \n",
                    "G0A-2B-40C-40D90X3Y-9Z-9 \n",
                    "G0A-2B-40C-40D90X3Y-9Z-9 \n",
                    "G01A-2B-40C-40D90X3Y-9Z-9F2000 \n",
                    "G01A-2B-40C-40D90X3Y-9Z-9F2000 \n",
                    "G01A-2B-40C-40D90X3Y-9Z-9F2000 \n"]

pillarPiezaCodesUno=["Pillo Pieza 0 UNO \n",
                    "Pillo Pieza 1 UNO \n",
                    "Pillo Pieza 2 UNO \n",
                    "Pillo Pieza 3 UNO \n",
                    "Pillo Pieza 4 UNO \n"]

pillarPiezaCodesDos=["Pillo Pieza 0 DOS \n",
                    "Pillo Pieza 1 DOS \n",
                    "Pillo Pieza 2 DOS \n",
                    "Pillo Pieza 3 DOS \n",
                    "Pillo Pieza 4 DOS \n"]

pillarPiezaCodesTres=["Pillo Pieza 0 TRES \n",
                    "Pillo Pieza 1 TRES \n",
                    "Pillo Pieza 2 TRES \n",
                    "Pillo Pieza 3 TRES \n",
                    "Pillo Pieza 4 TRES \n"]

def actualizarDatos():
    global filas
    global columnas
    global diagonales
    global gameArray

    filas = [[casillas[0],casillas[1],casillas[2]],
            [casillas[3],casillas[4],casillas[5]],
            [casillas[6],casillas[7],casillas[8]]]

    columnas = [[casillas[0],casillas[3],casillas[6]],
            [casillas[1],casillas[4],casillas[7]],
            [casillas[2],casillas[5],casillas[8]]]

    diagonales = [[casillas[0],casillas[4],casillas[8]],
            [casillas[2],casillas[4],casillas[6]]]

    for i in range(len(casillas)):
        if casillas[i]!=0:
            gameArray[i]=1

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
    casilla = comprobarArray(list(s0.readline()))
    numerocasilla = int(casilla)
    if numerocasilla!=-1 and numerocasilla!=10 and numerocasilla!=99:
        casillas[numerocasilla]=1
    actualizarDatos()

def comprobarArray(inputArray):
    # print inputArray
    global gameArray
    global empiezaThor
    # print gameArray
    contador = 0
    index = 5
    for i in range(len(gameArray)):
        if int(inputArray[i])!=gameArray[i]:
            contador += 1
            # print contador
            index = i
    if contador == 1:
        return index
    elif contador >1:
        print "Error: >1 diferencia"
        return 10
    elif contador == 0 and turnoNumero == 0:
        empiezaThor = True
        return 99
    else:
        print "Error: <1 diferencia"
        return -1



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

# def moverEsquinas():
#     global casillas
#     esquinasVacias=[]
#     for i in [0,2,6,8]:
#         if casillas[i]==0:
#             esquinasVacias.append(i)
#
#     if len(esquinasVacias)==0:
#         return False
#
#     elif len(esquinasVacias)==1:
#         casillas[esquinasVacias[0]]=2
#         moverPieza(esquinasVacias[0])
#         return True
#
#     else:
#         for k in esquinasVacias:
#             if k == 0:
#                 if casillas[1]==0 and casillas[2]==0 and casillas[3]==0 and casillas[6]==0:
#                     casillas[k]=2
#                     moverPieza(k)
#                     return True
#             if k == 2:
#                 if casillas[0]==0 and casillas[1]==0 and casillas[5]==0 and casillas[8]==0:
#                     casillas[k]=2
#                     moverPieza(k)
#                     return True
#             if k == 2:
#                 if casillas[0]==0 and casillas[1]==0 and casillas[5]==0 and casillas[8]==0:
#                     casillas[k]=2
#                     moverPieza(k)
#                     return True
#
#
#
#
#             casillas[i]=2
#             moverPieza(i)
#             return True
#     return False

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
    pillarPieza()
    print moverPiezaCodesUno[pos]
    # s0.write((moverPiezaCodesUno[pos]).encode('UTF-8'))
    print moverPiezaCodesDos[pos]
    # s0.write((moverPiezaCodesDos[pos]).encode('UTF-8'))
    print "M3S100 \n"
    # s0.write(('M3S100 \n').encode('UTF-8'))
    print "G4P0.5\n"
    # s0.write(('G4P0.5 \n').encode('UTF-8'))
    print moverPiezaCodesTres[pos]
    # s0.write(moverPiezaCodesTres[pos]).encode('UTF-8'))

def subirTurno():
    global turnoNumero
    turnoNumero += 1

def pillarPieza():
    print pillarPiezaCodesUno[turnoNumero]
    # s0.write((pillarPiezaCodesUno[turnoNumero]).encode('UTF-8'))
    print pillarPiezaCodesDos[turnoNumero]
    # s0.write((pillarPiezaCodesDos[turnoNumero]).encode('UTF-8'))
    print "M3S900 \n"
    # s0.write(('M3S900 \n').encode('UTF-8'))
    print "G4P0.5 \n"
    # s0.write(('G4P0.5 \n').encode('UTF-8'))
    print pillarPiezaCodesTres[turnoNumero]
    # s0.write(pillarPiezaCodesTres[turnoNumero]).encode('UTF-8'))


s0=serial.Serial(puerto0,9600)
time.sleep(2)
s0.close()
s0.open()

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
    actualizarDatos()
    printTablero()
    checkFinal()
    subirTurno()
s0.close()
