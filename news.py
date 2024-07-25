import requests

def get_news(api_key, country='us', category='technology'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles')
        if not articles:
            return "Sorry, I couldn't find any news articles at the moment."
        
        news_summary = "Here are the top 3 news headlines:\n"
        for i, article in enumerate(articles[:3], start=1):  # Limit to the top 3 news articles
            title = article.get('title')
            news_summary += f"{i}. {title}\n"
        return news_summary
    else:
        return "Sorry, I couldn't fetch the news at the moment."