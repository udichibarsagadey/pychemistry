import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=32)

print(arr)
print('number of dimensions :', arr.ndim)

arr = np.array(42)

print(arr)
# 1D array {d= dimention}
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print('__________________________________________')
# 2D array {d= dimention}
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
print('__________________________________________')
# 3D array {d= dimention}
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
print(arr)
print('__________________________________________')
# 4D array {d= dimention}
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6],[7,8,9],[10,11,12]])
print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
e = np.array([[[1, 2, 3], [4, 5, 6],[7,8,9],[10,11,12]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)

arr = np.array([1, 2, 3, 4], ndmin=32)

print(arr)
print('number of dimensions :', arr.ndim)