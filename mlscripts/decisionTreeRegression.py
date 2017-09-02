# Import the necessary modules and libraries
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

plt.ioff()

import sys
import string
import random
import time

inputs = sys.argv

# print(inputs)

# INPUTS: precision | 

# OUTPUTS: imageFile

# Create a random dataset
rng = np.random.RandomState(2)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# Fit regression model
precision = int(inputs[1])
# precision = 3
regr_2 = DecisionTreeRegressor(max_depth = precision)
'''regr_1.fit(X, y)'''
regr_2.fit(X, y)

# Predict
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_2 = regr_2.predict(X_test)

# Plot the results
plt.figure()
plt.scatter(X, y, s=20, edgecolor="black",
c="darkorange", label="data")
plt.plot(X_test, y_2, color="yellowgreen", label=precision, linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()

fname = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
fname = ''.join(map(str, ['figs/', fname, time.time(), '.png']))

plt.savefig(fname, bbox_inches='tight')

print(fname)