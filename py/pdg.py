class __A(object):
	def __init__(self, mass, gamma):
		self.__m = mass
		self.__g = gamma

	def __str__(self):
		return 'mass {0}, width {1}'.format(self.__m, self.__g)

	def __add__(self, other):
		return self.__m.__add__(other)
	def __sub__(self, other):
		return self.__m.__sub__(other)
	def __mul__(self, other):
		return self.__m.__mul__(other)
	def __div__(self, other):
		return self.__m.__div__(other)
	def __truediv__(self, other):
		return self.__m.__truediv__(other)

	@property
	def m(self):
		return self.__m
	@property
	def mass(self):
		return self.__m
	@property
	def g(self):
		return self.__g
	@property
	def gamma(self):
		return self.__g
	@property
	def width(self):
		return self.__g

pi = __A(139.6, 0)
Lc = __A(2286.5, 0)
Lb = __A(5620, 0)
Sigmac2455pp = __A(2453.97, 1.89)
Sigmac2455z  = __A(2453.75, 1.83)
Sigmac2520pp = __A(2518.41, 14.78)
Sigmac2520z  = __A(2518.48, 15.3)
Sigmac2800pp = __A(2801, 75)
Sigmac2800z  = __A(2806, 72)
Lc2595 = __A(2592.25, 2.6)
Lc2625 = __A(2628.11, 0.97)
Lc2880 = __A(2881.63, 5.6)
