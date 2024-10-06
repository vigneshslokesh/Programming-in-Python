bidders = {}

cont = True
while cont:
    
    name = input("What is your name?: ")
    bid = int(input("What's your bid? Rs"))
    others = input("Are there any other bidders? ").lower()
    print("\n" * 5)
    bidders[name] = bid


    if others == 'no':
        cont = False
        for item in bidders:
            print(f"Name: {item}")
            print(f"Bid: {bidders[item]}")

        person = max(bidders, key=bidders.get)   
        highest = max(bidders.values())  # Correct usage of max()
        print(f"The highest bid was from {person} with: Rs{highest}")
