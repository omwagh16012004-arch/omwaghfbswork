pn1 = float(input('Enter Principal: '))
tn2 = float(input('Enter Time: '))
rn3 = float(input('Enter Rate: '))

A = pn1*(1+rn3/100) **tn2
CI = (A-pn1)

print("Compound Interest =", CI)