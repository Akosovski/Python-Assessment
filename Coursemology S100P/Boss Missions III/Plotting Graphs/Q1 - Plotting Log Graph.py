import matplotlib.pyplot as plt
import math

x_values = list(range(1, 101))
y_log10 = [math.log10(x) for x in x_values]
y_log2 = [math.log2(x) for x in x_values]

plt.plot(x_values, y_log10, color='red', label='y = log10(x)')
plt.plot(x_values, y_log2, color='blue', label='y = log2(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of y = log10(x) and y = log2(x)')
plt.legend()

plt.show()