ISS Overhead Notifier
Get Notified When the ISS Is Above You!

This is a fun and practical application that uses live data to let you know when the International Space Station (ISS) is passing overhead. The program will check your current location and, if the ISS is in the sky and it's dark outside, it will send you a notification. This is a great way to use APIs to interact with real-world data and create a neat little app.

How It Works

This project is a showcase of how Python can use APIs (Application Programming Interfaces) to get live data from the web:

API Endpoints: The program makes a request to a public API, a web address that gives you live data about the ISS's current location and sunrise/sunset times for your location.

API Parameters: It uses API parameters to send your latitude and longitude to the API, so it knows what data to give you.

Making a Request: The program uses the requests module to fetch the data from the API.

Conditional Logic: It checks if your location is close to the ISS's current location and if it's dark outside before it sends you a notification.
