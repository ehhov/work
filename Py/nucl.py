__all__ = [
	'unit', 'mp', 'mn', 'me', 
	'Delta', 'Eb', 'Mass', 'NuclMass'
	'ZtoSymbol', 'SymboltoZ',
	'ZtoS', 'StoZ'
]
__doc__ = """
Everything here is in MeV
Delta, Eb, Mass, NuclMass arguments are [Z,A]

unit -- atomic mass unit 
mp, mn, me -- proton, neutron, and electron masses
Delta, Mass -- mass excess and atomic mass 
Eb, NuclMass -- binding energy and nucleus mass 
"""

unit = 931.4940954
mp = 938.2720813
mn = 939.5654133
me = 0.5109989461

data = open('src/masstable.txt','r')
lines = data.readlines()
data.close()

Delta = {}
Eb = {}
Mass = {}
NuclMass = {}

for line in lines:
	inline = line.replace('\n', '').replace('  ',' ').replace('  ',' ').split(' ')
	Z = int(inline[0])
	N = int(inline[1])
	D = float(inline[2])
	Delta[Z, N+Z] = D
	Eb[Z, N+Z] = N*mn+Z*mp - (D + (N+Z)*unit) + Z*me
	Mass[Z, N+Z] = D + (N+Z)*unit
	NuclMass[Z, N+Z] = D + (N+Z)*unit - Z*me 

del N, Z, D, inline, line, lines, data


line = '1 H 2 He 3 Li 4 Be 5 B 6 C 7 N 8 O 9 F 10 Ne 11 Na 12 Mg 13 Al 14 Si 15 P 16 S 17 Cl 18 Ar 19 K 20 Ca 21 Sc 22 Ti 23 V 24 Cr 25 Mn 26 Fe 27 Co 28 Ni 29 Cu 30 Zn 31 Ga 32 Ge 33 As 34 Se 35 Br 36 Kr 37 Rb 38 Sr 39 Y 40 Zr 41 Nb 42 Mo 43 Tc 44 Ru 45 Rh 46 Pd 47 Ag 48 Cd 49 In 50 Sn 51 Sb 52 Te 53 I 54 Xe 55 Cs 56 Ba 57 La 58 Ce 59 Pr 60 Nd 61 Pm 62 Sm 63 Eu 64 Gd 65 Tb 66 Dy 67 Ho 68 Er 69 Tm 70 Yb 71 Lu 72 Hf 73 Ta 74 W 75 Re 76 Os 77 Ir 78 Pt 79 Au 80 Hg 81 Tl 82 Pb 83 Bi 84 Po 85 At 86 Rn 87 Fr 88 Ra 89 Ac 90 Th 91 Pa 92 U 93 Np 94 Pu 95 Am 96 Cm 97 Bk 98 Cf 99 Es 100 Fm 101 Md 102 No 103 Lr 104 Rf 105 Db 106 Sg 107 Bh 108 Hs 109 Mt 110 Ds 111 Rg 112 Cn 113 Nh 114 Fl 115 Mc 116 Lv 117 Ts 118 Og'
line = line.split(' ')

ZtoSymbol = {}
SymboltoZ = {}
for i in range(0, int(len(line)/2)):
	ZtoSymbol[int(line[2*i])] = line[2*i+1]
	SymboltoZ[line[2*i+1]] = int(line[2*i])
ZtoS = ZtoSymbol
StoZ = SymboltoZ

del line, i
