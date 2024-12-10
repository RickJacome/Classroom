import numpy as np
import matplotlib.pyplot as plt

def underdamped_shm(m, k, b, x0, v0, t):
    """Simulates underdamped simple harmonic motion."""
    omega0 = np.sqrt(k/m)
    zeta = b/(2*np.sqrt(k*m))
    omega = omega0 * np.sqrt(1 - zeta**2)
    x = x0 * np.exp(-zeta * omega0 * t) * np.cos(omega * t - np.arctan(zeta / np.sqrt(1 - zeta**2)))
    return x
#def plotting():
# Parameters
m = 1.0  # Mass
k = 10.0  # Spring constant
b = 0.5  # Damping coefficient
x0 = 1.0  # Initial displacement
v0 = 0.0  # Initial velocity

t = np.linspace(0, 10, 1000)
# Calculate displacement
x = underdamped_shm(m, k, b, x0, v0, t)
# Plotting
fig, ax = plt.subplots(1,3, dpi=120,figsize=(10,2), constrained_layout=True)

ax[0].plot(t, x)
ax[1].plot(t, x)
ax[2].plot(t, x)

ax[0].set_xlabel('Time (s)');  ax[0].set_ylabel('Displacement (m)'); ax[0].set_title('Underdamped');

ax[1].set_xlabel('Time (s)');  ax[1].set_ylabel('Displacement (m)'); ax[1].set_title('Damped');

ax[2].set_xlabel('Time (s)');  ax[2].set_ylabel('Displacement (m)'); ax[2].set_title('Underdamped');

fig

plt.figure()
x = np.linspace(0, 10, 100)
y = np.sin(x)
# Create the figure and axes
fig1, ax1 = plt.subplots()
# Animation function
def animate(i):
    line.set_ydata(np.sin(x + i/10))
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)
# Save the animation as a GIF
ani.save('animation.gif', writer='pillow')

fig1

