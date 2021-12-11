
class ReplyCounts:
    def get_reply_counts(self, tweets):
        reply_counts = {"country": {"USA": 0, "INDIA": 0, "MEXICO": 0}, "sentiment": {"Positive": 0, "Negative": 0, "Neutral": 0}}
        for tweet in tweets:
            if "country" in tweet:
                if tweet["country"] == "USA":
                    reply_counts["country"]["USA"] += 1
                if tweet["country"] == "INDIA" or tweet["country"] == "India":
                    reply_counts["country"]["INDIA"] += 1
                if tweet["country"] == "MEXICO" or tweet["country"] == "Mexico":
                    reply_counts["country"]["MEXICO"] += 1
            if "sentiment" in tweet:
                if tweet["sentiment"] == "Positive":
                    reply_counts["sentiment"]["Positive"] += 1
                if tweet["sentiment"] == "Negative":
                    reply_counts["sentiment"]["Negative"] += 1
                if tweet["sentiment"] == "Neutral":
                    reply_counts["sentiment"]["Neutral"] += 1

