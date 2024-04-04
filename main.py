# Coded with the help of ChatGPT 4


import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = './HistoricalPrices.csv'
data = pd.read_csv(file_path)

# Correcting column names by stripping leading spaces
data.columns = data.columns.str.strip()

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Sort the data by date to ensure chronological order
data.sort_values('Date', inplace=True)

# Determine the unique years present in the dataset
unique_years = data['Date'].dt.year.unique()

# Highlight the first two years, or all available if less than two years of data
highlight_years = unique_years[:2] if len(unique_years) >= 2 else unique_years

# Separate the data for highlighting and for normal presentation
highlight_data = data[data['Date'].dt.year.isin(highlight_years)]
rest_data = data[~data['Date'].dt.year.isin(highlight_years)]

# Plotting
plt.figure(figsize=(10, 6))

# Plot for the rest of the years with normal ink weight
plt.plot(rest_data['Date'], rest_data['Close'], label='Other Years', linewidth=1, color ='blue')

# Plot for the first two years with a larger ink weight
plt.plot(highlight_data['Date'], highlight_data['Close'], label='First Two Years', linewidth=1, color = 'blue')

# Setting the title and labels
plt.title('S&P 500 Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')

# Adjust layout for better presentation
plt.tight_layout()

# Display the plot
plt.show()
