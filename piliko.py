# very, very basic implementation of some Rational Geometry formulas
# in two dimensions.

# Rational Geometry tries to stick to Rational numbers, here
# we use python's "Fraction" type to represent rationals.

# Rational Geometry is from Norman J Wildberger. This code is not affiliated
# with him nor endorsed by him in any way. See the README for info.

#
# todo
# simplify code
# use actual test suite
# deal with /0 and other problems
# implement non-implemented stuff

# split out print functions from basic code? sep presentation w data...
 
# add args* based triangle constructor (points or lines)
#   enable omega triangle

# what is omega inverse?

from fractions import Fraction

def rat( x, y ):
	return Fraction( x, y )

def sqr( x ):
	return x*x

class point:
	x,y=0,0
	def __init__(self, x, y):
		if (type(x) is float): raise Exception("Rationals only please")
		if (type(y) is float): raise Exception("Rationals only please")
		self.x,self.y=x,y
	def dump_coords( self ):
		return '('+str(self.x)+','+str(self.y)+')'
	def __str__( self ):
		return self.dump_coords()

class line:
	# line formula here is ax + by + c = 0
	a,b,c=0,0,0
	def __init__( self, a, b, c ): 
		if (type(a) is float): raise Exception("Rationals only please")
		if (type(b) is float): raise Exception("Rationals only please")
		if (type(c) is float): raise Exception("Rationals only please")
		self.a,self.b,self.c=a,b,c
	def __str__( self ):
		return '<'+str(self.a)+":"+str(self.b)+":"+str(self.c)+'>'


class lineseg:
	p0,p1=point(0,0),point(0,0)
	def __init__(self,p0,p1):
		self.p0,self.p1=p0,p1
	def dump_pts( self ):
		return str(self.p0) +'-'+str(self.p1)
	def dump_eqn( self ):
		return 'not implemented'
	def __str__( self ):
		return self.dump_pts()
	def quadrance( self ):
		return quadrance( self.p0, self.p1 )

class triangle:
	l0,l1,l2=line(0,0,0),line(0,0,0),line(0,0,0)
	p0,p1,p2=None,None,None
	ls0,ls1,ls2=None,None,None
	q0,q1,q2=None,None,None
	s0,s1,s2=[None]*3
	def __init__( self, l0, l1, l2 ):
		self.init_from_lines( l0, l1, l2 )

	def init_from_lines( self, l0, l1, l2 ):
		p0,p1,p2 = meet(l1,l2),meet(l0,l2),meet(l0,l1)
		ls0,ls1,ls2 = lineseg(p1,p2),lineseg(p0,p2),lineseg(p0,p1)
		q0,q1,q2=quadrance(ls0),quadrance(ls1),quadrance(ls2)
		s0,s1,s2=spread(l1,l2),spread(l0,l2),spread(l0,l1)

		self.l0,self.l1,self.l2=l0,l1,l2
		self.p0,self.p1,self.p2=p0,p1,p2
		self.ls0,self.ls1,self.ls2=ls0,ls1,ls2
		self.q0,self.q1,self.q2=q0,q1,q2
		self.s0,self.s1,self.s2=s0,s1,s2

	def dump_spreads( self ):
		return 'spreads:'+str(self.s0)+','+str(self.s1)+','+str(self.s2)
	def dump_lineqs( self ):
		return 'line eqs:'+str(self.l0)+','+str(self.l1)+','+str(self.l2)
	def dump_linesegs( self ):
		return 'line segs:'+str(self.ls0)+' '+str(self.ls1)+' '+str(self.ls2)
	def dump_pts( self ):
		return 'points:'+str(self.p0)+','+str(self.p1)+','+str(self.p2)
	def dump_quadrances( self ):
		return 'quadrances:'+str(self.q0)+','+str(self.q1)+','+str(self.q2)
	def __str__( self ):
		s = '\n  ' + self.dump_lineqs()
		s+= '\n  ' + self.dump_linesegs()
		s+='\n  ' + self.dump_pts()
		s+='\n  ' + self.dump_spreads()
		s+='\n  ' + self.dump_quadrances()
		return s



def red_quadrance( p1, p2 ):
	return sqr( p2.x-p1.x ) - sqr( p2.y-p1.y )

def green_quadrance( p1, p2 ):
	return 2*( p2.x-p1.x ) * ( p2.y-p1.y )

def blue_quadrance( p1, p2 ):
	return sqr( p2.x-p1.x ) + sqr( p2.y-p1.y )

def quadrance( *args ):
	p0,p1 = None,None
	if len(args)==2:
		if isinstance(args[0],point) and isinstance(args[1],point):
			p0,p1 = args[0],args[1]
	elif len(args)==1:
		if isinstance(args[0],lineseg):
			p0,p1 = args[0].p0, args[0].p1

	if p0==None and p1==None:
		raise Exception("unknown type for quadrance() " + str(args))
	else:
		return blue_quadrance( p0, p1 )

