import matplotlib.pyplot as plt
import numpy as np

amplitude = 1
x_values = np.linspace(0, 50, 1000)
y_values = amplitude * np.cos(2 * np.pi * x_values / 50)

plt.plot(x_values, y_values, color='red', label='y = cos(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('y = cos(x)')
plt.legend()

plt.show()