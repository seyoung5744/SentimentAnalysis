import numpy as np

a = np.array([1,2,3])
print("np.array()")
print(a)
print("==========================")

b = np.array([[1,2,3], [4,5,6]])

print(np.sum(b, axis=1))
print("==========================")

c = np.zeros((2,2))
print("np.zeros()")
print(c)
print("==========================")

d = np.ones((1,2))
print("np.ones")
print(d)
print("==========================")

e = np.full((2,2), 7)
print("np.full()")
print(e)
print("==========================")

