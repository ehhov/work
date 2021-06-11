import nucl

me = nucl.me
mn = nucl.mn
mp = nucl.mp
md   = nucl.NuclMass[1, 2]
mHe3 = nucl.NuclMass[2, 3]
mH3  = nucl.NuclMass[1, 3]
mHe4 = nucl.NuclMass[2, 4]
mBe7 = nucl.NuclMass[4, 7]
mLi7 = nucl.NuclMass[3, 7]

print(2*mp - md - me)
print(md + mp - mHe3)
print(2*mHe3 - mHe4 - 2*mp)
print(mHe3 + mHe4 - mBe7)
print(mBe7 + me - mLi7)
print(mLi7 + mp - mHe4 - mHe4)
print()
print()
print()
print()
print()
print()
