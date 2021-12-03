from newsapi import NewsApiClient



class news:
    def news(self,query):
        newsapi = NewsApiClient(api_key='7a9050d9c94b430393db68ed759fc22f')
        all_articles = newsapi.get_everything(q=query,
                                              sources='bbc-news,the-times-of-india,infobae,reuters,nbc-news,the-washington-post,business-insider',
                                              language='en',
                                              sort_by='relevancy',
                                              page=2)

        return all_articles


