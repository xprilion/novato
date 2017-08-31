
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.svm import SVR
 
np.random.seed(0) 
X = np.sort(5 * np.random.rand(40, 1), axis=0) 
T = np.linspace(0, 5, 500)[:, np.newaxis] 
y = np.sin(X).ravel() 
 
# Add noise to targets 
y[::5] += 1 * (0.5 - np.random.rand(8)) 
 
# Fit RBF Model 
polynomial_svm = int(input('n_neighbour parameters:')) 
for i, weights in enumerate(['uniform', 'distance']): 
    svr_poly = SVR(kernel='poly',C=1e3,degree=2)
    y_ = svr_poly.fit(X,y).predict(T)
     
plt.subplot(2, 1, i + 1) 
plt.scatter(X, y, c='k', label='data') 
plt.plot(T, y_, c='b', label='prediction') 
plt.axis('tight') 
plt.legend() 
plt.title("PolynomialSupportVectorRegression (k = %i, weights = '%s')" % (polynomial_svm, 
weights)) 
plt.show() 
