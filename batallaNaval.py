__author__ = 'User'
# -*- coding: utf-8 -*-

#Batalla Naval Game
import random

tablero = []

for x in range(0,5):
  tablero.append(["O"] * 5)

def print_tablero(tablero):
  for fila in tablero:
    print (" ".join(fila))

print ("¡Juguemos batalla naval!")
print_tablero(tablero)

def fila_aleatoria(tablero):
  return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero):
  return random.randint(0,len(tablero[0])-1)

barco_fila = fila_aleatoria(tablero)
barco_col = columna_aleatoria(tablero)
#print (barco_fila)
#print (barco_col)

for turno in range(0,4):
    adivina_fila = int(input("Adivina fila:"))
    adivina_columna = int(input("Adivina columna:"))
    if adivina_fila == barco_fila and adivina_columna == barco_col:
        print ("¡Felicitaciones! ¡Hundiste mi barco!")
        break
    else:
        if (adivina_fila < 0 or adivina_fila > 4) or (adivina_columna < 0 or adivina_columna > 4):
            print ("Vaya, esto ni siquiera está en el océano.")
        elif(tablero[adivina_fila][adivina_columna] == "X"):
            print ("Ya dijiste esa.")
        else:
            print ("¡No impactaste mi barco!")
            tablero[adivina_fila][adivina_columna] = "X"
            print_tablero(tablero)
    print ("Turno: "+str(turno + 1))
    if (turno == 4):
        print ("Terminó el juego")
        break
