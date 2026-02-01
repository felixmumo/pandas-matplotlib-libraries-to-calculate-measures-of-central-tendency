#measures of central tendency
import pandas as pd
import numpy as np
#campture the five numbers from the user 
data = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    data.append(num)
# create a pandas Series
series = pd.Series(data)
#print the data
print("Data:", series.tolist())
# calculate mean
mean = series.mean()
# calculate median
median = series.median()
# calculate mode    
mode = series.mode().tolist()
# print the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
#display a bar chart
import matplotlib.pyplot as plt
plt.bar(range(1, 6), series)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Bar Chart of Input Numbers')
plt.show()


