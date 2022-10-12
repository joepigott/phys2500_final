from matplotlib import pyplot as plt

# initialize figure
fig = plt.figure()

# create 3d subplot
ax = fig.add_subplot(projection='3d')

# loop through the first shell
for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            if i == 0 and j == 0 and k == 0: # origin
                color = 'black'
            elif (i + j + k) % 2 == 0:       # positive (Na)
                color = 'red'
            else:                            # negative (Cl)
                color = 'blue'

            # plot the current coordinate
            ax.scatter(i, j, k, color=color) # throws error but works?

# show plot
plt.show()

