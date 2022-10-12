from matplotlib import pyplot as plt

# generates plot for the convergence of total electric potential.

# number of shells computed
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

# data from main.py
y = [-8.64274, -8.77970, -8.82686, -8.85072, -8.86514, -8.87479, -8.88170, -8.88689, -8.89094, -8.89418, -8.89683, -8.89905, -8.90092, -8.90253, -8.90393]

# plot points
plt.plot(x, y)

# axis labels
plt.xlabel("# of shells")
plt.ylabel("Potential (V)")

# show plot
plt.show()
