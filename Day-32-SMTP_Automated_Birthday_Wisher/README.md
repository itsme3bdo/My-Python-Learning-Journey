Automated Birthday Wisher

This project is your personal assistant for remembering birthdays! The application automatically sends a happy birthday email to someone on their special day. All you have to do is set it up once, and it will handle the rest, making sure you never miss another important date.

How It Works 

This project is a showcase of how Python can connect to external services and automate a real-world task:

Working with SMTP: The core of this program uses Python's smtp module to connect to an email server. This is the protocol that allows the program to send emails, just like a regular email client.

Date and Time: The program uses the datetime module to check the current date and compare it to a list of birthdays. This is how it knows when to send the birthday wish.

Working with Files: The script reads the names and birthdays from a CSV file, so you can easily manage and update your list of contacts.

Randomness: To make each message a little more special, the program uses the random module to choose a unique birthday card or message from a selection of templates.
