from openpyxl.chart import marker

print("Data visualization in Python")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame([np.array([1,2,3,4,5,6,7,8]), np.array([12, 13, 14, 15, 16, 17, 18, 19])])

print(data)

data.plot()
plt.title("Data visualization")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Scatter Plotting
x = [1,2,3,4,5,6,7]
y = [8,6,5,4,3,2,1]
plt.scatter(x,y)
plt.show()

# Histogram Plotting

import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
data = np.random.normal(0, 1, 1000)

# Plot the data
plt.hist(data, bins=30)

# Add labels and a title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Show the plot
plt.show()


# Box Plotting
import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
data = [np.random.normal(0, 1, 100) for i in range(3)]

# Plot the data
plt.boxplot(data)

# Add labels and a title
plt.xlabel('Variable')
plt.ylabel('Value')
plt.title('Box Plot')

# Show the plot
plt.show()

