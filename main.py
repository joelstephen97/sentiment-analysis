import re
from flask import Flask, jsonify, request
import requests
from statistics import mean
from dotenv import load_dotenv
import os
from flask_caching import Cache


app = Flask(__name__)

load_dotenv()  # Load environment variables from .env file

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
CACHE_EXPIRATION_TIME = 7200  # Cache expiration time in seconds

newsAPIKey = os.getenv('NEWS_API_KEY')
sentimentAPIKey = os.getenv('SENTIMENT_API_KEY')

sentimentAPIUrl = 'https://apis.paralleldots.com/v4/sentiment'  # get key from https://dashboard.komprehend.io/login




@app.route('/')
@cache.cached(timeout=CACHE_EXPIRATION_TIME, query_string=True)
def sentiment_analysis():
    country = request.args.get('country')
    category = request.args.get('category')

    if not country and not category:
        newsAPIUrl = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsAPIKey}"  # general api url if no args
    elif country and not category:
        newsAPIUrl = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsAPIKey}"  # general api url if only country
    elif country and category:
        newsAPIUrl = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={newsAPIKey}"  # general api url if both country and category

    try:
        news_response = requests.get(newsAPIUrl).json()
        articles = news_response.get('articles', [])

        if len(articles) == 0:
            return jsonify(message='No articles found for today.')

        sentiments = []
        for article in articles:
            text = f"{article['title']}. {article['description']}"
            clean_text = re.sub(r'\W+', ' ', text)  # Removes special characters as news articles sometimes might include some unwanted characters with no bearing

            sentiment_response = requests.post(sentimentAPIUrl, data={
                'text': clean_text,
                'api_key': sentimentAPIKey
            }).json()

            sentiment_scores = sentiment_response.get('sentiment')

            # Check if sentiment_scores is a dictionary and contains 'neutral', 'positive', 'negative' keys
            if isinstance(sentiment_scores, dict) and 'neutral' in sentiment_scores and 'positive' in sentiment_scores and 'negative' in sentiment_scores:
                sentiment_value = sentiment_scores['positive'] - sentiment_scores['negative']
                sentiment_value = min(sentiment_value * 10, 10) if sentiment_value > 0 else max(sentiment_value * 10, -10)
                sentiments.append(sentiment_value)

        if len(sentiments) == 0:
            return jsonify(message='Sentiment analysis failed for all articles.')

        average_sentiment = mean(sentiments)  # mean of all sentiments

        return jsonify(average_sentiment=average_sentiment)

    except Exception as e:
        print(f'Error during sentiment analysis: {e}')
        return jsonify(error='Error performing sentiment analysis'), 500


if __name__ == '__main__':
    app.run(port=3000)
