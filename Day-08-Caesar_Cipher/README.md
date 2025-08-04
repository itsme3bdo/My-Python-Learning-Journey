Caesar Cipher

This is a fun and simple program that lets you encrypt or decrypt secret messages using the classic Caesar cipher. It's a great tool for understanding basic cryptography and for sending messages to your friends that are just a little bit harder to read. The best part is, you can keep running it over and over again until you're done with all your secret messages!

How It Works

This project is a fantastic showcase of a few fundamental Python concepts that work together to create a practical application:

Functions: The core logic is all wrapped up in a function called caesar(), which takes the message, the shift number, and whether you want to encode or decode. This makes the code organized and easy to reuse.

Loops: We use a for loop to go through each letter of your message and apply the shift. There's also a while loop that keeps the program running, so you can keep encrypting and decrypting messages without having to restart the script every time.

Conditional Logic: The script uses if and else statements to handle things like whether you're encoding or decoding, and it's also smart enough to recognize and keep any numbers or symbols you put in your message.

Working with the Alphabet: It uses a list of the alphabet and the modulo operator (%) to make sure that when you shift a letter, it wraps back around to the beginning of the alphabet instead of running off the end.
