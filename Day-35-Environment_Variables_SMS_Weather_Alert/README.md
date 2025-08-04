Weather Alert


This is a practical application that sends you a text message alert if it's going to rain in your area. This is a great way to stay ahead of the weather and make sure you're always prepared. The program runs in the background and will let you know when to grab your umbrella.

How It Works

This project is a showcase of how Python can connect to external services and automate a real-world task:

Environment Variables: The program uses environment variables to securely store sensitive information like API keys and phone numbers. This is a crucial practice for keeping your credentials safe and out of your code.

APIs: The program makes a request to a public API, a web address that gives you live weather data for your current location.

Working with SMTP: The core of this program uses Python's smtp module to connect to an email server. This is the protocol that allows the program to send emails, just like a regular email client.

Twilio: The program uses the Twilio API to send an SMS text message to your phone. It's a great example of how to use a third-party service to add powerful functionality to your applications.

Conditional Logic: The script checks if the weather forecast includes rain. If it does, it sends you an alert.
