import numpy as np

X = np.array([x for x in range(1,6)])

N=5

opMatrix = np.column_stack([X**(N-i-1) for i in range(N)])

print(opMatrix)


# Another method:
opMatrix1 = np.vander(X,N)
print(opMatrix1)

