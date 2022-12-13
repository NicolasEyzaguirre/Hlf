
from fun_hlf import *

print("bienvenido al juego de battleship")
nombre_jugador=input("por favor introduzcas su nombre de jugador: ")
print("los barcos se pondran de manera aleatoria")

print(barcos_jugador(([(0,1), (1,1)] , [(0,9), (1,9)] , [(9,1), (9,2)] , [(4,3), (4,4), (4,5), (4,6)]  , [(1,3), (1,4), (1,5)] , [(9,4), (9,5), (9,6)] , [(5,1)] , [(4,6)] ,[(5,8)] , [(7,7)]))) 
tablero_maquina_2=np.full((10,10),' ')
tablero_maquina_1=np.full((10,10),' ')
barco_maquina = []
tablero_maquina()
print('tanto las filas como las columnas estaran enumeradas del 0 - 9, tenga en cuenta esto a la hora de disparar.')
while "O" in tablero_jugador or "O" in tablero_maquina_1:
    columna=int(input("escriba a que columna va a dispar: "))
    fila=int(input("escriba a que fila va a dispar: "))
    print(disparar(columna,fila))
    print(disparo_maquina())
   
if "O" not in tablero_jugador:
    print("has perdido "+ nombre_jugador + " has decepcionado a toda una nacion")
if "O" not in tablero_maquina_1:
    print("has ganado "+ nombre_jugador)