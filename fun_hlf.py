import numpy as np
import math 
import random
tablero_jugador=np.full((10,10),' ')

def barcos_jugador (barcos):
    for i in barcos:
        for a in i:
            tablero_jugador[a]= 'O'
    print("asi estaran ubicados sus barcos")
    return tablero_jugador  


barco_maquina = []
def generar_b_aleatorio(eslora):

    barco_maq = []
    
    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    while (fila_random, columna_random) in barco_maquina:
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
    orien = random.choice(["Norte", "Sur", "Este", "Oeste"])
    if (columna_random+eslora)>9 and orien=="Este":
        orien="Oeste"
    elif (fila_random+eslora)>9 and orien=="Sur":
        orien="Norte"
    elif (columna_random-eslora)<0 and orien=="Oeste":
        orien="Este"
    elif (fila_random-eslora)<0 and orien=="Norte":
        orien="Sur"
    barco_maquina.append((fila_random,columna_random))
    barco_maq.append((fila_random,columna_random))     


    while len(barco_maq) < eslora:
        if orien == "Norte":
                fila_random = fila_random - 1
        if orien == "Sur":
                fila_random = fila_random + 1
        if orien == "Este":
                columna_random = columna_random + 1
        if orien == "Oeste":
                columna_random = columna_random - 1
        barco_maquina.append((fila_random,columna_random))
        barco_maq.append((fila_random,columna_random))

    return barco_maq

  
tablero_maquina_2=np.full((10,10),' ')
tablero_maquina_1=np.full((10,10),' ')
barco_maquina = []
def tablero_maquina():
  
    a=1
    generar_b_aleatorio(4)

    while a<=4:
        generar_b_aleatorio(1)
        if a<=2:
            generar_b_aleatorio(3)
        if a<4:
            generar_b_aleatorio(2)

        a=a+1
    for i in barco_maquina:
        tablero_maquina_1[i]= "O"
    return tablero_maquina_1


def disparar(fila,columna):
    if tablero_maquina_1[fila,columna] == "O":
        print("Has acertado")
        tablero_maquina_1[fila,columna] = "X"
        tablero_maquina_2[fila,columna] = "X"
        fila=int(input("escoja fila: "))
        columna=int(input("escoja columna: "))
        disparar(fila,columna)
    elif tablero_maquina_1[fila,columna] == " ":
        print("Has fallado")
        tablero_maquina_1[fila,columna] = "-"
        tablero_maquina_2[fila,columna] = "-"
    elif tablero_maquina_1[fila,columna] == "-" or tablero_maquina_1[fila,columna] == "X":
        print("capitan ya disparo a ese lugar antes, tomese este combate enserio")
        fila=int(input("escoja fila: "))
        columna=int(input("escoja columna: "))
        disparar(fila,columna)
    return tablero_maquina_2

registro_disparos=[]
def disparo_maquina ():
    fila_disparo = random.randint(0,9)
    columna_disparo = random.randint(0,9)
    while (fila_disparo, columna_disparo) in registro_disparos:
        fila_disparo= random.randint(0,9)
        columna_disparo = random.randint(0,9)
    registro_disparos.append([fila_disparo,columna_disparo])
    if tablero_jugador[fila_disparo,columna_disparo] == "O":
        print("Él enemigo ha acertado")
        tablero_jugador[fila_disparo,columna_disparo] = "X"
        disparo_maquina()
    elif tablero_jugador[fila_disparo,columna_disparo] == " ":
        print("Él enemigo ha fallado")
        tablero_jugador[fila_disparo,columna_disparo] = "-"
    return tablero_jugador


