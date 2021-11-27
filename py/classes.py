class Vector:
	def __init__(self, *coordinates):
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.z = coordinates[2]

	def __abs__(self):
		from math import sqrt
		return sqrt(self.x^2 + self.y^2 + self.z^2)

	def __str__(self):
		return "({}, {}, {})".format(self.x, self.y, self.z)

def _reflect(vector):
	return (-vector.x, -vector.y, -vector.z)

Vector.reflect = _reflect

class OtherVector(Vector):
	other = (9, 9, 9)
	def __str__(self):
		return "{} & {}".format(Vector.__str__(self), self.other)

v = Vector(1, 1, 1)

print(v, v.reflect())

ov = OtherVector(1, 1, 2)
print(ov, ov.reflect())
