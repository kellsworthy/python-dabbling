# SECTION 1: SETUP
# 1. Import the pandas package with the common pd alias.
# 2. Use help() to explore the pandas read_csv() function.
# 3. Use the pandas read_csv() function to load the data set.
# 4. Save the data set to a variable named indexes.
# 5. Save the symbol, date, and adjusted columns to variables.

# Import packages used
import pandas as pd

# Understand how to use the read_csv() function
# help(pd.read_csv)

# Save the data set to a variable for easy referencing
indexes = pd.read_csv("/Users/kellsworth/Developer/GitHub/python-dabbling/posit-academy/src/files/indexes.csv")

# Save symbol, date, and adjusted columns to variables
symbol = indexes['symbol']
date = indexes['date']
adjusted = indexes['adjusted']

# ==================================================

# SECTION 2: EXPLORE DATA
# 1. Display the contents of indexes.
# 2. Display the contents of the columns saved to variables.
# 3. Use the built-in min() function to find the first date in date.
# 4. Use the built-in max() function to find the last day in date.
# 5. Use the pandas value_counts() function to count the number of records for each symbol.

# Display the content of the full data set
indexes

# Display the content of the individual columns
symbol
date
adjusted

# Understand how to use the value_counts() function
# help(pd.value_counts)

# Run analysis against data
print("First day: ", min(date))
print("Last day: ", max(date))
print("Count per symbol: ", "\n", pd.Series(symbol).value_counts())

# ==================================================

# SECTION 3: EXTENSION
# Expand on your work above by investigating something that interests you.

# Create copy of data frame to preserve original
indexes_extension = indexes

# Add new columns to data frame
indexes_extension["daily_chng_val"] = (indexes_extension["close"] - indexes_extension["open"])
indexes_extension["daily_chng_pct"] = (indexes_extension["daily_chng_val"] / indexes_extension["open"])

# Analyze how symbols may fluctuate from each other
# CONTINUE HERE
