import math
from scipy.integrate import quad

Z = 1
m = 938.3
E = 1.9e-3
r0 = 2 * .87
r1 = Z*Z * 197/137 / E

def func(r):
	return 2 / 197 * math.sqrt(m*(-E + Z*Z * 197/137 / r))

res, err = quad(func, r0, r1)

print(Z, m, r0/2, r1)
print(res, err)
