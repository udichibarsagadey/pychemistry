import numpy as np
import matplotlib.pyplot as plt

m = np.sin(180)
print(m)
v = np.sin(90)
print(v)
f = np.cos(180)
print(f)
i = np.tan(180)
print(i)
x_sin = np.arange(0,25*np.pi,0.1)
print(x_sin)
y_sin = np.sin(x_sin)
print(y_sin)

plt.plot(x_sin,y_sin)
plt.show()


