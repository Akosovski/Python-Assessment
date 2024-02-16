import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0, 10, 100)
y_values = np.exp(x_values)

plt.plot(x_values, y_values, color='red', label='y = e^x')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Graph: y = e^x')
plt.legend()

plt.show()