from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# 4. Check resources sufficient? --> if not --> “Sorry there is not enough water.”
def sufficientResources(ingredients):
    notSufficientResources = []
    for key in ingredients:
        if (resources[key] < ingredients[key]):
            notSufficientResources.append(key)
    return notSufficientResources

# Reduce resources


def reduceResources(ingredients):
    for key in ingredients:
        resources[key] -= ingredients[key]


# 5. Process coins
def processCoins():
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


isMachineRunning = True
while isMachineRunning:

    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if prompt == "off":
        isMachineRunning = False

    # 3. When the user enters “report” to the prompt,
    elif prompt == "report":
        print(f"Water : {resources['water']}ml\nMilk : {resources['milk']}ml\nCoffee : {
              resources['coffee']}g\nMoney : ${resources['money']}")

    # coffee type
    else:
        isNotSufficient = sufficientResources(MENU[prompt]["ingredients"])
        if len(isNotSufficient) != 0:
            print(f'Sorry there is not enough {', '.join(isNotSufficient)}')
        else:
            # 5. Process coins
            total = processCoins()

            # 6. Check transaction successful? --> if not --> “Sorry that's not enough money. Money refunded.” --> more money will refunded.
            if total < MENU[prompt]["cost"]:
                print("Sorry that's not enough money. Money refunded.")

            # 7. Make Coffee
            else:
                reduceResources(MENU[prompt]["ingredients"])
                resources["money"] += MENU[prompt]["cost"]
                if total > MENU[prompt]["cost"]:
                    print(f"Here is ${
                          round(total - MENU[prompt]["cost"], 2)} is change.")
                print(f"“Here is your {prompt}☕☕. Enjoy!")
