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
x = underdamped_shm(m, k, b, x0, v0, t)
dx_dt = np.diff(x)/np.diff(t)

fft_result = np.fft.fft(x)
freq = np.fft.fftfreq(len(x), 0.01)
# Plotting
fig, ax = plt.subplots(1,3, dpi=120,figsize=(10,2), constrained_layout=True)

ax[0].plot(t, x)
ax[1].plot(t, dx_dt)
ax[2].plot(freq, fft_result)

ax[0].set_xlabel('Time (sec)');  ax[0].set_ylabel('Displacement (m)'); ax[0].set_title('Theoretical Underdamped System');
ax[1].set_xlabel('Time (sec)');  ax[1].set_ylabel('Velocity (mm/s)'); ax[1].set_title('Derivative of Theoretical System');
ax[2].set_xlabel('Frequency (Hz)');  ax[2].set_ylabel('Amplitude'); ax[2].set_title('Fast Fourier Transform');

fig

