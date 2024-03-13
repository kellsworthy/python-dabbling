# Import packages used.
import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_line, labs
from matplotlib import pyplot

# Set pandas options for column display and enabling copy.
pd.set_option('display.max_columns', None)
pd.set_option('mode.copy_on_write', True)

# Load dataset to variable.
indexes = pd.read_csv('/Users/kellsworth/Developer/GitHub/python-dabbling/posit-academy/data/indexes.csv')

# Filter data set to GSPC ticker.
indexgspc = indexes.loc[indexes['symbol'] == '^GSPC']

# Create scatterplot of GSPC ticker with each data point connected by a line.
(
    ggplot(data=indexgspc, mapping=aes(x='date', y='adjusted'))
    + geom_point()
    + geom_line(group=1)
    + labs(title='Price history for ^GSPC')
)

# Filter data set to TNX ticker.
indextnx = indexes.loc[indexes['symbol'] == '^TNX']

# Create scatterplot of GSPC ticker with each data point connected by a line.
(
    ggplot(data=indextnx, mapping=aes(x='date', y='adjusted'))
    + geom_point()
    + geom_line(group=1)
    + labs(title='Price history for ^TNX')
)

# Alternate solution using matplotlib to create a dual axis.
# (plotnine does not currently support dual axis)
# Create a blank figure to plot both axis on.
canvas, axisgspc = pyplot.subplots()

# Create first plot for GSPC ticker with axis labels and matching colors.
axisgspc.plot('date', 'adjusted', color='purple', marker='.', linewidth=1, markersize=5, data=indexgspc)
axisgspc.set_xlabel('date')
axisgspc.set_ylabel('GSPC adjusted', color='purple')
axisgspc.tick_params('y', colors='purple')

# Create a second axis that shares the first plot's y-axis.
axistnx = axisgspc.twinx()

# Create second plot for TNX ticker with y-axis labels and matching colors.
axistnx.plot('date', 'adjusted', color='blue', marker='.', linewidth=1, markersize=5, data=indextnx)
axistnx.set_ylabel('TNX adjusted', color='blue')
axistnx.tick_params('y', colors='blue')

# Find the max x- and y-axis values in both plots to be used for annotations.
ymaxgspc = indexgspc['adjusted'].max()
ymaxtnx = indextnx['adjusted'].max()
xmaxgspc = indexgspc['adjusted'].argmax()
xmaxtnx = indextnx['adjusted'].argmax()

# Annotate plots with max values.
axisgspc.annotate(
    f'GSPC max: {ymaxgspc:.0f}',
    xy=(xmaxgspc, ymaxgspc),
    xytext=(xmaxgspc-90, ymaxgspc+10),
    arrowprops=dict(arrowstyle='fancy')
)
axistnx.annotate(
    f'TNX max: {ymaxtnx:.2f}',
    xy=(xmaxtnx, ymaxtnx),
    xytext=(xmaxtnx+15, ymaxtnx-0.02),
    arrowprops=dict(arrowstyle='fancy')
)

# Generate the combined plot with both axis.
pyplot.show()
