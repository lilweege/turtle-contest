'''
Luigi Quattrociocchi
quattrl
Flaming Fireball
PYTHON TURTLE GRAPHICS CONTEST
Best McMaster / Fireball Design
November 21st, 2020

An original take on the classic McMaster engineering fireball logo


References:
https://en.wikipedia.org/wiki/McMaster_University#/media/File:Macfireball.png
'''

from turtle import *

def curve(n, f, l):
	for x in range(n):
		forward(f)
		left(l)


WIDTH, HEIGHT = 600, 600
setup(WIDTH, HEIGHT)
win = Screen()
win.title("McMaster Fireball Logo")
ht()
speed("fastest")


def draw_gradient():
	pu()
	goto(-WIDTH//2, HEIGHT//2)
	pd()

	win.tracer(False)
	for y in range(HEIGHT//2, -HEIGHT//2, -1):
		forward(WIDTH)
		color((1, (HEIGHT//2 - y) / HEIGHT, 0))
		goto(-WIDTH//2, y)
	win.tracer(True)


def draw_flame():
	pu()
	goto(160, -110)
	pd()

	color("red", "red")
	begin_fill()

	right(50)
	curve(11, 5, 5)
	left(135)
	curve(11, 5, -5)
	curve(11, 5, 10)

	right(180)
	curve(11, 5, 10)
	curve(11, 5, -5)
	curve(11, 5, -10)
	left(180)
	curve(21, 5, 5)

	right(180)
	curve(11, 5, 10)
	curve(16, 5, -10)
	left(180)

	curve(16, 5, 5)
	right(180)
	curve(21, 5, 3)
	left(135)

	curve(10, 5, -5)
	curve(6, 5, 5)
	right(135)

	curve(10, 5, 5)
	curve(12, 5, -10)

	left(180)
	curve(17, 5, 5)

	right(170)
	curve(14, 5, 5)
	curve(12, 5, -13)

	left(180)
	curve(15, 5, 5)

	right(135)
	curve(10, 5, 5)
	curve(9, 5, -15)

	left(180)
	curve(17, 5, 5)

	end_fill()


def draw_spiral():
	pu()
	goto(0, -100)
	pd()

	color("red", "yellow")
	begin_fill()

	for x in range(58):
		ps = pensize()
		if ps < 20:
			pensize(ps + 0.5)
		forward(x)
		left(20)
	end_fill()
	pensize(1)


def main():
	draw_gradient()
	draw_flame()
	draw_spiral()
	exitonclick()


if __name__ == "__main__":
	main()