# fixme - if a1^2 - bq^2 = 0 then l1 = null line
# both must be non null
def red_spread( l1, l2 ):
	a1,b1,c1 = l1.a, l1.b, l1.c
	a2,b2,c2 = l2.a, l2.b, l2.c
	numerator = -1 * sqr(a1*b2-a2*b1)
	denominator = (a1*a1-b1*b1)*(a2*a2-b2*b2)
	return Fraction( numerator, denominator )

def green_spread( l1, l2 ):
	a1,b1,c1 = l1.a, l1.b, l1.c
	a2,b2,c2 = l2.a, l2.b, l2.c
	numerator = -1 * sqr(a1*b2-a2*b1)
	denominator = 4 * a1 * a2 * b1 * b2
	return Fraction( numerator, denominator )
	
def blue_spread( l1, l2 ):
	a1,b1,c1 = l1.a, l1.b, l1.c
	a2,b2,c2 = l2.a, l2.b, l2.c
	numerator = sqr(a1*b2-a2*b1)
	denominator = (a1*a1+b1*b1)*(a2*a2+b2*b2)
	return Fraction( numerator, denominator )

def spread( l1, l2 ):
	return blue_spread( l1, l2 )

# fixme - what if dont meet? what if same line?
# what if a,b,c all 0?
def meet( l1, l2 ):
	a1,b1,c1 = l1.a, l1.b, l1.c
	a2,b2,c2 = l2.a, l2.b, l2.c
	x = Fraction( b2*c1-b1*c2, a2*b1-a1*b2 )
	y = Fraction( a2*c1-a1*c2, b2*a1-b1*a2 )
	return point( x, y )

def intersection( l1, l2 ):
	return meet( l1, l2 )

def is_green_perpendicular( l1, l2 ):
	raise Exception(" not implemented ")
	
def is_red_perpendicular( l1, l2 ):
	raise Exception(" not implemented ")
	
def is_blue_perpendicular( l1, l2 ):
	return spread( l1, l2 ) == 1

def is_perpendicular( l1, l2):
	return is_blue_perpendicular( l1, l2 )

def is_paralell( l1, l2):
	return spread( l1, l2 ) == 0

def is_parallel( l1, l2):
	return paralell( l1, l2 )




# calculate left hand side and right hand side of various formulas


def triple_quad_lhs( q0, q1, q2 ):
	return sqr(q0+q1+q2)

def triple_quad_rhs( q0, q1, q2 ):
	return 2*( q0*q0 + q1*q1 + q2*q2 )

def quadruple_quad_lhs( q0, q1, q2, q3 ):
	term0 = sqr( q0 + q1 + q2 + q3 )
	term1 = q0*q0 + q1*q1 + q2*q2 + q3*q3
	return sqr( term0 - 2*term1 )

def quadruple_quad_rhs( q0, q1, q2, q3 ):
	return 64 * q0 * q1 * q2 * q3

def cross_law_lhs( tri ):
	return sqr(tri.q0+tri.q1-tri.q2)
	
def cross_law_rhs( tri ):
	cross = 1-tri.s2
	return 4*tri.q0*tri.q1*(cross)

def spread_law( tri ):
	a,b,c = tri.s0/tri.q0 , tri.s1/tri.q1 , tri.s2/tri.q2
	return str(a)+', '+str(b)+', '+str(c)

def triple_spread_lhs( tri ):
	return sqr( tri.s0 + tri.s1 + tri.s2 )

def triple_spread_rhs( tri ):
	s0,s1,s2 = tri.s0, tri.s1, tri.s2
	return 2 * ( s0*s0 + s1*s1 + s2*s2 ) + 4*s0*s1*s2

def pythagoras_lhs( tri ):
	return tri.q0 + tri.q1

def pythagoras_rhs( tri ):
	return tri.q2

def colored_quadrance_lhs( p0, p1 ):
	return sqr(blue_quadrance( p0, p1 ))

def colored_quadrance_rhs( p0, p1 ):
	return sqr(red_quadrance(p0, p1)) + sqr(green_quadrance(p0, p1))

def colored_spread_lhs( l0, l1 ):
	bs = blue_spread( l0, l1 )
	rs = red_spread( l0, l1 )
	gs = green_spread( l0, l1 )
	return 1/bs + 1/rs + 1/gs

def colored_spread_rhs( l0, l1 ):
	return 2


def red_orthocenter( tri ):
	raise Exception(" not implemented ")
def green_orthocenter( tri ):
	raise Exception(" not implemented ")
def blue_orthocenter( tri ):
	raise Exception(" not implemented ")


def red_centroid( tri ):
	raise Exception(" not implemented ")
def green_centroid( tri ):
	raise Exception(" not implemented ")
def blue_centroid( tri ):
	raise Exception(" not implemented ")


def red_circumcenter( tri ):
	raise Exception(" not implemented ")
def green_circumcenter( tri ):
	raise Exception(" not implemented ")
def blue_circumcenter( tri ):
	raise Exception(" not implemented ")


def omega_triangle( tri ):
	o0 = red_orthocenter( tri )
	o1 = green_orthocenter( tri )
	o2 = blue_orthocenter( tri )
	return triangle( o0, o1, o2 )

