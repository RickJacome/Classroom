import numpy as np

th_2_2= np.random.randint(65,75)
th_2 = 90 - th_2_2  
th_r_2 = th_2*np.pi/180
v_A_2 = np.random.randint(42,48)
v_B_2 = np.random.randint(25,35)

mu_4 = np.random.randint(6,10)/10
x_4 = np.random.randint(50,70)
W_f_4 = np.random.randint(55,65)
W_r_4 = 100 - W_f_4
g = 9.81

paraQ1a = Element("Q1a")
paraQ1a.write(f"1 a) Slider Block B moves to the right with a constant velocity of 300 mm/s. Determine the velocity [mm/s] of slider block A. Rounded to the nearest tenth.")

paraQ1b = Element("Q1b")
paraQ1b.write(f" 1 b) Calculate the velocity [mm/s] of portion C of the cable. Rounded to the nearest tenth.")

paraQ1c = Element("Q1c")
paraQ1c.write(f" 1 c) Find the relative velocity [mm/s] of portion C of the cable with respect to slider block A. Rounded to the nearest tenth.")

paraQ2a = Element("Q2a")
paraQ2a.write(f" 2 a) 3 seconds after car B passes through the intersection shown, car A passes through the same intersection. Knowing that the speed of each car is constant, determine the relative velocity [mph] of B with respect to A. Rounded to the nearest tenth.")

paraQ2b = Element("Q2b")
paraQ2b.write(f" 2 b) State the direction [degrees] with respect to the horizontal of the velocity calculated in part 2a.  Rounded to the nearest tenth.")

paraQ2c = Element("Q2c")
paraQ2c.write(f" 2 c) Calculate the change in position [miles] of B with respect to A during a 4 second interval. Rounded to the nearest tenth.")

paraQ3a = Element("Q3a")
paraQ3a.write(f" 3 a) Race car A is traveling on a straight portion of the track while race car B is traveling on a circular portion of the track. At the instant shown, the speed of A is increasing at the rate of 10 m/s², and the speed of B is decreasing at the rate of 6 m/s². For the position shown, determine the velocity [m/s²] of B relative to A. Rounded to the nearest tenth. ")

paraQ3b = Element("Q3b")
paraQ3b.write(f" 3 b)  State the direction [degrees] with respect to the horizontal of the velocity calculated in part 3a.  Rounded to the nearest tenth. ")

paraQ3c = Element("Q3c")
paraQ3c.write(f" 3 c) Calculate the acceleration [m/s²] of B relative to A. Rounded to the nearest tenth. ")

paraQ3d = Element("Q3d")
paraQ3d.write(f" 3 d) State the direction [degrees] with respect to the horizontal of the acceleration calculated in part 3c. Rounded to the nearest tenth. ")

paraQ4a = Element("Q4a")
paraQ4a.write(f" 4 a) Determine the maximum theoretical speed [m/s] that may be achieved over a distance of 60 m by a car starting from rest, knowing that the coefficient of static friction is 0.80 between the tires and the pavement, and that 60% of the weight of the car is distributed over its front wheels and 40% over its rear wheels. Assume a four-wheel drive. Rounded to the nearest tenth. ")

paraQ4b = Element("Q4b")
paraQ4b.write(f" 4 b) Determine the maximum theoretical speed [m/s]  now assuming a front-wheel drive. Rounded to the nearest tenth. ")

paraQ4c = Element("Q4c")
paraQ4c.write(f" 4 c) Determine the maximum theoretical speed [m/s]  now assuming a rear-wheel drive. Rounded to the nearest tenth. ")


input_num1 = Element("Question1")
input_num2 = Element("Question2")
input_num3 = Element("Question3")
input_num4 = Element("Question4")
input_num5 = Element("Question5")
input_num6 = Element("Question6")
input_num7 = Element("Question7")
input_num8 = Element("Question8")
input_num9 = Element("Question9")
input_num10 = Element("Question10")
input_num11 = Element("Question11")
input_num12 = Element("Question12")
input_num13 = Element("Question13")

out1 = Element("outputDiv1") 
out2 = Element("outputDiv2") 
out3 = Element("outputDiv3") 
out4 = Element("outputDiv4") 
out5 = Element("outputDiv5")
out6 = Element("outputDiv6")
out7 = Element("outputDiv7") 
out8 = Element("outputDiv8")
out9 = Element("outputDiv9")
out10 = Element("outputDiv10")
out11 = Element("outputDiv11") 
out12 = Element("outputDiv12")
out13 = Element("outputDiv13")

def print_num1(*ags, **kws):
	global pnt1
	global ans1
	t1 = (-1*3*2*a2 + np.sqrt( (3*2*a2)**2 -4*(4*3*a1)*(a3*2) )) / (2*4*3*a1)
	t2 = (-1*3*2*a2 - np.sqrt( (3*2*a2)**2 -4*(4*3*a1)*(a3*2) )) / (2*4*3*a1)

	if t1 >= 0:
	    ans1 = round(t1,2)
	else:
	    ans1 = round(t2,2)

	if input_num1.value=='':
		out1.write(f"Blank value provided, please try again.")
	elif input_num1.value == str(ans1):
		out1.write(f"Correct!")
		pnt1 = 1
	else:
		out1.write(f"You typed in {input_num1.value}, that is not correct")
		pnt1 = 0
