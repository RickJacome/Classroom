		import numpy as np
		import matplotlib.pyplot as plt
		x = np.linspace(0, 15, 30)
		y = 0.5*x**3 + x - 10
		dydx = (3/2)*x**2 + 1
		dydxx = 3*x 
		noise = np.random.normal(0,2, len(x)) #  
		yn = y + noise
		dyndx = np.gradient(yn,x)
		dyndxx = np.gradient(dyndx,x)

		fig,ax = plt.subplots(nrows=1, ncols=3, dpi=120,figsize=(10,2), constrained_layout=True)
		ax[0].plot(x,y, c='blue'); ax[0].plot(x,yn,'*' ,c='black')
		ax[0].set_ylabel("Position (m)",fontsize=11); 
		ax[0].set_xlabel("Time (sec)", fontsize=11)
		ax[1].plot(x,dydx, c='blue'); ax[1].plot(x,dyndx, '*', c='black')
		ax[1].set_ylabel("Velocity (m/s)",fontsize=11); 
		ax[1].set_xlabel("Time (sec)", fontsize=11)
		ax[2].plot(x,dydxx, c='blue'); ax[2].plot(x,dyndxx,'*', c='black')
		ax[2].set_ylabel("Acceleration (m/s$^{2}$)",fontsize=11);
		ax[2].set_xlabel("Time (sec)", fontsize=11)
		fig
