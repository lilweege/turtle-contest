'''
Luigi Quattrociocchi
Hilbert Cube

References:
https://thecodingtrain.com/challenges/coding-in-the-cabana/003-hilbert-curve.html
https://math.stackexchange.com/questions/123642/representing-a-3d-hilbert-curve-as-an-l-system
https://en.wikipedia.org/wiki/Rotation_matrix
https://en.wikipedia.org/wiki/Isometric_projection
'''

'''
lsystem Hilbert3D {

    set iterations = 3;
    set symbols axiom = X;

    interpret F as DrawForward(10);
    interpret + as Yaw(90);
    interpret - as Yaw(-90);
    interpret ^ as Pitch(90);
    interpret & as Pitch(-90);
    interpret > as Roll(90);
    interpret < as Roll(-90);

    rewrite X to ^ < X F ^ < X F X - F ^ > > X F X & F + > > X F X - F > X - >;

}
'''

# ayo shit be jank but wuteva


import sys
from colorsys import hsv_to_rgb
from turtle import *
from math import *



# detail of curve
order = 2

# necessary constants
WIDTH, HEIGHT = 512, 512
N = 2 ** order
l = WIDTH // N
t = N ** 3

class Vector3:
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z
	
	def __repr__(self):
		return "({0:2.2f}, {1:2.2f}, {2:2.2f})".format(self.x, self.y, self.z)
	
	def __iter__(self):
		yield self.x
		yield self.y
		yield self.z


def matmult(m1, m2):
	return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*m1)] for A_row in m2]


class Point:
	class Action:
		def __init__(self, cmd: str, amt: float):
			self.command, self.amount = cmd, amt
	
	def __init__(self):
		self.pos = Vector3(0, 0, 0)
		self.rot = [
			[ 1,  0,  0],
			[ 0,  1,  0],
			[ 0,  0,  1]
		]
	
	
	def roll(self, phi):
		r = radians(phi)
		s = sin(r)
		c = cos(r)
		R_x = [
			[ 1,  0,  0],
			[ 0,  c, -s],
			[ 0,  s,  c]
		]
		self.rotate(R_x)
	
	def pitch(self, theta):
		r = radians(theta)
		s = sin(r)
		c = cos(r)
		R_y = [
			[ c,  0,  s],
			[ 0,  1,  0],
			[-s,  0,  c]
		]
		self.rotate(R_y)
	
	def yaw(self, psi):
		r = radians(psi)
		s = sin(r)
		c = cos(r)
		R_z = [
			[ c, -s,  0],
			[ s,  c,  0],
			[ 0,  0,  1]
		]
		self.rotate(R_z)
	
	
	def rotate(self, matr):
		self.rot = matmult(self.rot, matr)
	
	
	def walk(self, v):
		self.pos.x += v * self.rot[0][0]
		self.pos.y += v * self.rot[0][1]
		self.pos.z += v * self.rot[0][2]
	
	
	def act(self, action: Action):
		if func := getattr(self, action.command, None):
			func(action.amount)
	
	def stamp(self):
		return Vector3(*self.pos)
	


def LSystem(axioms: str, rules: dict, iters: int = order):
	for _ in range(iters):
		axioms = ''.join(rules.get(axiom, axiom) for axiom in axioms)
	return axioms



def traceCurve(sequence, interpret, alpha=25, beta=50):
	p = Point()
	project(p, alpha, beta)
	
	for char in sequence:
		if action := interpret.get(char, None):
			p.act(action)
			if char == "F":
				yield p.stamp()


def project(point, alpha, beta):
	# isometric is a=30, b=45
	point.roll(degrees(asin(tan(radians(alpha)))))
	point.pitch(beta)




def main():
	
	axiom = "X"
	ruleset = {"X": "^<XF^<XFX-F^>>XFX&F+>>XFX-F>X->"}
	interpret = {
		"F": Point.Action("walk", l // 2),
		"+": Point.Action("yaw", 90),
		"-": Point.Action("yaw", -90),
		"^": Point.Action("pitch", 90),
		"&": Point.Action("pitch", -90),
		">": Point.Action("roll", 90),
		"<": Point.Action("roll", -90),
	}

	sequence = LSystem(axiom, ruleset)
	
	
	states = []
	for angle in range(360):
		path = list(traceCurve(sequence, interpret, beta=angle))
		lines = list(enumerate((path[i], path[i+1]) for i in range(t - 2)))
		lines.sort(key=lambda e: e[1][0].z, reverse=True)
		states.append(lines)
		
		print(round(angle/3.6, 2), "%")
	
	# path = list(traceCurve(sequence, interpret))
	# lines = list(enumerate((path[i], path[i+1]) for i in range(t - 2)))
	# lines.sort(key=lambda e: e[1][0].z, reverse=True)
	
	setup(WIDTH, HEIGHT)
	title("Hilbert Cube")
	bgcolor('black')
	speed('fastest')
	ht()
	tracer(False)
	pensize(2)
	
	while True:
		for lines in states:
			for i, (p1, p2) in lines:
				pencolor(hsv_to_rgb(i / t, 1, 1))
				pu()
				goto(p1.x, p1.y)
				pd()
				goto(p2.x, p2.y)
			update()
			clear()

	# for i, (p1, p2) in lines:
		# pencolor(hsv_to_rgb(i / t, 1, 1))
		# pu()
		# goto(p1.x, p1.y)
		# pd()
		# goto(p2.x, p2.y)
	
	print("DONE")
	exitonclick()
		

if __name__ == '__main__':
	main()