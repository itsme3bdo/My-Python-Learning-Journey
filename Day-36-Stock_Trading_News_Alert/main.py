import os
import requests
import datetime
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- API Keys and Credentials from .env ---
# Twilio credentials
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_from_number = os.environ.get("TWILIO_FROM_NUMBER")
twilio_to_number = os.environ.get("TWILIO_TO_NUMBER")

# Alpha Vantage and NewsAPI keys
alpha_vantage_api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

# --- Stock and Date Configuration ---
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# The Alpha Vantage API call below is hardcoded for IBM. Let's fix that.
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=EX02D0Z71079TYV8'

# Determine dates for the stock price check
today = datetime.date.today()
if today.weekday() == 5:  # Saturday
    today = today - datetime.timedelta(days=1)
elif today.weekday() == 6:  # Sunday
    today = today - datetime.timedelta(days=2) # Corrected logic to go back to Friday
# The original logic for Tuesday was off. We can simplify this.
yesterday = today - datetime.timedelta(days=1)
before_yesterday = today - datetime.timedelta(days=2)

# Handle weekend dates for data, as markets are closed
# This logic is simpler and more robust.
if yesterday.weekday() == 5: # If yesterday was a Saturday, get Friday's data.
    yesterday = yesterday - datetime.timedelta(days=1)
    before_yesterday = before_yesterday - datetime.timedelta(days=1)
elif yesterday.weekday() == 6: # If yesterday was a Sunday, get Friday's data.
    yesterday = yesterday - datetime.timedelta(days=2)
    before_yesterday = before_yesterday - datetime.timedelta(days=2)

# --- STEP 1: Get Stock Price Data ---
# Use https://www.alphavantage.co to get daily stock data.
alphavantage_url = 'https://www.alphavantage.co/query'
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vantage_api_key,
}

try:
    response = requests.get(alphavantage_url, params=params)
    response.raise_for_status()  # Raise an exception for bad status codes
    data = response.json()

    # The API returns dates in a specific format, so we use string keys to access.
    # The keys for yesterday and before_yesterday must be strings in "YYYY-MM-DD" format.
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    before_yesterday_str = before_yesterday.strftime('%Y-%m-%d')

    yesterday_close_price = float(data["Time Series (Daily)"][yesterday_str]["4. close"])
    before_yesterday_close_price = float(data["Time Series (Daily)"][before_yesterday_str]["4. close"])

    # Calculate the percentage change.
    fiveper = (yesterday_close_price - before_yesterday_close_price) / before_yesterday_close_price * 100

    print(f"Percentage change for {STOCK}: {fiveper:.2f}%")

except requests.exceptions.RequestException as e:
    print(f"Error fetching Alpha Vantage data: {e}")
    exit()
except KeyError as e:
    print(f"Error parsing Alpha Vantage data. Date key missing: {e}")
    print("API Response:", data)
    exit()

# --- STEP 2: Get News if there's a significant price change ---
# The original code had 'if True:'. Now we check the actual condition.
if abs(fiveper) > 5:
    # Use https://newsapi.org to get relevant news articles.
    news_url = 'https://newsapi.org/v2/everything'
    news_params = {
        'qInTitle': COMPANY_NAME,
        'sortBy': 'popularity',
        'pageSize': 3,
        'language': 'en',
        'apiKey': news_api_key
    }

    try:
        response_news = requests.get(news_url, params=news_params)
        response_news.raise_for_status()
        newz = response_news.json()

        # Iterate through the top 3 articles to send a message for each
        for article in newz.get("articles", []):
            title = article.get("title", "No Title")
            brief = article.get("description", "No Brief")
            
            # Determine if the change was an increase or decrease
            up_down = "🔺" if fiveper > 0 else "🔻"

            # --- STEP 3: Send SMS with Twilio ---
            client = Client(account_sid, auth_token)
            message_body = f"{STOCK}: {up_down}{abs(fiveper):.2f}%\n\nHeadline: {title}\nBrief: {brief}"

            message = client.messages.create(
                body=message_body,
                from_=twilio_from_number,
                to=twilio_to_number,
            )
            print(f"SMS sent successfully. SID: {message.sid}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching News API data: {e}")
        exit()
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")

