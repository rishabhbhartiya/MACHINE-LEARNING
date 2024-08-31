# Calculate the number of missing values in each column
missing_values = data.isna().sum()

# Calculate the percentage of missing values
missing_percentage = (missing_values / len(data)) * 100

# Filter columns with missing values
columns_with_nan = missing_values[missing_values > 0]
percentage_with_nan = missing_percentage[missing_percentage > 0]

# Create a DataFrame with columns, missing values, and missing percentage
missing_data_df = pd.DataFrame({
    'Column': columns_with_nan.index,
    'Missing Values': columns_with_nan.values,
    'Percentage (%)': percentage_with_nan.values
})

# Display the DataFrame
missing_data_df
