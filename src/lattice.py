from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

ax = plt.figure().add_subplot(projection="3d")

shell = int(input("shell: "))

for i in range(shell):
    for j in range(shell):
        for k in range(shell):
            if (i + j + k) % 2 == 0:
                color = 'red'
            else:
                color = 'green'

            plt.plot(i, j, k, color=color)

plt.plot(x, y, x**2 + y**2)

plt.show()
