# Import packages used.
import pandas as pd
from matplotlib import rcParams
from plotnine import ggplot, aes, geom_line, geom_step, labs

# Enable copy on write, display all columns, and prevent legend from cutting off.
pd.set_option('mode.copy_on_write', True)
pd.set_option('display.max_columns', None)
rcParams.update({'savefig.bbox': 'tight'})

# Import data set and save to variable.
indexes = pd.read_csv('/Users/kellsworth/Developer/GitHub/python-dabbling/posit-academy/data/indexes.csv')

# View solution to be recreated in next steps.
solution = pd.read_csv('/Users/kellsworth/Developer/GitHub/python-dabbling/posit-academy/data/03-solution.csv')
solution

# Filter to only the GSPC ticker and save to a new DataFrame.
index = indexes.loc[indexes['symbol'] == '^GSPC']
index

# Create a new column that contains the previous values from the adjusted column.
index['lag'] = index['adjusted'].shift(1)

# Create a new column to calculate daily return for each row.
index['daily_return'] = 1 + ((index['adjusted'] - index['lag']) / index['lag'])

# Replace any NaN values in daily_return with 1.
index['daily_return'] = index['daily_return'].fillna(1)

# Create new column that calculates cumulative product on daily_return.
index['growth'] = index['daily_return'].cumprod()

# Remove lag column from DataFrame.
index = index.drop(columns='lag')

# View final version of solution recreation.
index

# Create line graph based on growth and date columns of index DataFrame.
g = (ggplot(data=index, mapping=aes(x='date', y='growth'))
    + geom_line(group=1))
g.show()

# Create new column that calculates cumulative maximum on daily_return.
index['maximum_growth'] = index['daily_return'].cummax().round(3)

# Select every 7 rows to minimize number of data points plotted.
index = index.iloc[::7]

# View index DataFrame with the additional column added.
index

# Create plot to visualize how cumulative max changes over time.
(
    ggplot(data=index, mapping=aes(x='date', y='growth'))
    + geom_step(group=1, alpha=0.25, size=3)
    + geom_line(group=1, mapping=aes(color='factor(maximum_growth)'), size=1)
    + labs(title="GSPC Growth Over Time", color='maximum growth')
)
