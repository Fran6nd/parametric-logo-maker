import math
class Vector2D:

	def copy(self):
		return Vector2D(self.x, self.y)

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getModule(self):
		return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

	def getArg(self):
		return math.atan2(self.y, self.x)

	def setArg(self, arg):
		module = self.getModule()
		y = math.sin(arg) * module
		x = math.cos(arg) * module
		return Vector2D(x, y)

	def normalize(self):
		arg = self.getArg()
		y = math.sin(arg)
		x = math.cos(arg)
		return Vector2D(x, y)

	def pos(self):
		return (self.x, self.y)

	def toDict(self):
		return {
			'x' : self.x,
			'y' : self.y
		}

	def fromDict(d):
		return Vector2D(d['x'], d['y'])

	#METATABLE.
	def __str__(self):
		return('Vector2D(x=' + str(self.x) + ', y=' + str(self.y) + ')')

	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector2D(self.x - other.x, self.y - other.y)

	def __iadd__(self, other):
		return self + other

	def __isub__(self, other):
		return self - other

	def __neg__(self):
		return Vector2D(-self.x, -self.y)

	def __pos__(self):
		return Vector2D(self.x, self.y)

	def __abs__(self):
		x = self.x if self.x>=0 else -self.x
		y = self.y if self.y>=0 else -self.y
		return Vector2D(x, y)

	def __mul__(self, other):
		x = self.x * other
		y = self.y * other
		return Vector2D(x, y)

	def __div__(self, other):
		x = self.x / other
		y = self.y / other
		return Vector2D(x, y)

	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		return False

	def __ne__(self, other):
		return not self.__eq__(other)

	#STATIC.
	def zero():
		return Vector2D(0,0)

	def up():
		return Vector2D(0,1)

	def down():
		return Vector2D(0,-1)

	def right():
		return Vector2D(1,0)

	def left():
		return Vector2D(-1,0)
if __name__ == "__main__":
	print(Vector2D.zero())
	a = Vector2D(0,-1)
	b = Vector2D(1,2)
	a -= b
	print(a)
	print(-a)
	a = Vector2D(3, 2)
	print(a.normalize())
	print(Vector2D.zero() == Vector2D.zero())
	print(Vector2D(4,5.5555555555555) == Vector2D(4,5.5555555555555))
	print(Vector2D(4,5.5555555555555) != Vector2D(4,5.5555555555555))
	print(Vector2D.right().getArg())
	print(Vector2D.up().getArg())
	print(Vector2D.up().setArg(0).getArg())
	print(Vector2D.up().setArg(0).getModule())