import random
import numpy as np
import numpy

def matrizOR():
    beets = [
      [0,0,False],
      [0,1,True],
      [1,0,True],
      [1,1,True]
    ];
    return beets
def matrizAND():
    beets = [
      0,0,'false',
      0,1,'false',
      1,0, 'false',
      1,1, 'true'
    ];


def neurona(beets,epochas,tipo):
    correctas = np.empty(beets, dtype=int)
    cont = 0
    if(tipo == "OR"):
        for i in range(epochas):
            num = random.randint(0,100)
            result = funcion(num)
            if(result == True):
                correctas[cont] = num
                cont = cont + 1
            if(cont == beets):
               return print(correctas)
            
def funcion(num):
    beets = matrizOR()
    newMatriz = [
      [0,0,False],
      [0,1, False],
      [1,0,False],
      [1,1,False]
    ];
    f = 0
    for i in range(len(beets)):
        f = 0
        for j in range(len(beets)-1):
            if(j < 2):
                f = newMatriz[i][j]*num + f
            else:
                if(f > num):
                    newMatriz[i][j] = True
                else:
                    newMatriz[i][j] = False
            # print(newMatriz[i][j])
    return numpy.array_equal(newMatriz, beets, equal_nan=False)
            
# 
arreglo = neurona(2,100,'OR')

