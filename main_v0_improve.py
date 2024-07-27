from data import MENU, resources

menu = MENU.keys()
menu_list = list(menu)

def report():
    """Prints a report of all resources."""
    for ingredient, amount in resources.items():
        if ingredient == "coffee":
            print(f"{ingredient.capitalize()}: {amount}g")
        elif ingredient == "money":
            print(f"{ingredient.capitalize()}: ${amount}")
        else:
            print(f"{ingredient.capitalize()}: {amount}ml")

def check_resource(drink_ingredients):
    """Checks if there are enough resources for the drink."""
    for ingredient, drink_amount in drink_ingredients.items():
        total_amount = resources.get(ingredient, 0)
        if drink_amount > total_amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coin(drink_cost):
    """Processes user coin input and checks if it is sufficient."""
    coin_cost = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    user_money = 0
    print("Please insert coins.")
    for coin, value in coin_cost.items():
        try:
            user_coins = int(input(f"How many {coin}?: "))
            user_money += value * user_coins
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            return False
        
    if user_money >= drink_cost:
        change = user_money - drink_cost
        if change > 0:
            print(f"here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

def deduct_resource(drink_ingredients):
    """Deduct the required resources for the drink."""
    for ingredient, amount in drink_ingredients.items():
        resources[ingredient] -= amount

def coffee_machine():
    """Main function to run the coffee machine."""
    shut_down = False
    while not shut_down:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "off":
            print("The machine is shutting down...")
            shut_down = True
        elif user_input == "report":
            report()
        elif user_input in menu_list:
            drink = MENU[user_input]
            drink_ingredients = drink["ingredients"]
            drink_cost = drink["cost"]
            if check_resource(drink_ingredients):
                if process_coin(drink_cost):
                    print(f"here is your {user_input.capitalize()} ☕. Enjoy!")
                    deduct_resource(drink_ingredients)
                    resources["money"] += drink_cost
        else:
            print("Please enter only 'espresso', 'latte', or 'cappuccino'.")

if __name__ == "__main__":
    coffee_machine()
