# Calculate the number of missing values in each column
missing_values = data.isna().sum()

# Filter columns with missing values
columns_with_nan = missing_values[missing_values > 0]

# Convert the result to a DataFrame
columns_with_nan_df = columns_with_nan.reset_index()

# Rename the columns for better understanding
columns_with_nan_df.columns = ['Column', 'Missing Values']

# Display the DataFrame
columns_with_nan_df
