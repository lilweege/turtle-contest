'''
Luigi Quattrociocchi
quattrl
Breakdancing Hilbert Sheet
PYTHON TURTLE GRAPHICS CONTEST
Best Artistic/Complex Design
November 29th, 2020

A hilbert curve visualization with a twist!
The program draws a typical hilbert curve but 
isometrically projected and then extruded on
the z axis by a sine wave calculation.

References:
https://thecodingtrain.com/challenges/coding-in-the-cabana/003-hilbert-curve.html
https://stackoverflow.com/questions/41080000/convert-3d-coordinate-to-2d-coordinate-using-axonometric-and-isometric-projectio?noredirect=1&lq=1
'''


from colorsys import hsv_to_rgb
from turtle import *
import numpy as np
import math



# detail of curve
order = 6

# necessary constants
WIDTH, HEIGHT = 512, 512
N = 2 ** order
l = WIDTH // N
t = N ** 2


class Point:
	'''simple point class'''
	def __init__(self, x, y, z=0):
		self.x, self.y, self.z = x, y, z
	
	def __repr__(self):
		return f"({self.x}, {self.y}, {self.z})"
	
	def __iter__(self):
		yield self.x
		yield self.y
		yield self.z


def hilbert(i):
	'''calculates curve point location based on current iteration'''
	
	# see ref for derrivation of formula
	p = [
		Point(0, 0),
		Point(0, 1),
		Point(1, 1),
		Point(1, 0),
	][i & 3]
	
	for j in range(1, order):
		i >>= 2
		index = i & 3
		l = 2 ** j
		
		if index == 0:
			p.x, p.y = p.y, p.x
		elif index == 1:
			p.y += l
		elif index == 2:
			p.x += l
			p.y += l
		elif index == 3:
			p.x, p.y = 2 * l - 1 - p.y, l - 1 - p.x
	
	return p


def project(x, y, z):
	'''3D to 2D isometric projection'''
	xp = (x - z) / (2 ** 0.5)
	yp = (x + 2 * y + z) / (6 ** 0.5)
	return xp, yp


scl1 = .7
scl2 = 100
def nextPoint(n):
	# get the next point
	p = hilbert(n)
	
	# transform for canvas
	p.x *= l
	p.y *= l
	p.x += l/2 - WIDTH // 2
	p.y += l/2 - HEIGHT // 2
	
	# transform z axis based on any desired metric
	p.z = 	math.asin(p.y / (HEIGHT // 2)) * \
			math.asin(p.x / (WIDTH // 2)) * scl2
	
	# zoom out
	p.x *= scl1
	p.y *= scl1
	
	# shift down slightly
	p.y -= 75
	
	# get hue based on percent competion
	pencolor(hsv_to_rgb(n / t, 1, 1))
	
	# goto projected point (draws a line)
	goto(*(project(*p)))


def main():
	# initialize turtle
	setup(WIDTH, HEIGHT)
	title("Breakdancing Hilbert Sheet")
	bgcolor('black')
	speed('fastest')
	ht()
	# tracer(False)
	
	# go to start
	pu()
	nextPoint(0)
	pd()
	
	# trace breakdancing hilbert curve
	for i in range(1, t):
		nextPoint(i)
	
	# finish
	print("DONE")
	exitonclick()


if __name__ == '__main__':
	main()