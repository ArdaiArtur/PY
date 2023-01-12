import matplotlib.pyplot as plt

# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 9, 4, 10]

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Add axis labels
ax.set(xlabel='x', ylabel='y',
       title='A simple line plot')

# Show the plot
plt.show()