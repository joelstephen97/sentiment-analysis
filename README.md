# Sentiment Analysis API

This repository contains code for a Flask-based Sentiment Analysis API. 
The API fetches news articles using the [News API](https://newsapi.org/) and performs sentiment analysis on the article titles and descriptions using the [ParallelDots Sentiment Analysis API](https://apis.paralleldots.com/v4/sentiment).
Then the sentiment is calculated from 10 to -10, 10 being fully positive or -10 being fully negative.
The aim is to get a sentiment based on the top news articles of the day, ideally giving an idea about market conditions and other variables remotely or directly depending on the larger news cycle.
This is a part of my large project to improve my coding and also build on some financial knowledge.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.x installed on your system.
- Access to the News API and ParallelDots Sentiment Analysis API. Sign up and obtain the necessary API keys from their respective websites.

## Installation

1. Clone this repository to your local machine.

   ```shell
   git clone https://github.com/joelstephen97/sentiment-analysis.git
   ```

2. Navigate to the project directory.
   ```shell
   cd sentiment-analysis
   ```

3. Install the required dependencies.

    ```shell
    pip install -r requirements.txt
    ```

4. Create a .env file in the project root directory and add your API keys.

    ```shell
    touch .env
    ```

5. Open the .env file in a text editor and add the following lines and replace your_news_api_key and your_sentiment_api_key with your actual API keys.

    ```makefile

    NEWS_API_KEY=your_news_api_key
    SENTIMENT_API_KEY=your_sentiment_api_key
    ```

## Usage

To start the Flask server and use the Sentiment Analysis API, follow these steps:

Run the following command:
   ```shell
   python app.py
   ```

The Flask server will start running on http://localhost:3000/.

Use an API testing tool like Postman or send HTTP requests to the server to perform sentiment analysis on news articles. 
The API supports the following parameters:
    
country (optional): The 2-letter ISO 3166-1 code of the country you want to get headlines for. Possible options: ae ar at au be bg br ca ch cn  co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za 
If not specified, defaults to us.

category (optional): News category Possible options: business entertainment general health science sports technology.

Example usage:

http://localhost:3000/?country=us - Perform sentiment analysis on top headlines from the United States.

http://localhost:3000/?country=gb&category=business - Perform sentiment analysis on top business news from the United Kingdom.

The API will return the average sentiment score for the retrieved articles.

## License

This project is licensed under the Creative Commons Zero v1.0 Universal license.
Please discuss with me before this code is used commercially or for business purposes.

Note: Remember to keep your API keys confidential and do not share them publicly.

## Author(s)
Joel Stephen

## Image Credits
<a href="https://www.freepik.com/free-vector/emoji-satisfaction-meter-small_44156211.htm#query=sentiment%20analysis&position=0&from_view=keyword&track=ais">Image by juicy_fish</a> on Freepik
