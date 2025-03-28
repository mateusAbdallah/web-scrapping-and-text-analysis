# %%
import pandas as pd
import nltk
import string


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')


# %%
df = pd.read_csv('data/wiki_paragraphs.csv')
df

# %%
# Tokenizing column first_paragraph
df['tokens'] = df['first_paragraph'].apply(lambda x: word_tokenize(x))

# Removing stopwords
stop_words = set(stopwords.words('english'))
df['filter_tokens'] = df['tokens'].apply(lambda x: [word for word in x if word.lower() not in stop_words])


# %%
# Remove punctuation
def remove_punc(text):
    return ' '.join([char for char in text if char not in string.punctuation])

df['clean_text'] = df['filter_tokens'].apply(remove_punc)

# %%
# Sentiment Analysis using NLTK

sent_analyzer = SentimentIntensityAnalyzer()
df['sentiment_score'] = df['clean_text'].apply(lambda x: sent_analyzer.polarity_scores(x)['compound'])

# %%

def classify_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'
    
df['sentiment_category'] = df['sentiment_score'].apply(classify_sentiment)

