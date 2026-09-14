import pandas as pd
import yfinance as yf

data = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2025-01-01",
    auto_adjust=False
)

data.columns = data.columns.get_level_values(0)

print(data.head())
print(data.shape)
print(data.columns)
data.to_csv("data/AAPL.csv")
print("Data saved successfully.")