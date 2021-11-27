from sys import argv
from math import sqrt

setofX=[]
for i in range(129):
	setofX.append(str(i/128))
#print(setofX) Точность необходимо считать среднеквадратично

file_one=open("task2-an-k{0}-N{1}.dat".format(argv[1],argv[2]),"r")
file_two=open("task2-k{0}-N{1}.dat".format(argv[1],argv[2]),"r")

u_one=[]
u_two=[]

for line in file_one.read().splitlines():
	tmp=line.split(" ")
	if(tmp!=['']):
		u_one.append(float(tmp[2]))
for line in file_two.read().splitlines():
	tmp=line.split(" ")
	if(tmp!=['']):
		u_two.append(float(tmp[2]))

tmp=0
for i in range(len(u_one)):
	tmp+=abs(u_one[i]-u_two[i])
tmp/=len(u_one)
#print(tmp)

tmp=0
for i in range(len(u_one)):
	tmp+=abs(u_one[i]-u_two[i])**2
tmp=sqrt(tmp/len(u_one))
print(tmp)

tmp=u_one[0]-u_two[0]
for i in range(len(u_one)):
	if (abs(tmp)<abs(u_one[i]-u_two[i])): tmp=u_one[i]-u_two[i]
#print(tmp)
