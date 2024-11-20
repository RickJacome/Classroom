import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

#fig = plt.figure()
#ax = plt.axes(projection='3d')

fig, ax = plt.subplots(1,3, dpi=120,figsize=(10,2), constrained_layout=True)
ax[0] = plt.axes(projection='3d')

ax[0].contour3D(X, Y, Z, 50, cmap='binary')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_zlabel('z');

fig
