import numpy as np
import random

a1 = random.randrange(1,10,1)
a2 = random.randrange(-1,-10,-1)
a3 = random.randrange(-5,-15,-1)
a4 = random.randrange(1,10,1)
a5 = random.randrange(1,10,1)


def p1_1(a1,a2,a3,a4,a5):


	t1 = (-1*3*2*a2 + np.sqrt( (3*2*a2)**2 -4*(4*3*a1)*(a3*2) )) / (2*4*3*a1)
	t2 = (-1*3*2*a2 - np.sqrt( (3*2*a2)**2 -4*(4*3*a1)*(a3*2) )) / (2*4*3*a1)

	if t1 >= 0:
	    ta = t1
	else:
	    ta = t2

	v = 4*a1*ta**3 + 3*a2*ta**2 + 2*a3*ta + a4

	x = a1*ta**4 + a2*ta**3 + a3*ta**2 + a4*ta + a5

	return ta,v,x