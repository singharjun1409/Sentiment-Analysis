import nltk
import ssl
from nltk.sentiment import SentimentIntensityAnalyzer
# Download VADER lexicon
#ssl._create_default_https_context = ssl._create_unverified_context
#nltk.download('vader_lexicon')
# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()
# Sample text for sentiment analysis
text = "I love this product! It's amazing."
# Perform sentiment analysis
sentiment_score = sid.polarity_scores(text)
# Print sentiment score 
print(sentiment_score)