import numpy as np

a1_1 = np.random.randint(2,10)
a2_1 = np.random.randint(1,5)
a3_1 = np.random.randint(4,8) 
a4_1 = -4.9
t_1 = np.random.randint(1,5)

th_2 = np.random.randint(25,45)
x_2 = np.random.randint(14,18)
y_b_2 = 10; a_2 = -32.2; y_a_2 = 6.8;
d1_2 = np.random.randint(8,12)
d2_2 = np.random.randint(15,17)

v_3 = np.random.randint(40,60)
th_3 = np.random.randint(20,30)

t_4 = np.random.randint(1,5)
C_th = np.random.randint(2,5)
C1_r = np.random.randint(4,8)
C2_r = np.random.randint(-5,-1)

print('1 a) A ball is thrown so that the motion is defined by the equations x = ' + str(a1_1) + 't and y = ' + str(a2_1) + ' + ' + str(a3_1) + 't ' + str(a4_1) + 't² , where x and y are expressed in meters and t is expressed in seconds. Determine the velocity [m/s] at t = ' + str(t_1) + ' s. Rounded to the nearest tenth.')

print('1 b) Calculate the horizontal distance [m] the ball travels before hitting the ground.')

print(' 2 a) A basketball player shoots when she is '+str(x_2)+' ft from the backboard. Knowing that the ball has an initial velocity v₀ at an angle of '+str(th_2)+' deg with the horizontal, determine the value of v₀ [ft/s] when d is equal to '+str(d1_2)+' in. Rounded to the nearest tenth.')

print(' 2 b) Calculate the value of v₀ [ft/s] when d is now equal to '+str(d2_2)+' in. Rounded to the nearest tenth.')

print(' 3 a) A golfer hits a golf ball from point A with an initial velocity of ' + str(v_3) +' m/s at an angle of ' + str(th_3) + '° with the horizontal axis. Determine the radius of curvature [m] of the trajectory described by the ball at point A. Rounded to the nearest tenth.')

print(' 3 b) Determine the radius of curvature [m] at the highest point of the trajectory. Rounded to the nearest tenth.')

print(' 4 a) The oscillation of rod OA about O is defined by the relation θ = ('+ str(C_th) +'/π)(sin πt), where θ and t are expressed in radians and seconds, respectively. Collar B slides along the rod so that its distance from O is r = '+ str(C1_r) +'(1- exp('+ str(C2_r) + 't) ) where r and t are expressed in inches and seconds, respectively. When t = '+str(t_4)+' s, determine the velocity [in/s] of the collar. Rounded to the nearest tenth.')

print(' 4 b) Calculate the acceleration [in/s²] of the collar. Rounded to the nearest tenth.')

input_num1 = Element("Question1")
input_num2 = Element("Question2")
input_num3 = Element("Question3")
input_num4 = Element("Question4")
input_num5 = Element("Question5")
input_num6 = Element("Question6")
input_num7 = Element("Question7")
input_num8 = Element("Question8")

out1 = Element("outputDiv1") 
out2 = Element("outputDiv2") 
out3 = Element("outputDiv3") 
out4 = Element("outputDiv4") 
out5 = Element("outputDiv5")
out6 = Element("outputDiv6")
out7 = Element("outputDiv7") 
out8 = Element("outputDiv8") 

def print_num1(*ags, **kws):
	global pnt1
	x = a1_1*t_1
	x_dot = a1_1
	x_ddot = 0
	y = a2_1 + a3_1*t_1 + a4_1*t_1**2
	y_dot = a3_1 + a4_1*2*t_1
	y_ddot = a4_1*2

	ans1 = round(np.sqrt( x_dot**2 + (y_dot)**2  ),1)
	
	if input_num1.value=='':
		out1.write(f"Blank value provided, please try again.")
	elif input_num1.value == str(ans1):
		out1.write(f"Correct!")
		pnt1 = 1
	else:
		out1.write(f"You typed in {input_num1.value}, that is not correct.")
		pnt1 = 0

def print_num2(*ags, **kws):
	global pnt2
	x = a1_1*t_1
	x_dot = a1_1
	x_ddot = 0
	y = a2_1 + a3_1*t_1 + a4_1*t_1**2
	y_dot = a3_1 + a4_1*2*t_1
	y_ddot = a4_1*2
	y0_dot = a3_1;
	y0 = a2_1;
	y_del = 0 - y0;
	th = np.arctan2(y_dot,x_dot)*180/np.pi

	t1_1b = (-1*y0_dot + np.sqrt( (y0_dot)**2 -4*(-y_del)*(0.5*y_ddot) )) / (2*0.5*y_ddot)
	t2_1b = (-1*y0_dot - np.sqrt( (y0_dot)**2 -4*(-y_del)*(0.5*y_ddot) )) / (2*0.5*y_ddot)

	if t1_1b >= 0:
	    ta = t1_1b
	else:
	    ta = t2_1b

	x_del = ta*x_dot

	ans2 = round(x_del,1)

	if input_num2.value=='':
		out2.write(f"Blank value provided, please try again.")
	elif input_num2.value == str(ans2):
		out2.write(f"Correct!")
		pnt2 = 1
	else:
		out2.write(f"You typed in {input_num2.value}, that is not correct.")
		pnt2 = 0		

