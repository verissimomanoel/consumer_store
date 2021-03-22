# ----------------------------------------------------------------------------------------------------------------------
#   This software is free software.
# ----------------------------------------------------------------------------------------------------------------------
from ..model.item import Item


class Checkout():
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

        if item.id == self.CENTRAL_AC_KEY:
            if self.charger.id not in self.products:
                self.products[self.charger.id] = []

            self.products[self.charger.id].append(self.charger)

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
                    discount = rule.process(item, self.products)
                    self.amount -= discount

    def total(self):
        self.amount = 0
        for key in self.products.keys():
            for item in self.products.get(key):
                self.amount += item.price

            self.__apply_rules(self.products.get(key)[0])

        return self.amount
