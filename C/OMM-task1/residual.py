import sys
from math import sqrt

setofX=["0","0.064","0.128","0.192","0.256","0.32","0.384","0.448","0.512","0.576","0.64","0.704","0.768","0.832","0.896"]
setofT=["0","0.064","0.128","0.192","0.256","0.32","0.384","0.448","0.512","0.576","0.64","0.704","0.768","0.832","0.896","0.96","1.024","1.088","1.152","1.216","1.28","1.344","1.408","1.472","1.536","1.6","1.664","1.728","1.792","1.856","1.92","1.984","2.048","2.112","2.176","2.24","2.304","2.368","2.432","2.496","2.56","2.624","2.688","2.752","2.816","2.88","2.944","3.008","3.072","3.136","3.2","3.264","3.328","3.392","3.456","3.52","3.584","3.648","3.712","3.776","3.84","3.904"]
#setofT=["0","0.064","0.128","0.192","0.256","0.32","0.384","0.448","0.512","0.576","0.64","0.704","0.768","0.832","0.896"]

file_one=open("task1_"+sys.argv[1]+".dat","r")
file_two=open("task1_"+sys.argv[2]+".dat","r")

mass_one=[]
mass_two=[]

for line in file_one.read().splitlines():
	tmp=line.replace("  "," ").split(" ")
	if(tmp[0] in setofT and tmp[1] in setofX):
		mass_one.append(float(tmp[2]))
for line in file_two.read().splitlines():
	tmp=line.replace("  "," ").split(" ")
	if(tmp[0] in setofT and tmp[1] in setofX):
		mass_two.append(float(tmp[2]))

#tmp=0
for i in range(len(mass_one)):
	print(i, mass_one[i]-mass_two[i])
#	tmp+=abs(mass_one[i]-mass_two[i])
#tmp/=len(mass_one)
#print(tmp)

#tmp=0
#for i in range(len(mass_one)):
#	tmp+=abs(mass_one[i]-mass_two[i])**2
#tmp=sqrt(tmp)/len(mass_one)
#print(tmp)

#tmp=mass_one[0]-mass_two[0]
#for i in range(len(mass_one)):
#	if (abs(tmp)<abs(mass_one[i]-mass_two[i])): tmp=mass_one[i]-mass_two[i]

#print(tmp)
