import pandas as pd

# Read the data from a CSV file
data = pd.read_csv('data.csv')

# Perform data analysis
# You can use various pandas functions to analyze the data, such as:
# - data.head() to display the first few rows of the data
# - data.describe() to get summary statistics of the data
# - data.groupby('column_name').mean() to calculate the mean of a specific column
# - data['column_name'].value_counts() to count the occurrences of each value in a column

# Example: Display the first few rows of the data
print(data.head())

# Example: Calculate the mean of a specific column
mean_age = data['Age'].mean()
print("Mean age:", mean_age)

# Example: Count the occurrences of each value in a column
gender_counts = data['Gender'].value_counts()
print("Gender counts:")
print(gender_counts)