import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Set the new NLTK data path
nltk.data.path.append('./nltk_data')

# Download VADER lexicon
nltk.download('vader_lexicon', download_dir='./nltk_data')

# Set the NLTK data path to use the local directory
nltk.data.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'nltk_data'))

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return {
        'sentiment': sentiment,
        'pos_score': sentiment_scores['pos'],
        'neg_score': sentiment_scores['neg'],
        'neu_score': sentiment_scores['neu'],
        'compound_score': sentiment_scores['compound']
    }
