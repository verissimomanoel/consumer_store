# ----------------------------------------------------------------------------------------------------------------------
#   This software is free software.
# ----------------------------------------------------------------------------------------------------------------------
import abc
from ..model.item import Item


class AbstractRule(metaclass=abc.ABCMeta):
    """
    Abstract class to be extended for all rules implementation.
    Each subclass needs to implement its own rule of discount.
    """

    def __init__(self, name):
        """
        Class constructor.
        :param name: The name of the rule
        """
        self.name = name

    @abc.abstractmethod
    def process(self, item: Item, dict_items: dict) -> float:
        """
        Process the informed item applying the specific rule. If the rule is reached, return the discount value.
        :param item: The item to be processed
        :param dict_items: The dict of all items by types to check rules about discounts
        :return:
        """
        pass
