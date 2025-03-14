import numpy as np
a1 = np.random.randint(1,10)
a2 = np.random.randint(-10,-1)
a3 = np.random.randint(-15,-5)
a4 = np.random.randint(1,10)
a5 = np.random.randint(1,10)
v =0 ;
a2a = np.random.randint(-15,-1)
x2a = np.random.randint(150,230)

t3a = np.random.randint(25,35)
x3a = np.random.randint(800,950)

v4a = np.random.randint(50,60)
t4a = np.random.randint(25,35)
d4a = np.random.randint(800,950)

paraQ1a = Element("Q1a")
paraQ1a.write(f"1 a) The motion of a particle is defined by x = {a1}t⁴ - {np.abs(a2)}t³ - {np.abs(a3)}t² + {a4}t + {a5}. Where x and t are in meters and seconds respectively. Determine the time [s] at which acceleration is zero. Rounded to the nearest hundred.")

paraQ1b = Element("Q1b")
paraQ1b.write(f"1 b) What is the velocity [m/s] of the particle at this time? Rounded to the nearest tenth.")

paraQ1c = Element("Q1c")
paraQ1c.write(f"1 c) What is the position [m] of the particle at this time? Rounded to the nearest tenth.")

paraQ2a = Element("Q2a")
paraQ2a.write(f"2 a) A car is driving at constant speed and starts applying the braking, causing it to slow down at a rate of {np.abs(a2a)} ft/s². If the car stops in {x2a} ft, determine how fast the car was traveling immediately before applying the brakes [m/s]. Rounded to the nearest tenth.")

paraQ2b = Element("Q2b")
paraQ2b.write(f"2 b) Calculate the time required for the car to come to a stop [s]. Rounded to the nearest tenth.")

paraQ3a = Element("Q3a")
paraQ3a.write(f"3 a) An airplane begins its take-off run at A with zero velocity and a constant acceleration a. Knowing that the airplane becomes airbone {t3a}s later at B and that the distance AB is {x3a} m. Determine the acceleration a [m/s²]. Rounded to the nearest tenth.")

paraQ3b = Element("Q3b")
paraQ3b.write(f"3 b) What is the take-off velocity [m/s] of the airplane? Rounded to the nearest tenth.")

paraQ4a = Element("Q4a")
paraQ4a.write(f"4 a) A motorist is traveling at {v4a} km/h and observers that a traffic light {d4a} m ahead has turned red. The traffic light is timed to stay red {t4a} s. If the motorist wishes to pass the light without stopping just as it turns green again, determine the required uniform deceleration [m/s²] of the car for it to cross without stopping. Rounded to the nearest hundred.")

paraQ4b = Element("Q4b")
paraQ4b.write(f"4 b) What is the velocity [m/s] of the car as it passes the light? Rounded to the nearest tenth.")

input_num1 = Element("Question1")
input_num2 = Element("Question2")
input_num3 = Element("Question3")
input_num4 = Element("Question4")
input_num5 = Element("Question5")
input_num6 = Element("Question6")
input_num7 = Element("Question7")
input_num8 = Element("Question8")
input_num9 = Element("Question9")


out1 = Element("outputDiv1") 
out2 = Element("outputDiv2") 
out3 = Element("outputDiv3") 
out4 = Element("outputDiv4") 
out5 = Element("outputDiv5")
out6 = Element("outputDiv6")
out7 = Element("outputDiv7") 
out8 = Element("outputDiv8") 
out9 = Element("outputDiv9")  


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
	ans4 = round(np.sqrt(v**2-2*a2a*x2a),1)
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
	ans5 = round(-ans4/a2a,1)
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
	ans6 = round(2*x3a/t3a**2,1)
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
	ans7 = round(2*x3a/t3a,1)
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
	global ans8
	ans8 = round((d4a - (v4a*10/36)*t4a)*2/t4a**2,1)
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
	ans9 = round(np.sqrt((v4a*10/36)**2 + 2*d4a*ans8),1)
	if input_num9.value=='':
		out9.write(f"Blank value provided, please try again.")
	elif input_num9.value == str(ans9):
		out9.write(f"Correct!")
		pnt9 = 1
	else:
		out9.write(f"You typed in {input_num9.value}, that is not correct.")
		pnt9 = 0

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

	out1.clear()	
	out2.clear()
	out3.clear()
	out4.clear()
	out5.clear()
	out6.clear()
	out7.clear()
	out8.clear()
	out9.clear()

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

	name = Element('student-name')
	out_final = Element('outputFinal')
	try:
		round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7+pnt8+pnt9)/9)*100,1)
	except NameError:
		out_final.write(f"You did not finish submitting all questions above. Refresh Page and start again. ")
	grade = round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7+pnt8+pnt9)/9)*100,1)
	out_final.write(f" Thank you {name.value}, your answers have been submitted. Your score is: {grade} %")
