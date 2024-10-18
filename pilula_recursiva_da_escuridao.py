import os
import time
import random
import threading
# 30 x 8 = 240

matriz = "---------------------------\n|     A B C D E F G       |\n|     H I J K L M N       |\n|     O P Q R S T U       |\n|     V X Y Z R R R       |\n|     R R R R R R R       |\n|     R R R R R R R       |\n---------------------------\n"


def dark_painting(pos,matriz):
    if i == None:
        return matriz
    else:
        return matriz[:pos-1] + "*" + matriz[pos:]


def pilula_recursiva(i,matriz,aux):
    if matriz[i] == "*" or matriz[i] == "-" or matriz[i] == "|" or matriz[i-1] == "|" or matriz[i-1] == "-":
        i = random.randint(1,len(matriz)-1)

        if aux < 100:
            print(aux)
            pilula_recursiva(i,matriz,aux+1)
        else:
            return 666
    else:
        return i


seconds = 0
darkness = False
while (not darkness):
    #print(f"Time: {seconds}s")
    i = random.randint(1,len(matriz)-1)
    i = pilula_recursiva(i,matriz,1)
    if i != 666:
        os.system("cls")
        matriz = dark_painting(i,matriz)
        print(matriz)
        time.sleep(0.07)
        seconds += 1
    else:
        darkness = True
    