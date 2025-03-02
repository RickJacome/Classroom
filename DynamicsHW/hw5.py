import numpy as np
# Define variables here


print('1 a)  A 0.2 lb model rocket is launched vertically from rest at time t = 0 with a constant thrust of 2 lb for one second and no thrust for t > 1 s. Neglecting air resistance and the decrease in mass of the rocket, determine the maximum height [ft] reached by the rocket. Rounded to the nearest tenth.')


print('1 b) Calculate the time [s] required to reach this maximum height. Rounded to the nearest tenth.')

print('2 a) The system shown is initially at rest. Neglecting axle friction and the mass of the pulley. Determine the acceleration [ft/s²] of block A. Rounded to the nearest tenth.')

print('2 b) Calculate the velocity [ft/s] of block A after it has moved through 10 ft. Rounded to the nearest tenth.')

print('2 c) Determine the time [s] required for block A reach a velocity of 20 ft/s. Rounded to the nearest tenth.')

print('3 a) A single wire ACB passes through a ring at C attached to a sphere that revolves at a constant speed v in the horizontal circle shown. Knowing that the tension is the same in both portions of the wire, determine the speed v [m/s]. Rounded to the nearest tenth. ')

print('4 a) A turntable A is built into a stage for use in a theatrical production. It is observed during a rehearsal that a trunk B starts to slide outwards on the turntable 10 s after the turntable begins to rotate. Knowing that the trunk undergoes a constant tangential acceleration of 0.24 m/s², determine the coefficient of static friction between the trunk and the turntable. Rounded to the nearest hundred. ')

print('5 a) The orbit of the planet Venus is nearly circular with an orbital velocity of 126.5 x 10³ km/hr. Knowing that the mean distance from the center of the sun to the center of Venus is 108 x 10⁶ km and that the radius of the sun is 695.5 x 10³ km. Determine the mass [kg] of the sun. Rounded to the nearest integer. ')

print('5 b) Determine the acceleration [m/s²] of gravity at the surface of the sun. Rounded to the nearest tenth. ')

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
	ans4 = round(np.sqrt(v**2-2*a*x),1)
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
	ans5 = round(-ans4/a,1)
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
	ans6 = round(2*x2/t2**2,1)
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
	ans9 = round(2*x2/t2,1)
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

	grade = round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7+pnt8+pnt9)/9)*100,1)
	name = Element('student-name')
	out_final = Element('outputFinal')
	out_final.write(f" Thank you {name.value}, your answers have been submitted. Your score is: {grade} %")
