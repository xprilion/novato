import numpy as np

filename = "../datasets/xor.csv"
a = np.loadtxt(open(filename, "rb"), delimiter=",")

print(a.shape)
