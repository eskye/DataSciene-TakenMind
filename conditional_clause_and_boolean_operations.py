import numpy as np

x = np.array([100, 400, 500, 600])  # each number 'a'
y = np.array([10, 15, 20, 25])  # each number 'b'
condition = np.array([True, True, False, False])

# use loops indirectly to perform this

z = [a if cond else b for a, cond, b in zip(x, condition, y)]
print z

# np.where(#condition, #value for yes, #value for No)
z2 = np.where(condition, x, y)
print z2

z3 = np.where(x > 0, 0, 1)
print z3
