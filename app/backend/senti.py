import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

class sentiment:
    def analyze(self,text):

        sid = SentimentIntensityAnalyzer()
        text_en = GoogleTranslator(source='auto', target='en').translate(text)
        #print(sid.polarity_scores(text_en))
        temp = sid.polarity_scores(text_en)
        sentiment = ""
        if temp['pos'] > temp['neu'] and temp['pos'] > temp['neg']:
            sentiment = "Positive"
            sentiment_score  = temp['pos']
        elif temp['neu'] > temp['pos'] and temp['neu'] > temp['neg']:
            sentiment = "Neutral"
            sentiment_score = temp['neu']
        else:
            sentiment = "Negative"
            sentiment_score = temp['neg']

        return sentiment,sentiment_score
# s = sentiment()
# s.analyze(text="It was a good movie")
# text = "यह एक अच्छी फिल्म थी।"


