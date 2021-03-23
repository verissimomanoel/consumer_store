# ----------------------------------------------------------------------------------------------------------------------
#   This software is free software.
# ----------------------------------------------------------------------------------------------------------------------
from app.main.model.item import Item
from app.main.checkout.checkout import Checkout
from app.main.rule.sony_rule import SonyRule
from app.main.rule.central_ac_rule import CentralACRule
from app.main.rule.nike_rule import NikeRule
import sys
import logging

CURRENCY_FORMAT = '$ {:.2f}'
LOG_FORMAT = '%(asctime)-15s :: %(message)s'

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def tests():
    """
    Execute some simple tests to verify the rules.
    :return:
    """
    # Scenario 1
    test_scenario1()

    # Scenario 2
    test_scenario2()

    # Scenario 3
    test_scenario3()

    # Scenario 4
    test_scenario4()

    # Scenario 5
    test_scenario5()

    # Scenario 6
    test_scenario6()

    # Scenario 7
    test_scenario7()

def test_scenario7():
    checkout = Checkout(rules)
    checkout.scam(nike_shoe)
    checkout.scam(sony_tv)
    checkout.scam(charger)
    total = checkout.total()
    assert round(total, 2) == 689.49
    logging.info('Pass Test 7 *** Total: ' + CURRENCY_FORMAT.format(total))

def test_scenario6():
    checkout = Checkout(rules)
    checkout.scam(nike_shoe)
    checkout.scam(nike_shoe)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(central_ac)
    checkout.scam(charger)
    checkout.scam(charger)
    total = checkout.total()
    assert round(total, 2) == 2778.97
    logging.info('Pass Test 6 *** Total: ' + CURRENCY_FORMAT.format(total))


def test_scenario5():
    checkout = Checkout(rules)
    checkout.scam(nike_shoe)
    checkout.scam(nike_shoe)
    checkout.scam(nike_shoe)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(central_ac)
    checkout.scam(charger)
    total = checkout.total()
    assert round(total, 2) == 3848.95
    logging.info('Pass Test 5 *** Total: ' + CURRENCY_FORMAT.format(total))

def test_scenario4():
    checkout = Checkout(rules)
    checkout.scam(nike_shoe)
    checkout.scam(nike_shoe)
    checkout.scam(nike_shoe)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(central_ac)
    checkout.scam(charger)
    total = checkout.total()
    assert round(total, 2) == 4148.94
    logging.info('Pass Test 4 *** Total: ' + CURRENCY_FORMAT.format(total))


def test_scenario3():
    checkout = Checkout(rules)
    checkout.scam(central_ac)
    checkout.scam(sony_tv)
    total = checkout.total()
    assert round(total, 2) == 1949.98
    logging.info('Pass Test 3 *** Total: ' + CURRENCY_FORMAT.format(total))


def test_scenario2():
    checkout = Checkout(rules)
    checkout.scam(nike_shoe)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(nike_shoe)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    checkout.scam(sony_tv)
    total = checkout.total()
    assert round(total, 2) == 2718.95
    logging.info('Pass Test 2 *** Total: ' + CURRENCY_FORMAT.format(total))


def test_scenario1():
    checkout = Checkout(rules)
    checkout.scam(nike_shoe)
    checkout.scam(nike_shoe)
    checkout.scam(nike_shoe)
    checkout.scam(charger)
    total = checkout.total()
    assert round(total, 2) == 249.00
    logging.info('Pass Test 1 *** Total: ' + CURRENCY_FORMAT.format(total))


def input_main():
    """
    Main execution to provide options to users to scam items and checkout.
    :return:
    """
    tests()

    checkout = Checkout(rules)
    while True:
        choice = input("Please choose one option of item id to scam (1 - Sony TV, 2 - Central AC, 3 - Nike Shoe or "
                       "4 - Charger) or 0 zero to exit:\n")
        if choice == '0':
            exit_program(checkout)
        else:
            if choice.isnumeric():
                item = accepted_items.get(int(choice))
                if item is not None:
                    checkout.scam(item)
                    print('Total:', CURRENCY_FORMAT.format(checkout.total()), "\n")
                else:
                    print("Wrong choice, try again...", "\n")
            else:
                print("Wrong choice, please type a number...", "\n")


def exit_program(checkout):
    """
    Ends the program, and if have items scanned, show the checkout.
    :param checkout:
    :return:
    """
    if checkout.products is not None and len(checkout.products) > 0:
        print('\n\n********************* Checkout **********************\n')
        print("ITEM_IDs Scanned:", checkout.get_itens_keys())
        print("Total:", checkout.total(), "\n")
        print('********************* Checkout **********************\n')

    print("Quitting...")
    sys.exit()


def prepare_accepted_items():
    """
    Prepare a list with the accepted items to scam.
    :return:
    """
    global sony_tv, central_ac, nike_shoe, charger, accepted_items
    sony_tv = Item("stv", "Sony TV", 549.99)
    central_ac = Item("cac", "Central AC", 1399.99)
    nike_shoe = Item("nsh", "Nike Shoe", 109.50)
    charger = Item("mch", "Charger", 30)

    accepted_items = {
        1: sony_tv,
        2: central_ac,
        3: nike_shoe,
        4: charger,
    }


def prepare_rules():
    """
    Prepare the rules to calculate the discounts.
    :return:
    """
    global rules
    sony_rule = SonyRule('Sony Rule')
    central_ac_rule = CentralACRule('Central AC Rule')
    nike_rule = NikeRule('Nike Rule')
    # Dict with all rules by item type.
    rules = {
        sony_tv.id: [sony_rule],
        central_ac.id: [central_ac_rule],
        nike_shoe.id: [nike_rule]
    }


if __name__ == '__main__':
    prepare_accepted_items()
    prepare_rules()
    input_main()
