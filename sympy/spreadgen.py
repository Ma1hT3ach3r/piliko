# symbolically calculate the spread polynomial S_N given n

# using the Explicit Formula, p 106 of Divine Proportions, Norman J Wildberger

from sympy import *
s,r,C,D,n=symbols('s,r,C,D,n')

#s=ю**2
r=sqrt(4*s*(1-s))
C=1-2*s+I*r
D=1-2*s-I*r

factors={}

def spread_poly(n):
	spoly = Rational(1,4)*(2 - C**n - D**n)
	return spoly

def slatex(x):
	return x
#	return latex(x)

for i in range(0,32):
	sp = spread_poly(i)
	print( 'S_'+str(i),'=',slatex(simplify(sp)) )
	print( 'S_'+str(i),'=',slatex(factor(sp)) )
	fl = factor_list(sp)
	for j in range(len(fl[1])):
		afactor = fl[1][j][0]
		repeats = fl[1][j][1]
		factors[str(afactor)]=factors.get(str(afactor),0)+repeats
		print( str(i) + 'f' + str(j),slatex(afactor), ',',repeats,',',factors[str(afactor)])
	if i==0: roots=[]
	else: roots=Poly(sp).all_roots(multiple=False)
	for j in range(len(roots)):
		r = roots[j]
		print( str(i)+'r'+str(j),' ',slatex(r[0]),',',slatex(r[1]) )
		#	print ( r[0].expr )
	print()

for k in factors:
	print(k,',',factors[k])
