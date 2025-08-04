Turtle Race Game

This is an interactive game where you can bet on which turtle you think will win the race. A group of colorful turtles will sprint across your screen, and you'll find out if your guess was right or wrong.

How It Works

Creating Multiple Turtles: Instead of just one turtle, this game creates multiple Turtle objects, each with its own color. This is done efficiently using a for loop to create each turtle and position them at the starting line.

User Input: Before the race begins, the program uses screen.textinput() to get your bet. It then uses this input to determine if you won or lost at the end of the race.

Random Movement: The heart of the race is the random module, which is used to move each turtle forward by a random amount in a while loop. This ensures that the race is unpredictable and different every time you play.

The Finish Line: The game keeps a close eye on each turtle's position. Once a turtle crosses the finish line, the loop stops, and the winner is announced!

