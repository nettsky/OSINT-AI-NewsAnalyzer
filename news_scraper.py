#collecting news

import requests
from bs4 import BeautifulSoup
import pandas
from textblob import TextBlob

url = "https://www.bbc.com/news"

#get content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

def analyze_sentiment(text):
    '''assessment of text emotion'''
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Possitive 😊"
    elif polarity < 0:
        return "Negetive 😡"
    else:
        return "Null 😐"
#extract news titles
 #find suitable tag contains News Titles
#articles = soup.find_all("h2")
articles = soup.find_all("a")
news_list = []
for article in articles:
    text = article.text.strip()
    if text:
        news_list.append(text)

#show first 5 top titles
# print(news_list[:5])
print("")

for news in news_list[:5]:
    print(f"📰 {news} --> Sentiment: {analyze_sentiment(news)}")

