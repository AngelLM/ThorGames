import random
import math
import time

import sys
import serial
import glob

puerto0='/dev/ttyUSB0'
puerto1='/dev/ttyACM0'
puerto2='/dev/ttyUSB1'


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
                    "G0A-1.5B-45C-45D-70X0Y-2Z-2 \n",
                    "G0A-12B-45C-45D-70X0Y-2Z-2 \n",
                    "G0A6B-70C-70D-30X0Y-0.5Z-0.5 \n",
                    "G0A-2B-65C-65D-34.5X0Y-0.7Z-0.7 \n",
                    "G0A-10B-70C-70D-28X0Y-0.35Z-0.35 \n"]

moverPiezaCodesDos=["G0A10B-38C-38D-92X0Y-2.3Z-2.3 \n",
                    "G0A-2B-34C-34D-98X0Y-2.6Z-2.6 \n",
                    "G0A-13.5B-37C-37D-92X0Y-2.35Z-2.35 \n",
                    "G0A7B-49C-49D-75X0Y-2Z-2 \n",
                    "G0A-1.5B-49C-49D-75X0Y-2Z-2 \n",
                    "G0A-12B-49C-49D-75X0Y-2Z-2 \n",
                    "G0A6B-74C-74D-35X0Y-0.5Z-0.5 \n",
                    "G0A-2B-72C-72D-38.5X0Y-0.7Z-0.7 \n",
                    "G0A-10B-75C-75D-32X0Y-0.35Z-0.35 \n"]

moverPiezaCodesTres=["G01A-2B40C40D-85X3Y-3Z-3F2000 \n",
                    "G01A-2B40C40D-85X3Y-3Z-3F2000 \n",
                    "G01A-2B40C40D-85X3Y-3Z-3F2000 \n",
                    "G01A-2B40C40D-85X3Y-3Z-3F2000 \n",
                    "G01A-2B40C40D-85X3Y-3Z-3F2000 \n",
                    "G01A-2B40C40D-85X3Y-3Z-3F2000 \n",
                    "G01A-2B40C40D-85X3Y-3Z-3F2000 \n",
                    "G01A-2B40C40D-85X3Y-3Z-3F2000 \n",
                    "G01A-2B40C40D-85X3Y-3Z-3F2000 \n"]

pillarPiezaCodesUno=["G0A65B-25C-25D-99X0Y-2Z-2 \n",
                    "G0A76B-25C-25D-99X0Y-2Z-2 \n",
                    "G0A90B-32C-32D-100X0Y-2Z-2 \n",
                    "G0A102B-32C-32D-100X0Y-2Z-2 \n",
                    "G0A112B-32C-32D-100X0Y-2.5Z-2.5 \n"]

pillarPiezaCodesDos=["G0A65B-39C-39D-99X0Y-2.7Z-2.7 \n",
                    "G0A76B-34C-34D-105X0Y-2.8Z-2.8 \n",
                    "G0A90B-34C-34D-106X0Y-2.8Z-2.8 \n",
                    "G0A102B-34C-34D-106X0Y-2.9Z-2.9 \n",
                    "G0A112B-38.5C-38.5D-99X0Y-2.7Z-2.7 \n"]

