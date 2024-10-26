MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_sufficient(order_ingridients):
    '''Returns if sufficient resources are available'''
    for item in order_ingridients:
        if order_ingridients[item]>=resources[item]:
            print(f"Sorry there is no enough {item}.")
            return False
    return True

def process_coins():
    '''Returns total calculated from coins inserted'''
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    '''Return True when the payment is accepted, or return False if the money is insufficient'''
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded!")
        return False

def make_coffe(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")    

def report(resource):
    for i in resource:
        print(f'{i} : {resource[i]}ml')
    print(f"Money: $ {profit}")


machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report(resources)

    elif choice == "off":
        print("Machine turning off!")
        machine_on = False

    else:
        drink=MENU[choice]
        if is_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(choice, drink["ingredients"])
        