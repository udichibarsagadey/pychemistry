import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))

import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
print('___________________________________')

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = []

for element in arr:

  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)