import os
import time
import random
# 30 x 8 = 240

matriz = f"""
    --------------------------
    |     A B C D E F G      |
    |     H I J K L M N      |  
    |     O P Q R S T U      |
    |     V X Y Z R R R      | 
    |     R R R R R R R      |
    |     R R R R R R R      | 
    --------------------------
"""

def dark_painting(pos,matriz):
    if i == None:
        return matriz
    else:
        return matriz[:pos-1] + "*" + matriz[pos:]


def pilula_recursiva(i,matriz,aux):
    if matriz[i] == "*":
        i = random.randint(1,240)

        if aux < 100:
            print(aux)
            pilula_recursiva(i,matriz,aux+1)
            
        else:
            return 666
    else:
        return i


darkness = False
while (not darkness):
    i = random.randint(1,240)
    i = pilula_recursiva(i,matriz,1)
    if i != 666:
        os.system("cls")
        matriz = dark_painting(i,matriz)
        print(matriz)
        time.sleep(0.1)
    else:
        darkness = True
    