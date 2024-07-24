import matplotlib.pyplot as plt

# Apply a specific style (ALWAYS AFTER THE IMPORTS)
plt.style.use('dark_background')

# data
years_x = [1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
total_y = [1243, 1543, 1619, 1831, 1960, 2310, 2415, 2270, 1918]
coal_y = [823, 1136, 1367, 1547, 1660, 1927, 1983, 1827, 1352]
gas_y = [171, 200, 166, 175, 228, 280, 319, 399, 529]


# Plot data
plt.plot(years_x, total_y, label="Total")
plt.plot(years_x, coal_y, label="Coal")
plt.plot(years_x, gas_y, label="Natural Gas")

# customize plot
plt.title("USA - CO2 emissions from electricity production")
plt.xlabel('Year')
plt.ylabel("CO2 - M of tons")
plt.xticks([1975, 1995, 2015], ['start', 1995, 'end'])
# plt.yticks([0, 5000])
plt.ylim((0, 3000))

# add legend
plt.legend(loc="best")

# Add grid
# plt.grid(axis="y", linewidth=0.5)
plt.grid()

# save and show plot
plt.savefig('carbon.jpg')
plt.show() # Will open a graph window.
           # Wait for it to be closed to continue script execution
