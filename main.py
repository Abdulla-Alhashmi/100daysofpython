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
}
profit = 0

def process_coins(choice):
    """If paid money is insufficient, returns False. Otherwise, returns True"""

    print("Please Insert Coins.")

    global MENU

    global profit

    cost = MENU[choice]['cost']

    total = int(input("How many quarters? ")) * 0.25

    total += int(input("How many dimes? ")) * 0.2

    total += int(input("How many nickles")) * 0.1

    total += int(input("How many pennies? ")) * 0.05

    change = total - cost


    if total >= cost:

        print(f"enjoy your coffee, your change is {change}")

        profit += cost

        return True

    else:

        print('Sorry, not enough coins.your money will be refunded.')

        return False


def is_resources_sufficient(ingredients, current_resources):
    """ If resources are enough, returns True. If not, returns False"""
    global resources

    for item in ingredients:

        if ingredients[item] > current_resources[item]:

            print(f"sorry not enough {item}")

            return False

        else:

            resources[item] -= ingredients[item]

            return True

is_on = True

while is_on:

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == 'off':

        is_on = False

    elif user_input == 'report':

        print(resources, ' ', profit)

    else:
        is_resources_sufficient(MENU[user_input]['ingredients'], resources)
        process_coins(user_input)






