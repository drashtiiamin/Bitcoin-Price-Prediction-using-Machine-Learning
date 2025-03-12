1. Data Collection
Data Source:
The project will use Bitcoin price data from sources like Yahoo Finance, CoinMarketCap, or public APIs for collecting historical data.

Data Format:
The dataset will include columns such as:

Date
Opening Price
Closing Price
High Price
Low Price
Volume
2. Data Preprocessing
In this section, you'll clean and preprocess the collected data, handle missing values, and normalize/scale features for machine learning models.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load Data
data = pd.read_csv('data/bitcoin_historical_data.csv')

# Data Cleaning
data = data.dropna()

# Feature Engineering
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Scaling the data
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data[['Open', 'High', 'Low', 'Close', 'Volume']])

# Save Preprocessed Data
pd.DataFrame(data_scaled, columns=['Open', 'High', 'Low', 'Close', 'Volume']).to_csv('data/processed_bitcoin_data.csv')

