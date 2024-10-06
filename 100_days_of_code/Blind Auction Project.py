bidders = {}

cont = True
while cont:
    
    name = input("What is your name?: ")
    bid = int(input("What's your bid? "))
    others = input("Are there any other bidders? ").lower()
    print("\n" * 5)
    bidders[name] = bid


    if others == 'no':
        cont = False
        for item in bidders:
            print(f"Name: {item}")
            print(f"Bid: {bidders[item]}")
            
        highest = max(bidders.values())  # Correct usage of max()
        print(f"The highest bid is: {highest}")
