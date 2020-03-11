import turtle
from time import sleep
from math import pi, sin, cos, radians, atan, tan, log

turtle.screensize(400, 400)
tut = turtle.Turtle()

round = 360
tut.speed('fastest')

R = 300				# radius 
n = 40				# number of functions drawed
coef = 100			# value of coef*Y coords of function 
bucle = 360			# range of X coords of function	 360 = 2*pi
viteza = 10			# high viteza -> low precision


def fct(x):
	if x == 0:
		return 0
	return sin(x)



tut.penup()
T = 0
for k in range(n):
    y = R * sin(2*k*pi/n)
    x = R * cos(2*k*pi/n)
    tut.goto(0, 0)
    tut.pendown()
    for pcts in range(0, bucle, viteza):
        m = y/x
        alph = atan(m)
        X = 0
        Y = 0
        simetric = (-1)**T
        if x >= 0 and y >= 0 or x >= 0 and y <= 0: #cadranul 1 si 4
            X = x/bucle*pcts - coef*sin(alph)*fct(radians(pcts))*simetric		# * simetric 
            Y = m*(x/bucle*pcts) + coef*cos(alph)*fct(radians(pcts))*simetric
        if x <= 0 and y >= 0 or x <= 0 and y <= 0: #cadranul 2 si 3
            X = x / bucle * pcts + coef * sin(alph) * fct(radians(pcts))*simetric
            Y = m * (x / bucle * pcts) - coef * cos(alph) * fct(radians(pcts))*simetric
       
        #	FARA CENTRU
        #if pcts == viteza:
        #	tut.penup()
        tut.goto(X, Y)
        #tut.pendown()
    T += 1
    tut.penup()
turtle.exitonclick()
