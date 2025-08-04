Stock Trading News Alert

This is a powerful and practical application that keeps an eye on the stock market for you. It automatically checks the price of a stock every day, and if there's a significant change (a 5% increase or decrease), it sends you a text message with the top three news articles about that company. This is a great way to stay informed about your investments without constantly checking the market.

How It Works 

This project is a showcase of how Python can connect to external services and automate a real world task:

APIs: The program uses two different public APIs: one from Alpha Vantage to get live stock price data and one from NewsAPI to get recent news articles about a company.

Working with Environment Variables: It uses environment variables to securely store sensitive information like API keys and phone numbers. This is a crucial practice for keeping your credentials safe and out of your code.

Twilio: The program uses the Twilio API to send an SMS text message to your phone. It's a great example of how to use a third-party service to add powerful functionality to your applications.

Conditional Logic: The script checks if the stock price has changed by more than 5%. If it has, it makes a second API call to get news articles and then sends you an alert.
