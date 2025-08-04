Mail Merge Project
A Program to Generate Personalized Letters

This is a project that shows you how to automate a very common task: generating multiple, personalized documents from a single template. With this program, you can create a unique letter for every person on a list, saving you a ton of time and effort.

How It Works 
This project is a showcase of how a few fundamental Python concepts work together to handle files and text:

File Handling (open()): The program uses Python's built-in file handling capabilities to read a list of names from one file and a template letter from another. It then writes each new, personalized letter to its own file.

String Manipulation: It finds a special placeholder in the template letter (like [name]) and then replaces it with each name from your list, one by one.

Loops: A for loop is the engine of the project. It goes through every name on the list, generates a new letter for that person, and saves it.
