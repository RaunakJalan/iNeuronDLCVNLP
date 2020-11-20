class Triangle:
	def __init__(self, s1, s2, s3):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3

class TriangleArea(Triangle):
	def __init__(self, s1, s2, s3):
		super(TriangleArea, self).__init__(s1,s2,s3)
	
	def area(self):
		s = (self.s1 + self.s2 + self.s3)/2
		res = (s*(s-self.s1)*(s-self.s2)*(s-self.s3))**0.5
		return res

triangle = TriangleArea(3,4,5)
print("Triangle area: {}".format(triangle.area()))