def print_num3(*ags, **kws):
	global pnt3
	
	x_del = (x_2 - d1_2/12)
	y = y_b_2 - y_a_2
	th_r = th_2*np.pi/180 # conversion to radians
	v0_2a = np.sqrt(  (0.5*a_2*(x_del**2)/(np.cos(th_r)**2))*(1/(y - x_del*np.tan(th_r))) )

	ans3 = round(v0_2a,1)
	if input_num3.value=='':
		out3.write(f"Blank value provided, please try again.")
	elif input_num3.value == str(ans3):
		out3.write(f"Correct!")
		pnt3 = 1
	else:
		out3.write(f"You typed in {input_num3.value}, that is not correct.")
		pnt3 = 0
def print_num4(*ags, **kws):
	global pnt4
	
	x_del = (x_2 - d2_2/12)
	y = y_b_2 - y_a_2
	th_r = th_2*np.pi/180 # conversion to radians
	v0_2b = np.sqrt(  (0.5*a_2*(x_del**2)/(np.cos(th_r)**2))*(1/(y - x_del*np.tan(th_r))) )
	ans4 = round(v0_2b,1)
	if input_num4.value=='':
		out4.write(f"Blank value provided, please try again.")
	elif input_num4.value == str(ans4):
		out4.write(f"Correct!")
		pnt4 = 1
	else:
		out4.write(f"You typed in {input_num4.value}, that is not correct.")
		pnt4 = 0	

def print_num5(*ags, **kws):
	global pnt5

	th_d = th_3*np.pi/180;

	ans5 = round(v_3**2/(np.cos(th_d)*9.81),1)
	if input_num5.value=='':
		out5.write(f"Blank value provided, please try again.")
	elif input_num5.value == str(ans5):
		out5.write(f"Correct!")
		pnt5 = 1
	else:
		out5.write(f"You typed in {input_num5.value}, that is not correct.")
		pnt5 = 0	

def print_num6(*ags, **kws):
	global pnt6

	th_d = th_3*np.pi/180;
	ans6 = round((v_3*np.cos(th_d))**2/(9.81),1)
	
	if input_num6.value=='':
		out6.write(f"Blank value provided, please try again.")
	elif input_num6.value == str(ans6):
		out6.write(f"Correct!")
		pnt6 = 1
	else:
		out6.write(f"You typed in {input_num6.value}, that is not correct.")
		pnt6 = 0

def print_num7(*ags, **kws):
	global pnt7
	
	th = (C_th/np.pi)*(np.sin(t_4*np.pi))
	th_dot = (C_th/np.pi)*(np.cos(t_4*np.pi))*np.pi
	th_ddot =  (C_th/np.pi)*(np.sin(t_4*np.pi))*np.pi**2*(-1)
	r = C1_r*(1-np.exp(C2_r*t_4))
	r_dot = -C1_r*np.exp(C2_r*t_4)*C2_r
	r_ddot = -C1_r*np.exp(C2_r*t_4)*(C2_r)**2
	vB_er = r_dot
	vB_et = r*th_dot
	v_mag = np.sqrt(vB_er**2 + vB_et**2)

	ans7 = round(v_mag,1)
	if input_num7.value=='':
		out7.write(f"Blank value provided, please try again.")
	elif input_num7.value == str(ans7):
		out7.write(f"Correct!")
		pnt7 = 1
	else:
		out7.write(f"You typed in {input_num7.value}, that is not correct.")
		pnt7 = 0

def print_num8(*ags, **kws):
	global pnt8

	th = (C_th/np.pi)*(np.sin(t_4*np.pi))
	th_dot = (C_th/np.pi)*(np.cos(t_4*np.pi))*np.pi
	th_ddot =  (C_th/np.pi)*(np.sin(t_4*np.pi))*np.pi**2*(-1)
	r = C1_r*(1-np.exp(C2_r*t_4))
	r_dot = -C1_r*np.exp(C2_r*t_4)*C2_r
	r_ddot = -C1_r*np.exp(C2_r*t_4)*(C2_r)**2

	aB_er = r_ddot - r*th_dot**2 
	aB_et =  r*th_ddot +  2*r_dot*th_dot
	a_mag = np.sqrt(aB_er**2 + aB_et**2)

	ans8 = round(a_mag,1)
	if input_num8.value=='':
		out8.write(f"Blank value provided, please try again.")
	elif input_num8.value == str(ans8):
		out8.write(f"Correct!")
		pnt8 = 1
	else:
		out8.write(f"You typed in {input_num8.value}, that is not correct.")
		pnt8 = 0

def clear(*ags, **kws):
	out1 = Element("outputDiv1")
	out2 = Element("outputDiv2")
	out3 = Element("outputDiv3")
	out4 = Element("outputDiv4")
	out5 = Element("outputDiv5")
	out6 = Element("outputDiv6")
	out7 = Element("outputDiv7")
	out8 = Element("outputDiv8")
	out1.clear()	
	out2.clear()
	out3.clear()
	out4.clear()
	out5.clear()
	out6.clear()
	out7.clear()
	out8.clear()
def final_sub(*ags, **kws):
	out1 = Element("outputDiv1")
	out2 = Element("outputDiv2")
	out3 = Element("outputDiv3")
	out4 = Element("outputDiv4")
	out5 = Element("outputDiv5")
	out6 = Element("outputDiv6")
	out7 = Element("outputDiv7")
	out8 = Element("outputDiv8")
	grade = round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7+pnt8)/8)*100,1)
	name = Element('student-name')
	out_final = Element('outputFinal')
	out_final.write(f" Thank you {name.value}, your answers have been submitted. Your score is: {grade} %")
