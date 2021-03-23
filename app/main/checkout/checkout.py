# ----------------------------------------------------------------------------------------------------------------------
#   This software is free software.
# ----------------------------------------------------------------------------------------------------------------------
from ..model.item import Item


class Checkout:
    """
    Store the items of checkout in the store.
    """
    CENTRAL_AC_KEY = "cac"

    def __init__(self, pricing_rules: dict):
        """
        Class constructor.
        :param pricing_rules: The list with all rule to process in checkout.
        """
        self.pricing_rules = pricing_rules
        self.products = {}
        self.amount = 0
        self.discount = 0
        self.charger = Item("mch", "Charger", 30)

    def scam(self, item: Item):
        """
        Verify the item and apply the rule by item type.
        :param item: The item to be verified
        :return:
        """
        products = self.products.get(item.id)
        if products is None:
            self.products[item.id] = []

        self.products[item.id].append(item)
        self.amount += item.price
        self.verify_central_ac(item)

    def verify_central_ac(self, item):
        """
        Check if the added item is a central ac, add a charger in a list of products, and
        increment the amount with the charger value.
        :param item:
        :return:
        """
        if item.id == self.CENTRAL_AC_KEY:
            if self.charger.id not in self.products:
                self.products[self.charger.id] = []

            self.products[self.charger.id].append(self.charger)
            self.amount += self.charger.price

    def __apply_rules(self, item):
        """
        Apply all rules defined for each item.
        :param item: The item to be verified
        :return:
        """
        if self.pricing_rules is not None:
            rules_item = self.pricing_rules.get(item.id)
            if rules_item is not None:
                for rule in rules_item:
                    self.discount += rule.process(item, self.products)

    def total(self):
        """
        Calculates the total amount for the checkout applying the discounts.
        :return:
        """
        self.discount = 0
        for key in self.products.keys():
            self.__apply_rules(self.products.get(key)[0])

        return self.amount - self.discount

    def get_itens_keys(self):
        itens_keys = ""
        for items in self.products.values():
            for item in items:
                itens_keys += item.id + ", "

        itens_keys = itens_keys[:-2]
        return itens_keys