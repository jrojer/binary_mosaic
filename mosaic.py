# coding: utf-8
import numpy as np
def isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def printM(M):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i][j] == True:
                print('\u2588\u2588',end='')
            else:
                print('\u2591\u2591',end='')
        print()
        
        
def getM(shape,op,test):
    M = np.zeros(shape=shape,dtype=np.bool)
    for x,y in np.ndindex(M.shape):
        if test(op(x,y)):
            M[x][y] = True
    return M


if name=='main':
    R = np.random.randint(0,2,512)
    printM(getM((500,500),lambda x,y:x|y,lambda x: R[x]))
