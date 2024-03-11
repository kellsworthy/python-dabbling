# Import packages used.
import pandas as pd

# Set option to display all table columns.
pd.set_option('display.max_columns', None)

# Load the data set and save as variable for later use.
indexes0 = pd.read_csv("/Users/kellsworth/Developer/GitHub/python-dabbling/posit-academy/data/indexes.csv")

# Save individual columns as variables for later use.
symbol = indexes0['symbol']
date = indexes0['date']
adjusted = indexes0['adjusted']

# Display the content of the full data set and individual columns.
print(indexes0)
print(symbol)
print(date)
print(adjusted)

# Run analyses against data.
print("First day: ", min(date))
print("Last day: ", max(date))
print("Count per symbol: ",  "\n", pd.value_counts(symbol))

# Copy dataframe to preserve original.
indexes1 = pd.DataFrame(indexes0)

# Add new columns to dataframe for extension work.
indexes1["daily_chng_val"] = (indexes1["close"] - indexes1["open"])
indexes1["daily_chng_pct"] = (indexes1["daily_chng_val"] / indexes1["open"])

# All symbols have the same count of values. How might they differ?
aggindexes = indexes1.groupby("symbol")[["open", "close", "daily_chng_val", "daily_chng_pct"]].mean()
print("Averages by symbol: ", "\n", aggindexes)
