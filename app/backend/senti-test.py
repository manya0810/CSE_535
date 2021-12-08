import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
sid = SentimentIntensityAnalyzer()
a = 'This was a good movie.'
print(sid.polarity_scores(a))
temp = sid.polarity_scores(a)
sentiment = ""
if temp['pos'] > temp['neu'] and temp['pos'] > temp['neg']:
    sentiment = "Positive"
elif temp['neu'] > temp['pos'] and temp['neu'] > temp['neg']:
    sentiment = "Neutral"
else:
    sentiment = "Negative"
print(sentiment)
a = 'This was the best, most awesome movie EVER MADE!!!'
print(sid.polarity_scores(a))
a = 'I am feeling sad today'
print(sid.polarity_scores(a))
a = 'I am happy but the movie could have been better'
print(sid.polarity_scores(a))
text = "यह एक अच्छी फिल्म थी।"
text_en = GoogleTranslator(source='auto', target='en').translate(text)
print(sid.polarity_scores(text_en))

