import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

plt.ioff()

import sys
import string
import random
import time

inputs = sys.argv

# print(inputs)

# INPUTS: none

# OUTPUTS: imageFile


# Load the diabetes dataset
dataset = load_diabetes()

# Use only one feature
dataset_X = dataset.data[:, np.newaxis, 2]

# Split the data into training/testing sets
dataset_X_train = dataset_X[:-20]
dataset_X_test = dataset_X[-20:]

# Split the targets into training/testing sets
dataset_y_train = dataset.target[:-20]
dataset_y_test = dataset.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(dataset_X_train, dataset_y_train)

# Make predictions using the testing set
dataset_y_pred = regr.predict(dataset_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(dataset_y_test, dataset_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(dataset_y_test, dataset_y_pred))

# Plot outputs
plt.scatter(dataset_X_test, dataset_y_test,  color='black')
plt.plot(dataset_X_test, dataset_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

fname = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
fname = ''.join(map(str, ['figs/', fname, time.time(), '.png']))

plt.savefig(fname, bbox_inches='tight')

print(fname)
