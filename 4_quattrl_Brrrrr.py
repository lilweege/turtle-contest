'''
Luigi Quattrociocchi
quattrl
Brrrrr
PYTHON TURTLE GRAPHICS CONTEST
Meme - Hilarious Design
November 29th, 2020

Python go Brrrrr
'''

from turtle import *
import random


WIDTH, HEIGHT = 600, 600
setup(WIDTH, HEIGHT)
title("Python go Brrrrr")
ht()
speed("fastest")


def draw_r(x, y):
	pu()
	goto(x, y)
	pd()
	begin_fill()
	goto(x-2, y)
	goto(x-2, y+10)
	goto(x, y+10)
	goto(x, y)
	end_fill()
	pu()
	goto(x+2, y+10)
	pd()
	begin_fill()
	goto(x+2, y+12)
	goto(x, y+12)
	goto(x, y+10)
	end_fill()

	
def main():
	# tracer(False)
	w=60
	h=30
	for y in range(1, h + 1):
		for x in range(1, w + 1):
			draw_r(x * 10 - WIDTH // 2, HEIGHT // 2 - y * 20)
		
	exitonclick()


if __name__ == "__main__":
	main()

