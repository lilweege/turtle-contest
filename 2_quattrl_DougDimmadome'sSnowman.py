'''
Luigi Quattrociocchi
quattrl
Doug Dimmadome's Snowman
PYTHON TURTLE GRAPHICS CONTEST
Christmas Themed Design
November 29th, 2020

Character from TV show Timmy Turner "Doug Dimmadome"
is well known for his tall top hat, this program
shows my interpretation of what would happen if
he were to build a snowman
'''

from turtle import *
import random


WIDTH, HEIGHT = 600, 600
setup(WIDTH, HEIGHT)
title("Doug Dimmadome's Snowman")
ht()
speed("fastest")


def draw_gradient():
	pu()
	goto(-WIDTH//2, HEIGHT//2)
	pd()

	tracer(False)
	for y in range(HEIGHT//2, -HEIGHT//2, -1):
		forward(WIDTH)
		v = (HEIGHT//2 - y) / HEIGHT
		color((v, v, 1))
		goto(-WIDTH//2, y)
	tracer(True)


def draw_snow():
	color('white', 'white')
	pu()
	goto(-WIDTH//2, -200)
	pd()
	begin_fill()
	goto(WIDTH//2, -200)
	goto(WIDTH//2, -HEIGHT//2)
	goto(-WIDTH//2, -HEIGHT//2)
	end_fill()



def draw_snowman():
	pensize(5)
	color('black', 'white')

	pu()
	goto(0, 0)
	pd()
	begin_fill()
	circle(30)
	end_fill()

	pu()
	goto(0, -100)
	pd()
	begin_fill()
	circle(50)
	end_fill()

	pu()
	goto(0, -210)
	pd()
	begin_fill()
	circle(60)
	end_fill()

	color('black', 'black')

	pu()
	goto(10, 35)
	pd()
	begin_fill()
	circle(3)
	end_fill()

	pu()
	goto(-10, 35)
	pd()
	begin_fill()
	circle(3)
	end_fill()

	pu()
	goto(0, -35)
	pd()
	begin_fill()
	circle(3)
	end_fill()

	pu()
	goto(0, -70)
	pd()
	begin_fill()
	circle(3)
	end_fill()
	
	pu()
	goto(0, -125)
	pd()
	begin_fill()
	circle(3)
	end_fill()

	pu()
	goto(-40, 60)
	pd()
	begin_fill()
	goto(40, 60)
	goto(40, 70)
	goto(-40, 70)
	goto(-40, 60)
	end_fill()
	begin_fill()
	goto(30, 70)
	goto(30, 1700)
	goto(-30, 1700)
	goto(-30, 70)
	end_fill()

	color("brown", "brown")

	pu()
	goto(35, -10)
	pd()
	goto(80, 40)
	goto(90, 40)
	goto(80, 40)
	goto(90, 50)
	
	pu()
	goto(-45, -20)
	pd()
	goto(-110, 20)
	goto(-120, 20)
	goto(-110, 20)
	goto(-120, 30)
	goto(-110, 20)
	goto(-100, 30)


	color("orange", "orange")

	pensize(10)
	pu()
	goto(0, 25)
	pd()
	goto(-40, 10)


def draw_snowflakes(n):
	color('white', 'white')
	for x in range(n):
		rx, ry = random.randint(-WIDTH//2, WIDTH//2), random.randint(-HEIGHT//2, HEIGHT//2)
		pu()
		goto(rx, ry)
		pd()
		begin_fill()
		circle(3)
		end_fill()


def main():
	draw_gradient()
	draw_snow()
	draw_snowflakes(25)
	draw_snowman()
	exitonclick()


if __name__ == "__main__":
	main()

