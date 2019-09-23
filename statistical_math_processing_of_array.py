import numpy as np
import matplotlib.pyplot as plt

axes_values = np.arange(-100, 100, 10)
dx, dy = np.meshgrid(axes_values, axes_values)  # meshgrid is a specific function on the numpy library which groups the point with the other points

# print("dx:")
# print(dx)
# print("dy:")
# print(dy)

function = 2*dx+3*dy
function2 = np.cos(dx) + np.cos(dy)
print(function)
# plt.imshow(function)
plt.imshow(function2)
# plt.title("function of plot 2*dx+3*dy")
plt.title("function cos ploy")
plt.colorbar()
# plt.savefig('myfig.png')
plt.savefig('myfig4.png')
