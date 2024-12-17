import os
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Set the directory paths for the data
stock_data_dir = '/home/elisha-a/week1/yfinance_data'
news_data_path = '/home/elisha-a/week1/raw_analyst_ratings.csv'

# List of tickers corresponding to the datasets
tickers = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA', 'TSLA']

# Load the entire news dataset
news_data = pd.read_csv(news_data_path, parse_dates=['date'])

# Process each stock ticker
for ticker in tickers:
    print(f"Processing data for {ticker}...")
    
    # Resolve and debug stock file path
    stock_file_path = os.path.join(stock_data_dir, f"{ticker}_historical_data.csv")
    if not os.path.exists(stock_file_path):
        print(f"Stock file for {ticker} not found at {stock_file_path}. Skipping...")
        continue

    # Load stock data
    stock_data = pd.read_csv(stock_file_path, index_col='Date', parse_dates=True)

    # Reset the index to avoid ambiguity with the 'Date' column
    stock_data.reset_index(inplace=True)

    # Filter news data for the current ticker
    ticker_news = news_data[news_data['stock'] == ticker].copy()
    
    # Convert 'date' column to datetime format
    ticker_news['date'] = pd.to_datetime(ticker_news['date'], errors='coerce')
    ticker_news = ticker_news.dropna(subset=['date'])
    ticker_news['date'] = ticker_news['date'].dt.date

    # Ensure stock data has a normalized 'Date' column
    stock_data['Date'] = stock_data['Date'].dt.date

    # Remove timezone information from both columns to avoid merge issues
    stock_data['Date'] = pd.to_datetime(stock_data['Date']).dt.tz_localize(None)
    ticker_news['date'] = pd.to_datetime(ticker_news['date']).dt.tz_localize(None)

    # Perform sentiment analysis on news headlines
    ticker_news['sentiment'] = ticker_news['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    
    # Aggregate sentiment scores by date (average sentiment for each day)
    daily_sentiment = ticker_news.groupby('date')['sentiment'].mean().reset_index()
    
    # Merge stock data with the aggregated sentiment data on the date
    merged_data = pd.merge(
        stock_data, 
        daily_sentiment, 
        left_on='Date', 
        right_on='date', 
        how='inner'
    )
    
    # Calculate daily returns for stock data (percentage change in closing prices)
    merged_data['Daily_Return'] = merged_data['Close'].pct_change() * 100
    
    # Drop NaN values that may result from the calculation of returns
    merged_data = merged_data.dropna(subset=['Daily_Return', 'sentiment'])

    # Check if there are enough data points for correlation
    if len(merged_data) < 2:
        print(f"Not enough data for correlation calculation for {ticker}. Skipping...")
        continue

    # Check for constant columns (if either sentiment or daily returns is constant)
    if merged_data['sentiment'].std() == 0 or merged_data['Daily_Return'].std() == 0:
        print(f"Constant data detected for {ticker}. Skipping correlation calculation...")
        continue

    # Calculate Pearson correlation between sentiment and stock returns
    correlation = merged_data['sentiment'].corr(merged_data['Daily_Return'])
    print(f"Correlation between sentiment and stock returns for {ticker}: {correlation}")
    
    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(merged_data['Date'], merged_data['Daily_Return'], label='Stock Daily Returns', color='blue')
    plt.plot(merged_data['Date'], merged_data['sentiment'], label='Sentiment', color='red')
    plt.title(f"Stock Daily Returns vs News Sentiment for {ticker}")
    plt.xlabel('Date')
    plt.ylabel('Percentage / Sentiment')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Save the processed data to CSV (optional)
    output_file = os.path.join(stock_data_dir, f"{ticker}_processed_data.csv")
    merged_data.to_csv(output_file, index=False)
    print(f"Processed data saved for {ticker} at {output_file}")
