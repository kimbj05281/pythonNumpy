import numpy
import numpy as np
import matplotlib.pyplot as plt

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

r = np.random.rand(3)
print(r)

r1000 = np.random.rand(1000)
plt.hist(r1000)
plt.grid()
plt.show()

rn =np.random.normal(0,1,3) #평균 0, 표준편차 1, 무작위 값 3개
print(rn)

rn1000 = np.random.normal(0,1,1000)
plt.hist(rn1000)
plt.grid()
plt.show()

np.random.seed(0)
print(np.random.rand(3))
np.random.seed(0)
print(np.random.rand(3))