import numpy as np
# Define Variables here

print('1 a) A 15-lb block B starts from rest and slides on the 25-lb wedge A, which is supported by a horizontal surface. Neglecting friction, determine the magnitude velocity [ft/s] of B relative to A after it has slid 3 ft down the inclined surface of the wedge. Rounded to the nearest tenth.')

print('1 b) Calculate the corresponding velocity [ft/s] of A. Rounded to the nearest tenth.')

print('2 a) A 40-lb block B is suspended from a 6-ft cord attached to a 60-lb cart A, which may roll freely on a frictionless, horizontal track. If the system is released from rest in the position shown, determine the velocity of A [ft/s] as B passes directly under A. Rounded to the nearest tenth.')

print('2 b) Calculate the velocity of B [ft/s] as B passes directly under A. Rounded to the nearest tenth.')

print('In a game of pool, ball A is moving with a velocity v_0 with a magnitude of 15 ft/s when it strikes balls B and C, which are at rest and aligned as shown in the image below. Knowing that after the collision the three balls move in the directions indicated and assuming frictionless surfaces and perfectly elastic impact (e.g. , conservation of energy).')
print('3 a) Determine the magnitude of the velocity [ft/s] of ball A. Rounded to the nearest tenth.')

print('3 b) Determine the velocity [ft/s] of ball B. Rounded to the nearest tenth.')

print('3 c) Determine the velocity [ft/s] of ball C. Rounded to the nearest tenth.')

print('In a game of pool, ball A is moving with a velocity v_0 with a magnitude of 15 ft/s when it strikes balls B and C, which are at rest and aligned as shown in the image below. Knowing that after the collision the three balls move in the directions indicated and assuming frictionless surfaces and perfectly elastic impact (e.g. , conservation of energy).')
print('4 a) Determine the magnitude of the velocity [ft/s] of ball A. Rounded to the nearest tenth.')

print('4 b) Determine the velocity [ft/s] of ball B. Rounded to the nearest tenth.')

print('4 c) Determine the velocity [ft/s] of ball C. Rounded to the nearest tenth.')

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

def print_num10(*ags, **kws):
	global pnt10
	ans10 = round(2*x2/t2,1)
	if input_num10.value=='':
		out10.write(f"Blank value provided, please try again.")
	elif input_num10.value == str(ans10):
		out10.write(f"Correct!")
		pnt10 = 1
	else:
		out10.write(f"You typed in {input_num10.value}, that is not correct.")
		pnt10 = 0

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

	out1.clear()	
	out2.clear()
	out3.clear()
	out4.clear()
	out5.clear()
	out6.clear()
	out7.clear()
	out8.clear()
	out9.clear()
	out10.clear()

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

	name = Element('student-name')
	out_final = Element('outputFinal')
	try:
		round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7+pnt8+pnt9+pnt10)/10)*100,1)
	except NameError:
		out_final.write(f"You did not finish submitting all questions above. Refresh Page and start again. ")
	grade = round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7+pnt8+pnt9+pnt10)/10)*100,1)
	out_final.write(f" Thank you {name.value}, your answers have been submitted. Your score is: {grade} %")


