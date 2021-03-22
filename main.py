# ----------------------------------------------------------------------------------------------------------------------
#   This software is free software.
# ----------------------------------------------------------------------------------------------------------------------
from app.main.model.item import Item
from app.main.checkout.checkout import Checkout
from app.main.rule.sony_rule import SonyRule
from app.main.rule.central_ac_rule import CentralACRule
from app.main.rule.nike_rule import NikeRule
import sys

FORMAT = '{:7,.2f}'

def tests():
    # Scenario 1
    checkout = Checkout(rules)
    checkout.scam(nike_shoe)
    checkout.scam(nike_shoe)
    checkout.scam(nike_shoe)
    checkout.scam(charger)
    total = checkout.total()
    assert total == 249.00
    print('Pass Test 1 *** Total:', FORMAT.format(total))

    # Scenario 2
    checkout = Checkout(rules)
    checkout.scam(nike_shoe)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(nike_shoe)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    total = checkout.total()
    assert total == 2718.95
    print('Pass Test 2 *** Total:', FORMAT.format(total))

    # Scenario 3
    checkout = Checkout(rules)
    checkout.scam(central_ac)
    checkout.scam(sony_tv)
    total = checkout.total()
    assert total == 1949.98
    print('Pass Test 3 *** Total:', FORMAT.format(total))


def input_main():
    checkout = Checkout(rules)
    while True:
        choice = input("Please choose one option of item id to scam (1 - Sony TV, 2 - Central AC, 3 - Nike Shoe or "
                       "4 - Charger) or 0 zero to exit:\n")
        if choice == '0':
            print("Quitting")
            sys.exit()
        else:
            if choice.isnumeric():
                item = accepted_item.get(int(choice))
                if item is not None:
                    checkout.scam(item)
                    print('Total:', FORMAT.format(checkout.total()))
                else:
                    print("Wrong choice, try again...")
            else:
                print("Wrong choice, please type a number...")


if __name__ == '__main__':
    sony_tv = Item("stv", "Sony TV", 549.99)
    central_ac = Item("cac", "Central AC", 1399.99)
    nike_shoe = Item("nsh", "Nike Shoe", 109.50)
    charger = Item("mch", "Charger", 30)

    accepted_item = {
        1: sony_tv,
        2: central_ac,
        3: nike_shoe,
        4: charger,
    }

    sony_rule = SonyRule('Sony Rule')
    central_ac_rule = CentralACRule('Central AC Rule')
    nike_rule = NikeRule('Nike Rule')

    # Dict with all rules by item type.
    rules = {
        sony_tv.id: [sony_rule],
        central_ac.id: [central_ac_rule],
        nike_shoe.id: [nike_rule]
    }

    tests()
    input_main()
