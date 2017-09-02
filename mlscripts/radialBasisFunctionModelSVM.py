import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.svm import SVR 

plt.ioff()

import sys
import string
import random
import time

inputs = sys.argv

# print(inputs)

# INPUTS: RBF parameters 

# OUTPUTS: imageFile
 
np.random.seed(0) 
X = np.sort(5 * np.random.rand(40, 1), axis=0) 
T = np.linspace(0, 5, 500)[:, np.newaxis] 
y = np.sin(X).ravel() 
 
# Add noise to targets 
y[::5] += 1 * (0.5 - np.random.rand(8)) 
 
# Fit RBF Model 
R_rbf = int(inputs[1]) 
for i, weights in enumerate(['uniform', 'distance']): 
    svr_rbf = SVR(kernel='rbf',C=1e3,gamma=0.1)
    y_ = svr_rbf.fit(X,y).predict(T)
     
plt.subplot(2, 1, i + 1) 
plt.scatter(X, y, c='k', label='data') 
plt.plot(T, y_, c='r', label='prediction') 
plt.axis('tight') 
plt.legend() 
plt.title("Radial Basis Function (k = %i, weights = '%s')" % (R_rbf, 
weights)) 

fname = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
fname = ''.join(map(str, ['figs/', fname, time.time(), '.png']))

plt.savefig(fname, bbox_inches='tight')

print(fname)
