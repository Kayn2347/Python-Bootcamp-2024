from replit import clear
# Clear function can be used to cleae everything from console
from ascii_art import logo

def find_higest_amount(p_bid_record):
    highest_bid = 0
    highest_bidder = ""
    for key, value in p_bid_record.items():
        if value > highest_bid:
            highest_bid = value
            highest_bidder = key
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

print(logo)
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid amount?: $"))
    bids[name] = bid_amount
    should_continue = input("Are there any other bidder?(Y/N)")
    if should_continue == "N":
        bidding_finished = True
        find_higest_amount(bids)
    elif should_continue == "Y":
        clear()