import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]

compp = random.randint(0,2)
userr = int(input("What do you choose? Type 0 for Rock, 1 for Paper,2 for Scissors.\n"))
if userr == compp:
    print(f"{options[userr]}\n Computer chose: {options[compp]}\n You Drew!")
elif userr == 0 and compp ==  2:
    print(f"{options[userr]}\n Computer chose: {options[compp]}\nYou Win!")
elif userr == 0 and compp ==  1:
    print(f"{options[userr]}\n Computer chose: {options[compp]}\nYou Lose!")
elif userr == 1 and compp ==  0:
    print(f"{options[userr]}\n Computer chose: {options[compp]}\nYou Win!")
elif userr == 1 and compp ==2:
    print(f"{options[userr]}\n Computer chose: {options[compp]}\nYou Lose!")
elif userr == 2 and compp == 1:
    print(f"{options[userr]}\n Computer chose: {options[compp]}\nYou Win!")
elif userr == 2 and compp ==  0:
    print(f"{options[userr]}\n Computer chose: {options[compp]} \nYou Lose!")
else:
    print("You entered a wrong value")

