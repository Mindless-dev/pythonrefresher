import os
from art import logo

# secret auction program
# os.system('cls||clear')

print(logo)


bidders = {}


def auction(bidder_name, bid_amount):
    bidders[bidder_name] = bid_amount


auction_running = True
highest_bid = 0

while auction_running:
    name = input("What's your name ?: ")
    bid = int(input("What would you like to bid $: "))
    more_bidders = input("Are there any other bidders? 'yes' or 'no' ").lower()
    auction(name, bid)

    if more_bidders == "no":
        auction_running = False
        for person in bidders:
            if bidders[person] > highest_bid:
                highest_bid = bidders[person]
        print(f"The winner is {person} with a bid of {bidders[person]}$")

    else:
        os.system('cls||clear')


# adding highest bid to dictionary
# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")
