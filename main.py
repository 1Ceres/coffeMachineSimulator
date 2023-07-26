from data import MENU, resources


# TODO 3. Check recipies vs resources if coffe can be made
def check_resources(choice):
    """
    :param choice: string, coffee chosen by user
    :return: Cost of coffee if resources are enough to make a coffe, information
     about not enough resources otherwise
    """
    for ingredient in MENU[choice]['ingredients']:
        if resources[ingredient] >= MENU[choice]['ingredients'][ingredient]:
            pass
        else:
            return f"Sorry, there is not enough {ingredient}."
    return float(MENU[choice]['cost'])


# TODO 4. Check if money is correct, reject if not, or give a change (if you have,
# TODO 4. cd. otherwise inform, that no change can be given) and produce a coffe
def calculate_change(quarter, dime, nickel, penny, cost, choice):
    """
    :param quarter: int amount of quarters provided
    :param dime: int amount of dimes provided
    :param nickel: int amount of nickels provided
    :param penny: int amount of pennies provided
    :param cost: float a cost of ordered coffee
    :param choice: str a choice off coffe

    :return: string with information of change provided if founds are enough,
    else: information that it's not enough money
    """
    def update_money(quarter, dime, nickel, penny, cost):
        """
        :param quarter: int amount of quarters provided
        :param dime: int amount of dimes provided
        :param nickel: int amount of nickels provided
        :param penny: int amount of pennies provided
        :param cost: float a cost of ordered coffee
        update resources with money

        :return None
        """
        paid = 0.00
        if quarter * 0.25 == cost:
            resources['quarter'] += quarter
        elif quarter * 0.25 > cost:
            resources['quarter'] += cost/0.25
        else:
            resources['quarter'] += quarter
            paid = quarter * 0.25
            if dime * 0.1 == cost - paid:
                resources['dime'] += dime
            elif dime * 0.1 > cost - paid:
                resources['dime'] += round((cost - paid) / 0.1)
                paid += (round((cost - paid) / 0.1)) * 0.1
                if cost - paid == 0:
                    pass
                else:
                    if nickel * 0.05 == cost - paid:
                        resources['nickel'] += nickel
                    elif nickel * 0.05 > cost - paid:
                        resources['nickel'] += round((cost - paid) / 0.05)
                    else:
                        resources['nickel'] += nickel
                        paid += nickel * 0.05
                        if penny * 0.01 == cost - paid:
                            resources['penny'] += penny
                        elif penny * 0.01 > cost - paid:
                            resources['penny'] += round((cost - paid) / 0.01)
            else:
                resources['dime'] += dime
                paid += dime * 0.1
                if nickel * 0.05 == cost - paid:
                    resources['nickel'] += nickel
                elif nickel * 0.05 > cost - paid:
                    resources['nickel'] += round((cost - paid)/0.05)
                else:
                    resources['nickel'] += nickel
                    paid += nickel * 0.05
                    if penny * 0.01 == cost - paid:
                        resources['penny'] += penny
                    elif penny * 0.01 > cost - paid:
                        resources['penny'] += round((cost - paid)/0.01)

    money_paid = 0.25*quarter+0.10*dime+0.05*nickel+0.01*penny
    if money_paid > cost:
        update_money(quarter, dime, nickel, penny, cost)
        return f"Here is ${format((money_paid-cost), '.2f')} change. \n" + give_coffe(choice)
    elif money_paid == cost:
        update_money(quarter, dime, nickel, penny, cost)
        return "There is no change. \n" + give_coffe(choice)
    else:
        return "Sorry that's not enough money. Money refunded."


def give_coffe(choice):
    """
    :param choice: str a choice of coffe
    function update a resources
    :return: str a print of coffee provided
    """
    for ingredient in MENU[choice]['ingredients']:
        resources[ingredient] -= MENU[choice]['ingredients'][ingredient]
    return f"Here is your {choice} ☕️. Enjoy!"


# TODO 5. repeat
while True:
    # TODO 2. Ask for coffe
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    money_in_machine = 0.25*resources['quarter']+0.10*resources['dime']+0.05*resources['nickel']+0.01*resources['penny']
    if choice == "off":
        break
    elif choice == "report":
        # TODO 1. Print report
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Quarters: {resources['quarter']}, dimes: {resources['dime']},"
              f" nickels: {resources['nickel']}, pennies: {resources['penny']}")
        print(f"\nMoney: ${money_in_machine:.2f}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        cost = check_resources(choice)
        # TODO 3a. Inform that resources not enough
        if type(cost) == str:
            print(cost)
        # TODO 3b. Ask for money
        else:
            print(f"Please insert coin. You should pay: ${format(cost, '.2f')} for your {choice}.")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickel = int(input("How many nickels?: "))
            penny = int(input("How many pennies?: "))
            print(calculate_change(quarter, dime, nickel, penny, cost, choice))
    else:
        print("Sorry, I didn't get that, could you choose again?")
