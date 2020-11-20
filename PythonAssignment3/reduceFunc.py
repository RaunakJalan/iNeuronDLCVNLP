def myreduce(func, list):
	s=0
	for i in list:
		s=func(s,i)
	return s

'''
example functions for debugging
'''
def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mult(a,b):
	return a*b


# syntax: reduce(function name, list)
print(myreduce(add, [10,20,30,40,50]))
