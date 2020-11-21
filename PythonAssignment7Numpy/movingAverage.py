import numpy as np

def movingaverage(data, k=3):
	sumData = np.cumsum(data, dtype=float)
	sumData[k:] = sumData[k:]-sumData[:-k]
	return sumData[k-1:]/k


test = [3,5,7,2,8,10,11,65,72.81,99,100,150]
k=3
print(movingaverage(test,k))
