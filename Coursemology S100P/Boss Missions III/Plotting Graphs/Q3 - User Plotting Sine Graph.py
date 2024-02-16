import matplotlib.pyplot as plt
import numpy as np

amplitude = 1
x_values = np.linspace(0, 50, 1000)
y_values = amplitude * np.sin( 2 * np.pi * x_values / 50)

plt.plot(x_values, y_values, color='red', label='y = sin(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('y = sin(x)')
plt.legend()

plt.show()