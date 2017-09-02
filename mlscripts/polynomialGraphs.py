import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.ioff()

import sys
import random
import time
import string


x = np.arange(-100, 100, 0.25)
y = np.arange(-100, 100, 0.25)
X, Y = np.meshgrid(x, y)

inputs = sys.argv[1:]

# print(inputs)

# INPUTS: precision | 

# OUTPUTS: imageFile

#filename = int(inputs[0])

a,b,c,d,e,f = map(int,inputs)

Force= a*X*X + b*Y*Y + c*X*Y + d*X + e*Y + f 


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Force)


fname = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
fname = ''.join(map(str, ['figs/', fname, time.time(), '.png']))


plt.savefig(fname, bbox_inches='tight')

print(fname)
