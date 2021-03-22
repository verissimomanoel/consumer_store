# ----------------------------------------------------------------------------------------------------------------------
#   This software is free software.
# ----------------------------------------------------------------------------------------------------------------------
from .abstract_rule import AbstractRule
from ..model.item import Item


class SonyRule(AbstractRule):
    PRICE_WITH_DISCOUNT = 499.99

    def __init__(self, name):
        """
        Class constructor.
        :param name: The name of rule
        """
        super(SonyRule, self).__init__(name)

    def process(self, item: Item, dict_items: list) -> float:
        """
        Process the rule according to the specification below:
        Sony TV will have a Bulk discount, where the price will drop to $499.99 each, if someone buys more than 4.
        :param item: The item to be processed
        :param dict_items: The dict of all items by types to check rules about discounts
        :return:
        """
        items = dict_items.get(item.id)
        diff = item.price - self.PRICE_WITH_DISCOUNT
        if len(items) < 4:
            return 0
        else:
            return len(items) * diff
