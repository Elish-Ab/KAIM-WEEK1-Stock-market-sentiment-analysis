import pandas as pd
import matplotlib.pyplot as plt

# Generate a sample dataset
data = pd.DataFrame({'Sentiment': ['Positive', 'Negative', 'Neutral'], 'Count': [50, 30, 20]})

# Plot the dataset
plt.bar(data['Sentiment'], data['Count'])
plt.title('Sentiment Distribution')
plt.savefig('artifacts/sentiment_distribution.png')