pillarPiezaCodesTres=["G01A-2B-30C-30D-75X3Y-1Z-1F2000 \n",
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
    s2.write(('w').encode('UTF-8'))
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
    s2.write(('w').encode('UTF-8'))
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
    s2.write(('w').encode('UTF-8'))
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
    if casilla!=10 and casilla!=-1 and casilla!=99:
        numerocasilla = int(casilla)
        if numerocasilla!=-1 and numerocasilla!=10 and numerocasilla!=99:
            casillas[numerocasilla]=1
        actualizarDatos()

def comprobarArray(inputArray):
    # print inputArray
    global gameArray
    global empiezaThor
    global juegoTerminado
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
        s2.write(('t').encode('UTF-8'))
        juegoTerminado = True
        return 10
    elif contador == 0 and turnoNumero == 0:
        empiezaThor = True
        return 99
    else:
        print "Error: <1 diferencia"
        return -1



def mover():
    if turnoNumero==0 and empiezaThor == True:
        randomnum = random.randrange(2)
        if randomnum == 0:
            moverCentro()
        else:
            moverEsquinas()
    elif jugadaDetect():
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

# def moverEsquinas():
#     global casillas
#     for i in [0,2,6,8]:
#         if casillas[i]==0:
#             casillas[i]=2
#             moverPieza(i)
#             return True
#     return False

def moverEsquinas():
    global casillas
    esquinasVacias=[]
    esquinasMolonas=[]
    for i in [0,2,6,8]:
        if casillas[i]==0:
            esquinasVacias.append(i)

    if len(esquinasVacias)==0:
        return False

    elif len(esquinasVacias)==1:
        casillas[esquinasVacias[0]]=2
        moverPieza(esquinasVacias[0])
        return True

    else:
        for k in esquinasVacias:
            if k == 0:
                if casillas[1]==0 and casillas[2]==0 and casillas[3]==0 and casillas[6]==0:
                    esquinasMolonas.append(k)
            if k == 2:
                if casillas[0]==0 and casillas[1]==0 and casillas[5]==0 and casillas[8]==0:
                    esquinasMolonas.append(k)
            if k == 6:
                if casillas[0]==0 and casillas[3]==0 and casillas[7]==0 and casillas[8]==0:
                    esquinasMolonas.append(k)
            if k == 8:
                if casillas[6]==0 and casillas[7]==0 and casillas[2]==0 and casillas[5]==0:
                    esquinasMolonas.append(k)

        if len(esquinasMolonas)>0:
            randomnum = random.randrange(len(esquinasMolonas))
            casillas[esquinasMolonas[randomnum]]=2
            moverPieza(esquinasMolonas[randomnum])
            return True

        else:
            randomnum = random.randrange(len(esquinasVacias))
            casillas[randomnum]=2
            moverPieza(randomnum)
            return True

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
            s1.write(('G01A0B0C0D0X0Y0Z0F1000 \n').encode('UTF-8'))

def moverPieza(pos):
    pillarPieza()
    print moverPiezaCodesUno[pos]
    s1.write((moverPiezaCodesUno[pos]).encode('UTF-8'))
    time.sleep(1)
    print moverPiezaCodesDos[pos]
    s1.write((moverPiezaCodesDos[pos]).encode('UTF-8'))
    time.sleep(1)
    print "M3S100 \n"
    s1.write(('M3S100 \n').encode('UTF-8'))
    time.sleep(1)
    print "G4P0.5\n"
    s1.write(('G4P0.5 \n').encode('UTF-8'))
    time.sleep(1)
    print moverPiezaCodesTres[pos]
    s1.write((moverPiezaCodesTres[pos]).encode('UTF-8'))
    time.sleep(1)

def subirTurno():
    global turnoNumero
    turnoNumero += 1

def pillarPieza():
    print pillarPiezaCodesUno[turnoNumero]
    s1.write((pillarPiezaCodesUno[turnoNumero]).encode('UTF-8'))
    time.sleep(1)
    print pillarPiezaCodesDos[turnoNumero]
    s1.write((pillarPiezaCodesDos[turnoNumero]).encode('UTF-8'))
    time.sleep(1)
    print "M3S900 \n"
    s1.write(('M3S900 \n').encode('UTF-8'))
    time.sleep(1)
    print "G4P1 \n"
    s1.write(('G4P0.5 \n').encode('UTF-8'))
    time.sleep(1)
    print pillarPiezaCodesUno[turnoNumero]
    s1.write((pillarPiezaCodesUno[turnoNumero]).encode('UTF-8'))
    time.sleep(1)


s0=serial.Serial(puerto0,9600)
s1=serial.Serial(puerto1,115200)
s2=serial.Serial(puerto2,9600)

time.sleep(2)
s0.close()
s0.open()
s1.close()
s1.open()
s2.close()
s2.open()

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
s1.write(('G01A0B0C0D0X0Y0Z0F1000 \n').encode('UTF-8'))
s0.close()
s1.close()
s2.close()
