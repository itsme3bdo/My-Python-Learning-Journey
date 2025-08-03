from art import logo,vs
from game_data import data
import random

g1=data[random.randint(0,49)]
g2=data[random.randint(0,49)]
while g1['name']==g2['name']:
    g2=data[random.randint(0,49)]
print(logo)
gameover  = False
score=0

while not gameover and g1['name']!=g2['name']:
    print(f"Compare A: {g1['name']}, a {g1['description']}, from {g1['country']}")
    print(vs)
    print(f"Against B: {g2['name']}, a {g2['description']}, from {g2['country']}")
    print(g1['follower_count'], g2['follower_count'])
    ans=input("Who has more follower?  Type 'A' or 'B':").lower()
    if ans == "a":
        if g1['follower_count'] > g2['follower_count']:
            score+=1
            print(20*"\n")
            print(logo)
            print(f"You're right! Current score:{score}")
            g1=g2

        else:
            print(20 * "\n")
            print(logo)
            print(f"Sorry that's wrong. Final Score:{score}")
            gameover=True
    elif ans == "b":
        if g1['follower_count'] < g2['follower_count']:
            score+=1
            print(20*"\n")
            print(logo)
            print(f"You're right! Current score:{score}")
            g1=g2

        else:
            print(20 * "\n")
            print(logo)
            print(f"Sorry that's wrong. Final Score:{score}")
            gameover=True
    g2 = data[random.randint(0, 49)]

