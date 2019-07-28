import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.exp(x ** 2)
fig = plt.figure()
plt.plot(x, y)
plt.show()
