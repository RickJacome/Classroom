import numpy as np
# Define Variables here

paraQ1a = Element("Q1a")
paraQ1a.write(f"1 a) An estimate of the expected load on over-the-shoulder seat belts is to be made before designing prototype belts that will be evaluated in automobile crash tests. Assuming that an automobile traveling at 45 mi/h is brought to a stop in 110 ms. Determine the average impulsive force [lb] exerted by a 200-lb man on the belt.  Rounded to nearest integer.")

paraQ1b = Element("Q1b")
paraQ1b.write(f"1 b) Determine the maximum force [lb] exerted on the belt if the force-time diagram has the shape shown.  Rounded to nearest integer.")

paraQ2a = Element("Q2a")
paraQ2a.write(f"2 a) At an intersection, car B was traveling south and car A was traveling 30° north of east  when they slammed into each other. Upon investigation it was found that after the crash the two cars got stuck and skidded off at an angle of 10° north of east. Each driver claimed that he was going at the speed limit of 50 km/h and that he tried to slow down but could not avoid the crash because the other driver was going a lot faster. Knowing that the masses of cars A and B were 1500 kg and 1200 kg, respectively, determine which car was going faster [A or B?] .")

paraQ2b = Element("Q2b")
paraQ2b.write(f"2 b) Determine the speed [km/h] of the faster of the two cars if the slower car was traveling at the speed limit. Rounded to the nearest tenth.")

paraQ3a = Element("Q3a")
paraQ3a.write(f"3 a) A ballistic pendulum is used to measure the speed of high-speed projectiles. A 6-g bullet A is fired into a 1-kg wood block B suspended by a cord with a length of l = 2.2 m. The block then swings through a maximum angle of θ = 60°. Determine the initial speed [m/s] of the bullet v_0. Rounded to the nearest tenth.")

paraQ3b = Element("Q3b")
paraQ3b.write(f"3 b) Calculate the impulse [m/s] imparted by the bullet on the block. Rounded to the nearest tenth.")

paraQ3c = Element("Q3c")
paraQ3c.write(f"'3 c) Determine the force [m/s] on the cord immediately after the impact. Rounded to the nearest tenth.")

paraQ4a = Element("Q4a")
paraQ4a.write(f"'4 a) Two identical billiard balls can move freely on a horizontal table. Ball A has a velocity v_0 as shown and hits ball B, which is at rest, at a point C defined by θ = 45°. Knowing that the coefficient of restitution between the two balls is e = 0.8 and assuming no friction, determine the velocity of ball A after impact as a function of the initial velocity. Rounded to the nearest hundred.")

paraQ4b = Element("Q4b")
paraQ4b.write(f" 4 b) Determine the direction [degrees] of velocity for ball A after impact with respect to the horizontal. Rounded to the nearest tenth.")

paraQ4c = Element("Q4c")
paraQ4c.write(f"4 c) Determine the magnitude of velocity for ball B after impact as a function of the initial velocity. Rounded to the nearest hundred.")

paraQ4d = Element("Q4d")
paraQ4d.write(f"4 d)  Determine the direction [degrees] of velocity for ball B after impact with respect to the horizontal. Rounded to the nearest tenth.")

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

def print_num11(*ags, **kws):
	global pnt11
	ans11 = round(2*x2/t2,1)
	if input_num11.value=='':
		out11.write(f"Blank value provided, please try again.")
	elif input_num11.value == str(ans11):
		out11.write(f"Correct!")
		pnt11 = 1
	else:
		out11.write(f"You typed in {input_num10.value}, that is not correct.")
		pnt11 = 0

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
	out11.clear()

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

	grade = round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7+pnt8+pnt9+pnt10+pnt11)/10)*100,1)
	name = Element('student-name')
	out_final = Element('outputFinal')
	out_final.write(f" Thank you {name.value}, your answers have been submitted. Your score is: {grade} %")
