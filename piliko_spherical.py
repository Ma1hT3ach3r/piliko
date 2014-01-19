from piliko import *
from piliko_geodesic import *

# spherical geometry.
# See "UnivHypGeom41 Trigonometry in elliptic geometry.mp4.", 
# Norman J Wildberger, University of New South Wales, youtube

# projective point = line through origin (0,0,0)
# projective quadrance = spread between lines through origin
# projective spreads of spherical triangle = proj quadrances of 'polar triangle'

projective_point_sph = vector

def projective_quadrance( p1, p2 ):
	# note, blue quasdrance of vector v is equivalent to the dot-product 
	# of v with itself. lots of dot products here!
	numer = sqr(p1.dot(p2)) 
	denom = quadrance(p1) * quadrance(p2)
	#print 'proj quad. input:',p1,p2
	#print 'p1 dot p2',p1.dot(p2)
	#print 'numer,denom',numer,denom
	#print 'output:', 1 - Fraction( numer, denom )
	return 1 - Fraction( numer, denom )

def find_polar_triangle( spherical_tri ):
	t = spherical_tri
	b1 = t.p3.cross(t.p2)
	b2 = t.p1.cross(t.p3)
	b3 = t.p2.cross(t.p1)
	return spherical_triangle( b1,b2,b3 )

# note - this seems to break if the points are given in 'clockwise' order
# (as seen from outside the sphere)
class spherical_triangle:
	def __init__(self, p1,p2,p3): self.p1,self.p2,self.p3=p1,p2,p3
	def quadrances(self):
		p1,p2,p3=self.p1,self.p2,self.p3
		q1 = projective_quadrance( p2, p3 )
		q2 = projective_quadrance( p1, p3 )
		q3 = projective_quadrance( p1, p2 )
		return q1,q2,q3
	def spreads(self):
		pt = find_polar_triangle(self)
		return pt.quadrances()
	def __str__(self): return spherical_triangle_txt(self)
	def __repr__(self): return spherical_triangle_txt(self)
	def __getitem__( self, i ):
                if i==0: return self.p1
                if i==1: return self.p2
                if i==2: return self.p3

def sph_tri_tess( tri, splits, sphere_quadrance ):
	tris = geo_splitn( tri, splits )
	tris2 = geo_project( tris, sphere_quadrance )
	return tris2

def testsph():
	pa = projective_point_sph(1,2,3)
	pb = projective_point_sph(4,-1,2)
	qab = projective_quadrance(pa,pb)
	print 'pa,pb,q pa pb',pa,pb,qab
	
	a1 = projective_point_sph(0,1,0)
	a2 = projective_point_sph(1,0,0)
	a3 = projective_point_sph(0,0,1)
	print 'tri: a1,a2,a3:',a1,a2,a3,
	q1 = projective_quadrance(a2,a3)
	q2 = projective_quadrance(a1,a3)
	q3 = projective_quadrance(a1,a2)
	print ' q1,q2,q3:',q1,q2,q3

	a1=projective_point_sph( 1,-1,2 )
	a2=projective_point_sph( 3,1,1 )
	a3=projective_point_sph( 1,2,-2 )
	st = spherical_triangle( a1,a2,a3 )
	print '\ntri: a1,a2,a3:',a1,a2,a3
	print 'quads:',st.quadrances()
	print 'polar tri:',find_polar_triangle( st )
	print 'spreads:',st.spreads()
	q1,q2,q3 = st.quadrances()
	s1,s2,s3 = st.spreads()
	print 'spread law:',Fraction(s1,q1),Fraction(s2,q2),Fraction(s3,q3)
	print 'cross law: lhs:',sqr(s1*q2*q3-q1-q2-q3+2),
	print 'rhs:',4*(1-q1)*(1-q2)*(1-q3)
	print 'dual of cross law: lhs:',sqr(q1*s2*s3-s1-s2-s3+2),
	print 'rhs:',4*(1-s1)*(1-s2)*(1-s3)


	print
	a1=projective_point_sph( 3,4,0 )
	a2=projective_point_sph( 0,3,4 )
	a3=projective_point_sph( 3,0,4 )
	st = spherical_triangle( a1,a2,a3 )
	pt = find_polar_triangle( st )
	q1,q2,q3 = st.quadrances()
	s1,s2,s3 = st.spreads()
	print '\ntri: a1,a2,a3:',a1,a2,a3
	print 'quads:',q1,q2,q3
	print 'spreads:',s1,s2,s3
	print 'polar tri:',pt
	print 'spread law:',Fraction(s1,q1),Fraction(s2,q2),Fraction(s3,q3)
	print 'cross law: lhs:',sqr(s1*q2*q3-q1-q2-q3+2),
	print 'rhs:',4*(1-q1)*(1-q2)*(1-q3)
	print 'dual of cross law: lhs:',sqr(q1*s2*s3-s1-s2-s3+2),
	print 'rhs:',4*(1-s1)*(1-s2)*(1-s3)

	#triangles_to_stl( [st,pt] )
	open('out.stl','w').write( triangles_to_stl( st,pt ) )
	print 'wrote to out.stl'



	print
	a1=projective_point_sph( 4,3,0 )
	a2=projective_point_sph( 3,4,0 )
	a3=projective_point_sph( 3,4,1 )
	st = spherical_triangle( a1,a2,a3 )
	pt = find_polar_triangle( st )
	q1,q2,q3 = st.quadrances()
	s1,s2,s3 = st.spreads()
	print '\ntri: a1,a2,a3:',a1,a2,a3
	print 'quads:',q1,q2,q3
	print 'spreads:',s1,s2,s3
	print 'polar tri:',pt
	print 'spread law:',Fraction(s1,q1),Fraction(s2,q2),Fraction(s3,q3)
	print 'cross law: lhs:',sqr(s1*q2*q3-q1-q2-q3+2),
	print 'rhs:',4*(1-q1)*(1-q2)*(1-q3)
	print 'dual of cross law: lhs:',sqr(q1*s2*s3-s1-s2-s3+2),
	print 'rhs:',4*(1-s1)*(1-s2)*(1-s3)
	print 'sph pythag thm, s1=1 -> q1 = q2+q3-q2q3 :', q1, '=',q2+q3-q2*q3
	print 'dual sph pythag thm, q1=1 -> s1 = s2+s3-s2s3 :', s1, '=',s2+s3-s2*s3
	t2 = sph_tri_tess( pt, 15, 1 )
	t = sph_tri_tess( st, 15, 1 )
	open('out2.stl','w').write( triangles_to_stl( t+t2 ) )
	print 'wrote to out2.stl'
testsph()

