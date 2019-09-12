import numpy as np
import matplotlib.pyplot as plt

axes_values = np.arange(-100, 100, 10)
dx, dy = np.meshgrid(axes_values,
                     axes_values)  # meshgrid is a specific function on the numpy library which groups the point with the other points

print "dx:"
print dx
print "dy:"
print dy
