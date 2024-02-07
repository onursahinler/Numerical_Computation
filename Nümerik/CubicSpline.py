import numpy as np
from scipy.interpolate import CubicSpline

# given points
x = np.array([0, 1, 2])
y = np.array([3, -2, 1])

# create a cubic spline interpolation
cs = CubicSpline(x, y, bc_type='natural')

# print the cubic spline polynomials
for i in range(len(x)-1):
    print(f"For the interval [{x[i]}, {x[i+1]}]:")
    print(cs.c[:,i])