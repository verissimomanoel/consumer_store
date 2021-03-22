# ----------------------------------------------------------------------------------------------------------------------
#   This software is free software.
# ----------------------------------------------------------------------------------------------------------------------
from .abstract_rule import AbstractRule
from ..model.item import Item


class NikeRule(AbstractRule):
    def __init__(self, name):
        """
        Class constructor.
        :param name: The name of rule
        """
        super(NikeRule, self).__init__(name)

    def process(self, item: Item, dict_items: dict) -> float:
        """
        Process the rule according to the specification below:
        We have a 3 for 2 great deal on Nike Shoes. i.e. if you buy 3 Nike Shoes, you’ll just pay the price of 2.
        :param item: The item to be processed
        :param dict_items: The dict of all items by types to check rules about discounts
        :return:
        """
        items = dict_items.get(item.id)
        return item.price * int(len(items) / 3)
