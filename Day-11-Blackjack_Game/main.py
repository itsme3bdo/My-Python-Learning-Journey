import art
import random
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

want = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n")

def  calculate_score(cards):
    score=sum(cards)
    while score > 21 and 11 in cards:
        cards.remove(11)
        cards.appened(1)
        score = sum(cards)
    return score

while want == "y":
    user_cards= [random.choice(cards),random.choice(cards)]
    computer_cards= [random.choice(cards)]
    gameover = False

    while not gameover:
        score_user = calculate_score(user_cards)
        score_comp = calculate_score(computer_cards)

        print(f"Your cards: [{user_cards}], current score: {score_user}")
        print(f"Computer's first card: {computer_cards}")

        if score_user > 21:
            print("You went over you lose\n")
            gameover=True
            continue

        another = input("Type 'y' to get another card, type 'n' to pass:")
        if another == "y":
            user_cards.append(random.choice(cards))
        else:
            gameover=True

    while score_comp < 17 and gameover:
        computer_cards.append(random.choice(cards))
        score_comp=calculate_score(computer_cards)

    print(f"Your final hand: [{user_cards}], final score: {score_user}")
    print(f"Computer's final hand: [{computer_cards}], final score: {score_comp}")

    if score_user > 21:
        print("You went over you lose\n")
    elif score_comp > 21 or score_user > score_comp:
        print("You Win")
    elif score_comp > score_user:
        print("You Lose")
    else:
        print("You drew")

    want = input("Do  you want to play a game of Blackjack? Type 'y' or 'n'.\n")








