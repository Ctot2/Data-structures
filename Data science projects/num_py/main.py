import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.arange(10)
z = np.zeros(100)
a = z[:].copy()
a[99] = 1
b = y[:5]
print (b)
