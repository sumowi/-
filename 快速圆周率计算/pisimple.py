import numpy as np
simpi = lambda num: len(filter(lambda pt: pt[0]*pt[0]+pt[1]*pt[1]<1, np.reshape(np.random.uniform(size=2*num), [num, 2])))/float(num)*4
print(simpi(1000000),file=open("pisimple.txt","w"))