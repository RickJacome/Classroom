import numpy as np
import matplotlib.pyplot as plt

#def underdamped_shm(m, k, b, x0, v0, t):
#    """Simulates underdamped simple harmonic motion."""
#    omega0 = np.sqrt(k/m)
#    zeta = b/(2*np.sqrt(k*m))
#    omega = omega0 * np.sqrt(1 - zeta**2)
#
#    x = x0 * np.exp(-zeta * omega0 * t) * np.cos(omega * t - np.arctan(zeta / np.sqrt(1 - zeta**2)))
#    return x


def plotting():
	# Parameters
	m = 1.0  # Mass
	k = 10.0  # Spring constant
	b = 0.5  # Damping coefficient
	x0 = 1.0  # Initial displacement
	v0 = 0.0  # Initial velocity
	omega0 = np.sqrt(k/m)
	zeta = b/(2*np.sqrt(k*m))
	omega = omega0 * np.sqrt(1 - zeta**2)
	x = x0 * np.exp(-zeta * omega0 * t) * np.cos(omega * t - np.arctan(zeta / np.sqrt(1 - zeta**2)))

	# Time array
	t = np.linspace(0, 10, 1000)

	# Calculate displacement
	x = underdamped_shm(m, k, b, x0, v0, t)
	# Plotting
	plt.plot(t, x)
	plt.xlabel('Time (s)'); plt.ylabel('Displacement (m)')
	plt.title('Underdamped Simple Harmonic Motion'); plt.show()

	display(fig, target="graph-area", append=False)