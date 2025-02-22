import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Read the CSV data into a Pandas DataFrame
data = pd.read_csv("NIFTY 50-18-06-2023-to-18-06-2024.csv")

# Extract closing prices as a NumPy array
closing_prices = data["Close "].to_numpy()

# Separate the data for plotting (dates are not required for regression)
dates = data["Date "]  # Optional for plotting

# Linear Regression using SciPy
slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(closing_prices)), closing_prices)

# Predicted closing prices based on the fitted model
predicted_prices = slope * range(len(closing_prices)) + intercept

# Plot the actual closing prices
plt.plot(dates, closing_prices, marker='o', label='Actual Closing Price')

# Plot the predicted closing prices (as a straight line)
plt.plot(range(len(closing_prices)), predicted_prices, color='red', label='Predicted Closing Price')

# Add labels and title
plt.xlabel("Date ")
plt.ylabel("Closing Price ")
plt.title("NIFTY 50 Closing Prices (Actual vs. Predicted)")

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()

# Print the linear regression equation (optional)
print(f"Linear Regression Equation: y = {slope:.2f}x + {intercept:.2f}")
