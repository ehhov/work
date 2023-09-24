from math import sqrt

class val_err: #  {{{
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
# }}}

if __name__ == '__main__':

    piz = val_err(30.7, 0.5)
    gamma = val_err(1.6, 0.4)
    rho = -0.44
    print(gamma.div(piz, rho))

    exit()

    n1 = val_err(1933, 56)
    n1r = val_err(862, 55)
    n0 = val_err(26505, 177)
    print(n1/n0, n1r/n1, sep='\n')
    exit()

    dic = {}
    dic['fitmodel'] = 1.5, 5.7
    dic['multiple'] = 0.8, 0.7
    dic['lbkin'] = 0.2, .4
    dic['doptstarpkin'] = .1, .2
    dic['lckin'] = .3, .0
    dic['pid'] = .7, .5
    dic['track'] = .2, .0
    dic['trig'] = .9, .5
    dic['simreweight'] = 1.9, 2.8
    dic['effstat'] = .8, .9

    signal = 0.0
    normal = 0.0
    for e in dic.values():
        signal = sqrt(signal**2 + e[0]**2)
        normal = sqrt(normal**2 + e[1]**2)
    print(f"signal = {signal}, normal = {normal}")

    simcorr_sources = ['lbkin', 'doptstarpkin', 'lckin', 'simreweight']
    effcorr_sources = ['pid', 'track', 'trig']
    simcorr = [0.0, 0.0]
    for s in simcorr_sources:
        e = dic[s]
        simcorr[0] = sqrt(simcorr[0]**2 + e[0]**2)
        simcorr[1] = sqrt(simcorr[1]**2 + e[1]**2)
    effcorr = [0.0, 0.0]
    for s in effcorr_sources:
        e = dic[s]
        effcorr[0] = sqrt(effcorr[0]**2 + e[0]**2)
        effcorr[1] = sqrt(effcorr[1]**2 + e[1]**2)
    print(f'sim {simcorr}, eff {effcorr}')

    other_sources = ['fitmodel', 'multiple', 'effstat']
    other = [0.0, 0.0]
    for s in other_sources:
        e = dic[s]
        other[0] = sqrt(other[0]**2 + e[0]**2)
        other[1] = sqrt(other[1]**2 + e[1]**2)

    total = [0.0, 0.0]
    total[0] = sqrt(simcorr[0]**2 + effcorr[0]**2 + other[0]**2)
    total[1] = sqrt(simcorr[1]**2 + effcorr[1]**2 + other[1]**2)
    print(total)

    #apo2 = val_err(1.0950, .0126)
    #johnsonsu = val_err(1.1089, .0130)
    #cb2 = val_err(1.1119, .0131)
    #genhyp = val_err(1.0921, .0122)
    #print(johnsonsu - apo2)
    #print(cb2 - apo2)
    #print(genhyp - apo2)
	# do the thing

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