def print_num2(*ags, **kws):
	global pnt2
	ans2 = round(4*a1*ans1**3 + 3*a2*ans1**2 + 2*a3*ans1 + a4,1)
	
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
	ans3 = round(a1*ans1**4 + a2*ans1**3 + a3*ans1**2 + a4*ans1 + a5 ,1)
	
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
	global ans4
	ans4 = round(np.sqrt((v_A_2*np.cos(th_r_2))**2 + (v_B_2+v_A_2*np.sin(th_r_2))**2),1)
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
	ans5 = round(np.arctan2(v_B_2+v_A_2*np.sin(th_r_2) , v_A_2*np.cos(th_r_2) )*180/np.pi,1)
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
	ans6 = round(2,1)
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
	ans7 = round(2*x2/t2,1)
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
	ans8 = round(2*x2/t2,1)
	if input_num8.value=='':
		out8.write(f"Blank value provided, please try again.")
	elif input_num8.value == str(ans8):
		out8.write(f"Correct!")
		pnt8 = 1
	else:
		out8.write(f"You typed in {input_num8.value}, that is not correct.")
		pnt8 = 0

def print_num9(*ags, **kws):
	global pnt9
	ans9 = round(-ans4/a,1)
	if input_num9.value=='':
		out9.write(f"Blank value provided, please try again.")
	elif input_num9.value == str(ans9):
		out9.write(f"Correct!")
		pnt9 = 1
	else:
		out9.write(f"You typed in {input_num9.value}, that is not correct.")
		pnt9 = 0	

def print_num10(*ags, **kws):
	global pnt10
	ans10 = round(2*x2/t2**2,1)
	if input_num10.value=='':
		out10.write(f"Blank value provided, please try again.")
	elif input_num10.value == str(ans10):
		out10.write(f"Correct!")
		pnt10 = 1
	else:
		out10.write(f"You typed in {input_num10.value}, that is not correct.")
		pnt10 = 0

def print_num11(*ags, **kws):
	global pnt11
	ans11 = round(np.sqrt(2*mu_4*g*x_4),1)
	if input_num11.value=='':
		out11.write(f"Blank value provided, please try again.")
	elif input_num11.value == str(ans11):
		out11.write(f"Correct!")
		pnt11 = 1
	else:
		out11.write(f"You typed in {input_num11.value}, that is not correct.")
		pnt11 = 0

def print_num12(*ags, **kws):
	global pnt12
	ans12 = round(np.sqrt(2*(W_f_4/100)*mu_4*g*x_4),1)
	if input_num12.value=='':
		out12.write(f"Blank value provided, please try again.")
	elif input_num12.value == str(ans12):
		out12.write(f"Correct!")
		pnt12 = 1
	else:
		out12.write(f"You typed in {input_num12.value}, that is not correct.")
		pnt12 = 0

def print_num13(*ags, **kws):
	global pnt13
	ans13 = round(np.sqrt(2*(W_r_4/100)*mu_4*g*x_4),1)
	if input_num13.value=='':
		out13.write(f"Blank value provided, please try again.")
	elif input_num13.value == str(ans13):
		out13.write(f"Correct!")
		pnt13 = 1
	else:
		out13.write(f"You typed in {input_num13.value}, that is not correct.")
		pnt13 = 0

def clear(*ags, **kws):
	out1 = Element("outputDiv1")
	out2 = Element("outputDiv2")
	out3 = Element("outputDiv3")
	out4 = Element("outputDiv4")
	out5 = Element("outputDiv5")
	out6 = Element("outputDiv6")
	out7 = Element("outputDiv7")
	out8 = Element("outputDiv8")
	out9 = Element("outputDiv9")
	out10 = Element("outputDiv10")
	out11 = Element("outputDiv11")
	out12 = Element("outputDiv12")
	out13 = Element("outputDiv13")

	out1.clear()	
	out2.clear()
	out3.clear()
	out4.clear()
	out5.clear()
	out6.clear()
	out7.clear()
	out8.clear()
	out8.clear()
	out9.clear()
	out10.clear()
	out11.clear()
	out12.clear()
	out13.clear()	

def final_sub(*ags, **kws):
	out1 = Element("outputDiv1")
	out2 = Element("outputDiv2")
	out3 = Element("outputDiv3")
	out4 = Element("outputDiv4")
	out5 = Element("outputDiv5")
	out6 = Element("outputDiv6")
	out7 = Element("outputDiv7")
	out8 = Element("outputDiv8")
	out9 = Element("outputDiv9")
	out10 = Element("outputDiv10")
	out11 = Element("outputDiv11")
	out12 = Element("outputDiv12")
	out13 = Element("outputDiv13")	
	name = Element('student-name')
	out_final = Element('outputFinal')
	
	try:
		round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7+pnt8+pnt9+pnt10+pnt11+pnt12+pnt13)/13)*100,1)
	except NameError:
		out_final.write(f"You did not finish submitting all questions above. Refresh Page and start again. ")

	grade = round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7+pnt8+pnt9+pnt10+pnt11+pnt12+pnt13)/13)*100,1)

	out_final.write(f" Thank you {name.value}, your answers have been submitted. Your score is: {grade} %")

