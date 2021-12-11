
class TweetCounts:
    def get_counts(self, tweets):
        counts = {"country": {"USA": 0, "INDIA": 0, "MEXICO": 0},
                  "sentiment": {"Positive": 0, "Negative": 0, "Neutral": 0}}
        for tweet in tweets:
            if "country" in tweet:
                if tweet["country"] == "USA":
                    counts["country"]["USA"] += 1
                if tweet["country"] == "INDIA" or tweet["country"] == "India":
                    counts["country"]["INDIA"] += 1
                if tweet["country"] == "MEXICO" or tweet["country"] == "Mexico":
                    counts["country"]["MEXICO"] += 1
            if "sentiment" in tweet:
                if tweet["sentiment"] == "Positive" or tweet["sentiment"] == "POSITIVE":
                    counts["sentiment"]["Positive"] += 1
                if tweet["sentiment"] == "Negative" or tweet["sentiment"] == "NEGATIVE":
                    counts["sentiment"]["Negative"] += 1
                if tweet["sentiment"] == "Neutral":
                    counts["sentiment"]["Neutral"] += 1

        return counts

    def get_reply_counts(self, tweets):
        total_counts = {"country": {"USA": 0, "INDIA": 0, "MEXICO": 0},
                "sentiment": {"Positive": 0, "Negative": 0, "Neutral": 0}}
        for tweet in tweets:
            if "replies" in tweet:
                counts = {"country": {"USA": 0, "INDIA": 0, "MEXICO": 0},
                    "sentiment": {"Positive": 0, "Negative": 0, "Neutral": 0}}
                counts["country"]["USA"] = tweet["replies"].count("en")
                total_counts["country"]["USA"] += tweet["replies"].count("en")
                counts["country"]["INDIA"] += tweet["replies"].count("hi")
                total_counts["country"]["INDIA"] += tweet["replies"].count("hi")
                counts["country"]["MEXICO"] += tweet["replies"].count("es")
                total_counts["country"]["MEXICO"] += tweet["replies"].count("es")
                counts["sentiment"]["Positive"] += tweet["replies"].count("Positive")
                total_counts["sentiment"]["Positive"] += tweet["replies"].count("Positive")
                counts["sentiment"]["Negative"] += tweet["replies"].count("Negative")
                total_counts["sentiment"]["Negative"] += tweet["replies"].count("Negative")
                counts["sentiment"]["Neutral"] += tweet["replies"].count("Neutral")
                total_counts["sentiment"]["Neutral"] += tweet["replies"].count("Neutral")
                tweet["reply_counts"] = counts
        return tweets, total_counts

    def get_empty_dict(self):
        return {"country": {"USA": 0, "INDIA": 0, "MEXICO": 0},
                "sentiment": {"Positive": 0, "Negative": 0, "Neutral": 0}}

