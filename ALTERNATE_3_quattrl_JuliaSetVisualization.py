'''
Luigi Quattrociocchi
quattrl
Julia Set Visualization
PYTHON TURTLE GRAPHICS CONTEST
Best Artistic/Complex Design
November 21st, 2020

A julia set visualization using numpy for vectorization, PIL
for image processing and exporting, matplotlib for colormaps,
and turtle for displaying quickly and simply (although there
are many other ways to display the image).

References:
https://en.wikipedia.org/wiki/Mandelbrot_set
http://www.karlsims.com/julia.html
https://www.youtube.com/watch?v=6_u18uFEoN0
https://pillow.readthedocs.io/en/stable/reference/
https://numpy.org/doc/stable/numpy-ref.pdf
https://docs.python.org/3/library/turtle.html
https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

https://www.learnpythonwithrune.org/numpy-calculate-the-julia-set-with-vectorization/
https://stackoverflow.com/questions/10965417/how-to-convert-a-numpy-array-to-pil-image-applying-matplotlib-colormap
'''


from turtle import *
import numpy as np
from matplotlib import cm
from PIL import Image


# width and height of image and also of window
WIDTH, HEIGHT = 800, 600
# half width and height created for later convenience
HALFW, HALFH = WIDTH // 2, HEIGHT // 2


def julia_set(c=complex(-0.4, 0.6), h=HEIGHT, w=WIDTH, x=0.0, y=0.0, ax=1.5, scl=1.0, num_iters=100):
	'''
	Returns a 2d numpy array with a percentage of the 
	number of iterations that is took for the point at
	that location in the complex plane to diverge
	'''
	
	# scaling variables
	x_w = ax
	y_h = ax * h / w
	x_lo = x - x_w / scl
	x_hi = x + x_w / scl
	y_lo = y - y_h / scl
	y_hi = y + y_h / scl
	
	# initialize complex plane re and im axis mapped to points in matrix
	z = np.linspace(x_lo, x_hi, w).reshape((1, w)) + \
		np.linspace(y_lo, y_hi, h).reshape((h, 1)) * 1j
	
	# initialize matrix with all points as the complex number given
	c = np.full(z.shape, c)
	
	# initialize boolean matrix for open set of points (haven't diverged yet)
	open_s = np.full(z.shape, True, dtype=bool)
	
	# percent of max iterations at which point diverges
	# percent used to make easier to use colormap later
	div_p = np.zeros(z.shape, dtype=float)
	
	for iter in range(num_iters):
		# numpy array indexing is not the same as lists, but like a filter
		# for instance, ALL points for which abs(z) > 2 will become false
		# in other words, if any point z is beginning to diverge, remove it from the set
		open_s[np.abs(z) > 2] = False
		
		# all points which haven't diverged yet will be updated for this iteration
		z[open_s] = z[open_s] ** 2 + c[open_s]
		div_p[open_s] = iter / num_iters
	
	return div_p


def draw_matrix(matrix: np.ndarray):
	'''
	an alternate method to display a color matrix
	without using PIL (relatively very slow)
	'''

	# some assumptions should be made about the color matrix
	assert matrix.ndim == 3, f"Matrix Error: {matrix.ndim} dimension array (expected 3: [y][x][c])"
	assert matrix.shape[-1] == 4, f"Matrix Error: innermost array has length of {matrix.shape[-1]} (expected 4: [r g b a])"
	assert matrix.dtype == np.float64, f"Matrix Error: {matrix.dtype} data type (expected np.float64)"


	def get_color(x, y):
		'''
		extracts the r, g, b color values from the
		matrix at a given x, y point. If the point
		is out of bounds the function returns black
		'''
		
		if 0 <= x < WIDTH and 0 <= y < HEIGHT:
			r, g, b, _ = matrix[y][x]
			return float(r), float(g), float(b)
		return 0, 0, 0


	# turtle graphics functions are used to fill screen with pixels
	
	# disable tracer (or else it will take forever to finish)
	tracer(False)
	ht() # hide turtle
	seth(270) # set heading to south
	
	# nested for loops iterate over every pixel on screen
	for x in range(WIDTH):
	
		# go to top of screen in the current column
		# NOTE: (0, 0) is the center of the screen
		# pen is lifted so that a line is not drawn
		pu() # pen down
		goto(x - HALFW, HALFH)
		pd() # pen up

		# inner for loop draws each column of pixels
		for y in range(HEIGHT):
		
			# set the color to the corresponding color in the image
			pencolor(get_color(x, y))
			# move down by one pixel (heading is south)
			forward(1)
		
		# update the screen after every strip
		update()
		


def main():
	# matrix = julia_set()
	# matrix = julia_set(c=-1, ax=2)
	# matrix = julia_set(c=complex(0, -0.8))
	# matrix = julia_set(c=complex(-0.7269, 0.1889), num_iters=300)
	# matrix = julia_set(c=complex(-0.79, 0.15), num_iters=300)
	# matrix = julia_set(c=complex(-0.162, 1.04))
	# matrix = julia_set(c=complex(0.28, 0.008))
	matrix = julia_set(c=complex(-0.79, 0.15), num_iters=10)

	# colormap = "hot"
	# colormap = "afmhot"
	colormap = "magma"
	# colormap = "inferno"
	# colormap = "jet"
	# colormap = "twilight"

	'''
	setting individual pixels using goto method is too slow
	to be feasible, saving pixel data to image file and blitting
	entire graphic to screen at once is much more efficient,
	as the turtle library uses a tkinter window and canvas.
	Having a draw call for every individual pixel very inefficient.
	Furthermore, I've found that memory leaks can occur if you
	aren't careful with HOW the pixels are being set. I've found
	the way shown above to be the best as it is going to get.
	matplotlib could also be used in place of turtle to display the image (also allows zooming)
	'''

	# initialize turtle
	setup(WIDTH, HEIGHT)
	title("Julia set visualization")

	# convert floats (0-1) to rgba arrays (size 4)
	colormap = cm.get_cmap(colormap)(matrix)
	
	
	# METHOD 1 (SLOW)
	# draw_matrix(colormap)


	# METHOD 2 (FAST)
	fn = "julia_set.png"
	img = Image.fromarray(np.uint8(colormap * 255))
	img.save(fn)
	bgpic(fn)

	exitonclick()


if __name__ == "__main__":
	# __import__('sys').exit(0)
	main()
