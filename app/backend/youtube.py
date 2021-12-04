class youtube:
    def fetch_videos(self,query):
        import urllib.request
        import re
        query = query.replace(" ","+")

        search_keyword=query
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        video_urls = list()
        for i in range(3):
            video_urls.append("https://www.youtube.com/watch?v=" + video_ids[i])
        return video_urls



