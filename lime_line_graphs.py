from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
plt.figure(figsize=(12,8))

# Write the command to create the left subplot. Save this subplot in a variable called ax1
ax1 = plt.subplot(1,2,1)
# In the left subplot, we are going to plot the total page visits over the past year as a line.
x_values = range(len(months))

# Plot the total page visits against these x_values as a line.
plt.plot(x_values, visits_per_month, marker='o')

# Label the x-axis and y-axis with descriptive titles of what they measure.
plt.xlabel('Months')
plt.ylabel('Visits Per Month')

# Set the x-axis ticks to be the x_values.
ax1.set_xticks(x_values)

# Label the x-axis tick labels to be the names stored in the months list.
ax1.set_xticklabels(months)

# Add a title to each of the two plots you've created.
plt.title('Site Visits per Month')

# Write the command to create the right subplot.Save this subplot in a variable called ax2
ax2 = plt.subplot(1,2,2)

# In the subplot on the right, we are going to plot three lines on the same set of axes. 
plt.plot(x_values, key_limes_per_month, color='green')
plt.plot(x_values, persian_limes_per_month, color='orange')
plt.plot(x_values, blood_limes_per_month, color='red')

# Add a legend to differentiate the lines, labeling each lime species.
plt.legend(['Key limes', 'Persian limes', 'Blood limes'])

# Set the x-axis ticks to be the x_values, and the tick labels to be the months list.
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)

# Add a title to each of the two plots you've created.
plt.title('Limes Sold per Month')

# Now, save your figure as a png with a descriptive file name.
plt.savefig('SublimeLimes.png')

plt.show()
