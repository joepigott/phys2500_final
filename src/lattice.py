from matplotlib import pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection="3d")

shell = int(input("shell: "))

for i in range(shell):
    for j in range(shell):
        for k in range(shell):
            if (i + j + k) % 2 == 0:
                color = 'red'
            else:
                color = 'green'

            ax.plot(i, j, k, color=color)

plt.show()
