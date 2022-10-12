from matplotlib import pyplot as plt

# generates the plot for the convergence of the Madelung constant.

# number of shells computed
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

# data from main.py
y = [-1.69258, -1.71940, -1.72864, -1.73331, -1.73613, -1.73802, -1.73938, -1.74039, -1.74119, -1.74182, -1.74234, -1.74277, -1.74314, -1.74346, -1.74373]

# plot the points
plt.plot(x, y)

# horizontal line for textbook value
plt.axhline(y = -1.74757, color='red') # throws error but works?

# axis labels
plt.xlabel("# of shells")
plt.ylabel("Madelung constant")

# show plot
plt.show()
