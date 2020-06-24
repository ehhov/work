from math import sqrt

class val_err:
	def __init__(self, val, err):
		self.val = float(val)
		self.err = abs(float(err))
	
	def times(me, x):
		return val_err(me.val*x, me.err*abs(x))
	def segment(me):
		return '[{0}, {1}]'.format(me.val-me.err, me.val+me.err)
	def scale(self, x):
		return val_err(self.val*x, self.err*abs(x))
	def flip(self):
		return val_err(1/self.val, self.err/self.val**2)

	def add(self, other, r):
		return val_err(self.val+other.val, sqrt(self.err**2 + other.err**2 + 2*r*self.err*other.err))
	def sub(self, other, r):
		return self.add(other.scale(-1), -r)
	def mul(self, other, r):
		return val_err(self.val*other.val, sqrt((self.err*other.val)**2 + (self.val*other.err)**2 + 2*r*abs(self.val*other.val)*self.err*other.err))
	def div(self, other, r):
		return self.mul(other.flip(), -r)
	def Print(self):
		print(self.val, '+-', self.err)
	
	def __add__(self, other):
		return self.add(other, 0)
	def __sub__(self, other):
		return self.sub(other, 0)
	def __truediv__(self, other):
		return self.div(other, 0)
	def __div__(self, other):
		return self.div(other, 0)
	def __mul__(self, other):
		return self.mul(other, 0)
	
	def __str__(self):
		return "{0} +- {1}".format(self.val, self.err)


### Bachelor BR using PDG ### Dp  = .0938
### Bachelor BR using PDG ### Dpe = .0016
### Bachelor BR using PDG ### Dz  = .03950
### Bachelor BR using PDG ### Dze = .031
### Bachelor BR using PDG ### Lc  = .0628
### Bachelor BR using PDG ### Lce = .0032
### Bachelor BR using PDG ### 
### Bachelor BR using PDG ### Lc3pi = val_err(0.0077, 0.0011)
### Bachelor BR using PDG ### Lcpi  = val_err(0.0049, 0.0004)
### Bachelor BR using PDG ### pi3pi = .5
### Bachelor BR using PDG ### r = Lc3pi.div(Lcpi, pi3pi)
### Bachelor BR using PDG ### 
### Bachelor BR using PDG ### RR = 0.0806
### Bachelor BR using PDG ### RRstat = .0023
### Bachelor BR using PDG ### RRsyst = .0035
### Bachelor BR using PDG ### R = .0522
### Bachelor BR using PDG ### Rstat = .0019
### Bachelor BR using PDG ### Rsyst = .0014
### Bachelor BR using PDG ### 
### Bachelor BR using PDG ### stat = val_err(R, Rstat)/val_err(RR, RRstat)
### Bachelor BR using PDG ### stat = stat.scale(r.val*Dp/Dz)
### Bachelor BR using PDG ### syst = val_err(R, Rsyst)/val_err(RR, RRsyst)
### Bachelor BR using PDG ### syst = syst.scale(r.val*Dp/Dz)
### Bachelor BR using PDG ### pdg1 = val_err(Dp, Dpe) * r / val_err(Dz, Dze)
### Bachelor BR using PDG ### pdg1 = pdg1.scale(R/RR)
### Bachelor BR using PDG ### pdg2 = r * val_err(Dp, Dpe) / val_err(Dz, Dze)
### Bachelor BR using PDG ### pdg2 = pdg2.scale(R/RR)
### Bachelor BR using PDG ### 
### Bachelor BR using PDG ### print(stat)
### Bachelor BR using PDG ### print(syst)
### Bachelor BR using PDG ### print(pdg1)
### Bachelor BR using PDG ### print(pdg2)
### Bachelor BR using PDG ### # R/RR * r * Dp / Dz













### Lb-Dppipi Analysis, resonant D* mode ### pi0 = (.307, 0.005)
### Lb-Dppipi Analysis, resonant D* mode ### gamma = (.016, 0.004)
### Lb-Dppipi Analysis, resonant D* mode ### r_ = -.44
### Lb-Dppipi Analysis, resonant D* mode ### ratio = (0.05211726384364821, 0.0134244518539487)
### Lb-Dppipi Analysis, resonant D* mode ### print(ratio)
### Lb-Dppipi Analysis, resonant D* mode ### ratio = (.016/.307, ((pi0[1]*gamma[0]/pi0[0]**2)**2 + (gamma[1]/pi0[0])**2 - 2*r_*abs(gamma[0]*gamma[1]*pi0[1]/pi0[0]**3))**.5)
### Lb-Dppipi Analysis, resonant D* mode ### print(ratio)
### Lb-Dppipi Analysis, resonant D* mode ### pi0 = val_err(.307, 0.005)
### Lb-Dppipi Analysis, resonant D* mode ### gamma = val_err(.016, 0.004)
### Lb-Dppipi Analysis, resonant D* mode ### ratio = gamma.add(pi0, r_)
### Lb-Dppipi Analysis, resonant D* mode ### print(ratio.err / ratio.val * 1.9)
### Lb-Dppipi Analysis, resonant D* mode ### print(ratio)

