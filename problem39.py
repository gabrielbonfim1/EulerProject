import numpy as np
from numba import jit,cuda
from numba import vectorize
from timeit import default_timer as timer
import itertools


def test(a,b,c):

    x=0
    for i in a:
        for j in b:
            t = (((i**2) + (j**2))**(0.5))+i+j
            if t.is_integer():
                c[x] = int(t)

            x+=1




n=1001
a = np.arange(3,n)
b = np.arange(4,n)
c = np.zeros(a.size*b.size,dtype=int)
test(a,b,c)
c = c[c!=0]
c=c[c<1001]
counts = np.bincount(c)
print(np.argmax(counts))






