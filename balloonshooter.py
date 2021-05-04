import turtle


wn = turtle.Screen()
wn.title("Balloon")
wn.bgcolor("black")
wn.setup(width=800,height=600) 
wn.tracer(0)
score = 0
missed_score = 0



# Balloon

baloon=turtle.Turtle()
baloon.speed(0) #	not the speed of the paddle
baloon.shape("circle")
baloon.shapesize(stretch_wid=3, stretch_len=3)
baloon.color("white")
baloon.penup()  #	using the pen up
baloon.goto(-350,0)


#	gun B

gun=turtle.Turtle()
gun.speed(0) #	not the speed of the paddle
gun.shape("turtle")
gun.tilt(180)
gun.shapesize(stretch_wid=3, stretch_len=3)
gun.color("white")
gun.penup()  #	using the pen up
gun.goto(350,0)

# #eraser
# eraser=turtle.Turtle()
# eraser.speed(0) #	not the speed of the paddle
# eraser.shape("square")
# eraser.tilt(0)
# eraser.shapesize(stretch_wid=10, stretch_len=10)
# eraser.color("black")
# eraser.penup()  #	using the pen up


# #	bullet

bullet=turtle.Turtle()
bullet.speed(0) #	not the speed of the paddle
bullet.shape("square")
bullet.color("white")
bullet.penup()  #	using the pen up


# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup() 
pen.hideturtle()
pen.goto(0,260)


def baloon_up():
	y=baloon.ycor()
	y+=20
	baloon.sety(y)

def baloon_down():
	y=baloon.ycor()
	y-=20
	baloon.sety(y)

def gun_up():
	y=gun.ycor()
	y+=20
	gun.sety(y)

def gun_down():
	y=gun.ycor()
	y-=20
	gun.sety(y)

def shoot():
	bullet.goto(gun.xcor(), gun.ycor())
	bullet.dx=3
	bullet.dy=0
	global score
	global missed_score 
	score_flag = False
	# loc_score = score
	while bullet.xcor() > -420:
		bullet.sety(bullet.ycor() + bullet.dy)
		bullet.setx(bullet.xcor() - bullet.dx)
		baloon.sety(baloon.ycor() - 2)

		#ballon loop
		if baloon.ycor() <= -294:
			baloon.sety(baloon.ycor() + 594)
		if abs(baloon.xcor() - bullet.xcor()) <= 40 and abs(baloon.ycor() - bullet.ycor()) <= 40:
			# print("balloon xcord = "+str(baloon.xcor()))
			# print("balloon ycor = "+str(baloon.ycor()))
			# print("bullet xcoord = "+str(bullet.xcor()))
			# print("bullet ycoord = "+ str(bullet.ycor()))
			score_flag = True
			score += 1
			# print("in if in loop score = "+str(score))
		wn.update()
	if not score_flag:
		missed_score += 1
		# eraser.sety(280)
		# eraser.setx(-10)
		pen.clear()
		pen.write("Missed score = "+ str(missed_score), align="center", font=("Arial", 24, "normal"))
		wn.update()
		print("missed score = "+str(missed_score))
		print("balloon xcord = "+str(baloon.xcor()))
		print("balloon ycor = "+str(baloon.ycor()))
		print("bullet xcoord = "+str(bullet.xcor()))
		print("bullet ycoord = "+str(bullet.ycor()))
	else:
		score_flag = False
		#print("score = " + str(score))
		wn.clearscreen()
		pen.write("Missed score = "+ str(missed_score), align="center", font=("Arial", 24, "normal"))
wn.listen()
# wn.onkeypress(baloon_up,"w")
wn.onkeypress(gun_up,"Up")
# wn.onkeypress(baloon_down,"s")
wn.onkeypress(gun_down,"Down")

wn.onkeypress(shoot, "space")


#	Main Loop
while True:
	#	Update the screen 
	wn.update() 

	#	Move the bullet
	baloon.sety(baloon.ycor() - 2)

	if baloon.ycor() <= -294:
		baloon.sety(baloon.ycor() + 594)

	


