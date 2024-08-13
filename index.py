import numpy
import numpy as np

narray = np.array([[1,3,5,7,9],[2,4,6,8,10]])
print(narray.shape)
d52 = narray.reshape(5,2)
print(d52.shape)
d10 = narray.reshape(10,)
print(d10.shape)

zero = np.zeros((2,5))
print(zero)

one = np.ones((2,5))
print(one)