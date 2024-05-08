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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,  # Adding the money tracking wallet to resources
}

def check_requirements(order_item):
    item_ingredients = MENU[order_item]['ingredients']
    for ingredient, quantity in item_ingredients.items():
        if resources[ingredient] < quantity:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True

def calculate_price(quarters, dimes, nickles, pennies):
    price_quarters = 0.25
    price_dimes = 0.1
    price_nickles = 0.05
    price_pennies = 0.01
    total = quarters * price_quarters + dimes * price_dimes + nickles * price_nickles + pennies * price_pennies
    return round(total, 2)

def report():
    for item, quantity in resources.items():
        if item != "money":
            print(f"{item.capitalize()}: {quantity}g")
        else:
            print(f"Money: ${quantity}")

def off():
    exit()

def transaction_and_coffee_making(order_item, total_price):
    if total_price < MENU[order_item]['cost']:
        print('Sorry, that\'s not enough money. Money refunded.')
        return
    change = round(total_price - MENU[order_item]['cost'], 2)
    resources["money"] += MENU[order_item]['cost']
    print(f"Here's your {order_item} ☕️. Enjoy! Your change is ${change}.")

    # Deducting ingredients
    for ingredient, quantity in MENU[order_item]['ingredients'].items():
        resources[ingredient] -= quantity

def coffee_making_process():
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "report":
            report()
        elif order == "off":
            off()
        elif order in MENU:
            if check_requirements(order):
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                total_price = calculate_price(quarters, dimes, nickels, pennies)
                transaction_and_coffee_making(order, total_price)
        else:
            print("Invalid input. Please try again.")

coffee_making_process()
