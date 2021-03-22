# ----------------------------------------------------------------------------------------------------------------------
#   This software is free software.
# ----------------------------------------------------------------------------------------------------------------------
from .abstract_rule import AbstractRule
from ..model.item import Item


class CentralACRule(AbstractRule):
    CHARGER_KEY = "mch"

    def __init__(self, name):
        """
        Class constructor.
        :param name: The name of rule
        """
        super(CentralACRule, self).__init__(name)

    def process(self, item: Item, dict_items: dict) -> float:
        """
        Process the rule according to the specification below:
        We will add an additional Charger free of cost with every Central AC sold
        :param item: The item to be processed
        :param items: The list of item to check rules about discounts
        :return:
        """
        charger = dict_items.get(self.CHARGER_KEY)[0]
        items = dict_items.get(item.id)

        return len(items) * charger.price
