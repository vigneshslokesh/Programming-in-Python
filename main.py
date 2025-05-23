from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


order = Menu()
resource = CoffeeMaker()
money = MoneyMachine()

machine_on = True

while machine_on:
    ip = input(f"What would you like? {order.get_items()} : ")
    if ip == "report":
        resource.report()
        money.report()

    elif ip == "off":
        machine_on = False
    else:         
        drink_name = order.find_drink(ip)
        if drink_name:
            if resource.is_resource_sufficient(drink_name) and money.make_payment(drink_name.cost):
                resource.make_coffee(drink_name)
        else:
            print("Invalid selection")

    



