A Classic Quiz with a Modern Touch

This is a fun and interactive quiz game that runs right in your terminal. What makes it special is that it's built using a key programming concept called Object-Oriented Programming (OOP). The game will challenge you with a series of questions and keep track of your score, all while demonstrating a clean and organized approach to coding.

How It Works

This project is an excellent example of how to use OOP to structure an application. 
Here's what's happening in the code:

Classes and Objects: Instead of just using variables and functions, the program creates classes. For instance, there's likely a Question class that holds all the information for a single question, like the text and the answer. Each question in the quiz is an object (an instance) of this class.

Encapsulation: OOP allows us to bundle related data and functionality together. This means the Question object knows both its question text and its correct answer. This keeps the code tidy and makes it easy to add new questions later on without changing the core game logic.

The Game Loop: The project uses a while loop to keep the game going as long as there are questions left. It iterates through the list of question objects, presents each one, and then checks your answer.
