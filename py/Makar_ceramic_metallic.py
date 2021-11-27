import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})
import numpy as np
exp = np.exp



twat = 50
tair = 20

cwat = 4.2*5
ccer = .8*2
cmet = .5*2

tcer = (twat*cwat + tair*ccer) / (cwat + ccer)
tmet = (twat*cwat + tair*cmet) / (cwat + cmet)

lcer = .9
lmet = 50 
lair = .02 


def Tcer(t):
	return tair + (tcer - tair)*exp(-lair*t) + (twat - tcer)*exp(-lcer*t)

def Tmet(t):
	return tair + (tmet - tair)*exp(-lair*t) + (twat - tmet)*exp(-lmet*t)


t = np.arange(0., 150., .1)

plt.plot(t, Tcer(t), ',-r', t, Tmet(t), ',-b')
plt.legend(['Ceramic', 'Metallic'])
plt.xlabel('time')
plt.ylabel('temperature')
plt.show()
