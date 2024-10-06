

cont = True

bidders = {}

def highest_bid(bidder_dict):
    winner = ''
    highest = 0
    for bid in bidder_dict:
        bid_amount = bidder_dict[bid]
        if bid_amount > highest:
            highest = bid_amount
            winner = bid
    
    print(f"The Winner is {winner} with a bid of Rs {highest}.")


while cont:
    name = input("What's your name: ")
    bid = int(input("What's your bid: Rs"))
    others = input("Are there other person? (Type 'yes' to continue else type 'no' to exit): ").lower()
    bidders[name] = bid

    if others == "no":
        cont = False
        highest_bid(bidders)
        

    elif others == "yes":
        print("\n" * 20)
