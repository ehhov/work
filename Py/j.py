import err






#import nucl 
#from collections import defaultdict
#import matplotlib.pyplot as plt
#
#e = {}
#e = defaultdict(lambda: 0, e)
#for z,a in nucl.Eb:
#	e[a] = max(nucl.Eb[z,a], e[a]) / a
#x = [i for i in e]; x.sort()
#y = [e[i] for i in x]
#plt.plot(x, y)
#plt.show()






















###  from err import val_err
###  
###  pi = val_err(.307, .005)
###  gamma = val_err(.016, .004)
###  rho = -.44
###  
###  ratio = gamma.div(pi, rho)
###  print(ratio)
###  
###  N1 = val_err(3862, 79)
###  N1r = val_err(1792, 120)
###  N1nr = val_err(822, 523)
###  
###  Nratio = N1r / N1
###  print(Nratio)
###  
###  N1_TOS = val_err(1954, 57)
###  N1r_TOS = val_err(929, 76)
###  N1nr_TOS = val_err(300, 318)
###  
###  Nratio_TOS = N1r_TOS / N1_TOS
###  print(Nratio_TOS)
