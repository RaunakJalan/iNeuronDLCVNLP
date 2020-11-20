def myfilter(func, list):
	filterArr = [i for i in list if func(i) is True]
	
	return filterArr



'''
Example Functions
'''
def isEven(a):
	if a%2==0:
		return True
	return False

def isOdd(a):
	if a%2!=0:
		return True
	return False

#syntax: filter(function, list)
print(myfilter(isEven,[1,2,3,4,5,6,7,8,9,10]))
