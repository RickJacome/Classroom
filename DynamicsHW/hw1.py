import numpy as np
import js


a = np.random.randint(1, 5)
b = np.random.randint(4, 10)
x = np.random.randint(30,40)
t = np.random.randint(2,5)
v1 = np.random.randint(10,15)
v2 = np.random.randint(25,35)
d = np.random.randint(45,80)
A1 = np.random.randint(2,10)
A2 = np.random.randint(11,20)
B1 = np.random.randint(4,10)
B2 = np.random.randint(-10,-4)

paraQ1 = Element("Q1")
paraQ1.write(f"if a = {a} and b = {b}")

paraQ1a = Element("Q1a")
paraQ1a.write(f" 1 a) What is a + b = ?")

paraQ1b = Element("Q1b")
paraQ1b.write(f"1 b) What is a - b = ?")

paraQ2 = Element("Q2")
paraQ2.write(f"2) If a car traveled {x} meters in about {t} seconds. What is the velocity [m/s] of the car? Rounded to the nearest tenth.")

paraQ3 = Element("Q3")
paraQ3.write(f"3) If a car changed its speed from {v1} (m/s) to {v2} (m/s), while having traveled {d} meters. What is the acceleration [m/s²] of the car? Rounded to the nearest tenth.")

paraQ4 = Element("Q4")
paraQ4.write(f"4) Given vector A = {A1}i + {A2}j. Calculate the magnitude of A. Rounded to the nearest tenth.")

paraQ5 = Element("Q5")
paraQ5.write(f"5) Given vector B = {B1} i - {np.abs(B2)} j. Calculate the angle [radians] in between vectors A and B. Rounded to the nearest tenth. ")

paraQ6 = Element("Q6")
paraQ6.write(f"6) Calculate the i-component of the vector A-B. Rounded to the nearest whole number.")



input_num1 = Element("Question1")
input_num2 = Element("Question2")
input_num3 = Element("Question3")
input_num4 = Element("Question4")
input_num5 = Element("Question5")
input_num6 = Element("Question6")
input_num7 = Element("Question7")

out1 = Element("outputDiv1") 
out2 = Element("outputDiv2") 
out3 = Element("outputDiv3") 
out4 = Element("outputDiv4") 
out5 = Element("outputDiv5")
out6 = Element("outputDiv6")
out7 = Element("outputDiv7") 

def print_num1(*ags, **kws):
	global pnt1
	ans1 = a+b
	
	if input_num1.value =='':
		out1.write(f"Blank value provided, please try again.")
	elif input_num1.value  == str(ans1):
		out1.write(f"Correct!")
		pnt1 = 1
	else:
		out1.write(f"You typed in {input_num1.value}, that is not correct")
		pnt1 = 0

def print_num2(*ags, **kws):
	global pnt2
	ans2 = a-b
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
	ans3 = round(x/t,1)
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
	ans4 = round((v2**2-v1**2)/(2*d),1)
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
	ans5 = round(np.sqrt(A1**2 + A2**2) , 1)
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
	ans6 = round( np.arccos((A1*B1+A2*B2)/( np.sqrt(A1**2 + A2**2)*np.sqrt(B1**2 + B2**2) ) ),1)
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
	ans7 = round(A1-B1,1)
	if input_num7.value=='':
		out7.write(f"Blank value provided, please try again.")
	elif input_num7.value == str(ans7):
		out7.write(f"Correct!")
		pnt7 = 1
	else:
		out7.write(f"You typed in {input_num7.value}, that is not correct.")
		pnt7 = 0

def clear(*ags, **kws):
	out1 = Element("outputDiv1")
	out2 = Element("outputDiv2")
	out3 = Element("outputDiv3")
	out4 = Element("outputDiv4")
	out5 = Element("outputDiv5")
	out6 = Element("outputDiv6")
	out7 = Element("outputDiv7")
	out1.clear()	
	out2.clear()
	out3.clear()
	out4.clear()
	out5.clear()
	out6.clear()
	out7.clear()
def final_sub(*ags, **kws):
	out1 = Element("outputDiv1")
	out2 = Element("outputDiv2")
	out3 = Element("outputDiv3")
	out4 = Element("outputDiv4")
	out5 = Element("outputDiv5")
	out6 = Element("outputDiv6")
	out7 = Element("outputDiv7")
	name = Element('student-name')
	out_final = Element('outputFinal')
	try:
		round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7)/7)*100,1)
	except NameError:
		out_final.write(f"You did not finish submitting all questions above. Refresh Page and start again. ")

	grade = round(((pnt1+pnt2+pnt3+pnt4+pnt5+pnt6+pnt7)/7)*100,1)
	out_final.write(f" Thank you {name.value}, your answers have been submitted. Your score is: {grade} %")
