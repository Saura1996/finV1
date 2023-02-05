from pygooglenews import GoogleNews
import pandas as pd
import re
from datetime import datetime

gn = GoogleNews()

def get_news_by_title(search_key):
    stories = []
    search = gn.search(search_key)
    if search is not None:
        newsitem = search['entries']
        for item in newsitem:
            story = {
                'type':'stock market',
                'title': item['title'],
                #'title_detail': item['title_detail'],
                'links':item['links'],
                #'summary': item['summary'],
                #'summary_detail': item['summary_detail'],
                'source': re.search(r'<font color="#6f6f6f">(.*?)</font>', item['summary']).group(1),
                #'source2':item['source'],
                'url': item['link'],
                'timestamp':item['published'],
                'date': datetime.strptime(item['published'], '%a, %d %b %Y %H:%M:%S %Z').strftime("%-d %b %Y"),
                'time': datetime.strptime(item['published'], '%a, %d %b %Y %H:%M:%S %Z').strftime("%H:%M")
                
            }
            stories.append(story)
    return stories

news_data = get_news_by_title('Top Gainers India')
news_data = pd.DataFrame(news_data)
news_data.to_json("news.json", orient="records")
