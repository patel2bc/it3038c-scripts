# Must run 'pip install matplotlib' before beginning, this will also install numpy lib

import matplotlib.pyplot as plt
import numpy as np

# Example 1: Plot a simple line graph
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# Example 2: Plot a scatter plot with custom colors and sizes
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
colors = np.random.rand(100)
sizes = 100 * np.random.rand(100)
plt.scatter(x, y, c=colors, s=sizes)
plt.show()

# Example 3: Plot a bar chart with error bars
x = ["A", "B", "C", "D", "E"]
y = [23, 45, 17, 30, 55]
errors = [2, 5, 1, 4, 3]
plt.bar(x, y, yerr=errors, align="center")
plt.show()

# Sources:
# https://numpy.org/install/
# https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm

# By: Bunci Patel

