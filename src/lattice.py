from matplotlib import pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(projection='3d')

for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            if i == 0 and j == 0 and k == 0:
                color = 'black'
            elif (i + j + k) % 2 == 0:
                color = 'red'
            else:
                color = 'blue'

            ax.scatter(i, j, k, color=color)

plt.show()

