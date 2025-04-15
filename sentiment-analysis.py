from nltk.sentiment import SentimentIntensityAnalyzer
import re
from collections import Counter

def get_reviews(filepath):
    with open(filepath , "r") as f:
        text = f.read()
        return(re.findall(r'"(.*?)"' , text))

def analyze_sentiments(filepath):
    reviews = get_reviews(filepath)

    # Initialize VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    analysis = []

    for review in reviews:
        # Perform sentiment analysis
        sentiment_score = sid.polarity_scores(review)
        analysis.append(sentiment_score)
    
    tally = Counter()
    for score in analysis:
        if score["compound"] == 0:
            tally["Neutral"] += 1
        elif score["compound"] > 0:
            tally["Positive"] += 1
        else:
            tally["Negative"] += 1

    for key in tally:
        print(f"Review: {key} , Count: {tally[key]}")
analyze_sentiments("reviews.txt")