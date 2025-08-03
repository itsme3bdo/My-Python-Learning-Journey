from art import logo
print(logo)

def find_highest(bidding):
    winner=""
    nooom=0
    for key in bidding:
        amount=bidding[key]
        if amount > nooom:
            nooom = amount
            winner=key
    print(f"The winner is {winner} with {nooom}$")
data={}
still=True
while still:

# TODO-1: Ask the user for input
    name=input("Enter your name\n")
    bid=int(input("Enter your bid\n"))
# TODO-2: Save data into dictionary {name: price}
    data[name]=bid
# TODO-3: Whether if new bids need to be added
    still=input("Is there someone else? Type yes or no").lower()
    if still == "no":
        still = False
        find_highest(data)
    elif still=="yes":
        print("\n"*100)
# TODO-4: Compare bids in dictionary



