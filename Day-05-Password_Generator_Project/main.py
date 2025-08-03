import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password =  []
# randoo = 0
# x = 0
final=""
for letter in range(0,nr_letters):
    password.append(random.choice(letters))
#     if x < nr_letters:
#         x+=1
#         randoo = random.randrange(0,len(letters))
#         password.append(letters[randoo])
# x = 0
for symbol in range(0,nr_symbols):
#     if x < nr_symbols:
#         x+=1
#         randoo = random.randrange(0,len(symbols))
#         password.append(symbols[randoo])
# x = 0
    password.append(random.choice(symbols))
for number in range(0,nr_numbers):
    # if x < nr_numbers:
    #     x += 1
    #     randoo = random.randrange(0, len(numbers))
    #     password.append(numbers[randoo])
    password.append(random.choice(numbers))


random.shuffle(password)

for let in password:
    final = final + let

print(f"Your password is {final}")

