import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
def rosenbrock(x,y):
    return 1 * (y - x**2)**2 + (1 - x)**2

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
Zr = rosenbrock(X,Y)
#fig = plt.figure()
#ax = plt.axes(projection='3d')

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

ax1.contour3D(X, Y, Z, 50, cmap='viridis')
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('z');

ax2.contour3D(X, Y, Zr, 50, cmap='inferno')
ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('z');

ax3.contour3D(X, Y, Z, 50, cmap='binary')
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z');

fig
