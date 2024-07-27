from data import MENU, resources

menu = MENU.keys()
menu_list = list(menu)

def report():
    for ingredient in resources:
        amount = resources[ingredient]
        if ingredient == "coffee":
            print(f"{ingredient.capitalize()}: {amount}g")
        elif ingredient == "money":
            print(f"{ingredient.capitalize()}: ${amount}")
        else:
            print(f"{ingredient.capitalize()}: {amount}ml")

def check_resource(drink_ingredients):
    do_coffee = 0
    for ingredient in drink_ingredients:
        total_amount = resources[ingredient]
        drink_amount = drink_ingredients[ingredient]
        
        if drink_amount <= total_amount:
            do_coffee += 1
        else:
            print(f" Sorry there is not enough {ingredient}.")
            return False
    if do_coffee in (2,3):
        return True

def process_coin(drink_cost, user_coins):
    coin_cost = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickles": 0.05,
        "pennies": 0.01
    }
    user_money = 0
    for coin in user_coins:
        user_money += coin_cost[coin] * user_coins[coin]

    change = user_money - drink_cost
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def deduct_resource(drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]

shut_down = False
while not shut_down:
    user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()
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
            coins = {
                "quarters": 0,
                "dimes": 0,
                "nickles": 0,
                "pennies": 0
            }
            user_coins = {}
            print("Please insert coins.")
            for coin in coins:
                user_coin = int(input(f"how many {coin}?: "))
                user_coins[coin] = user_coin
            if process_coin(drink_cost, user_coins):
                print(f"Here is your {user_input.capitalize()}☕. Enjoy!")
                deduct_resource(drink_ingredients)
                resources["money"] += drink_cost
    else:
        print("Please enter only 'espresso', 'latte' or 'cappuccino'.")