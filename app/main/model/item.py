# ----------------------------------------------------------------------------------------------------------------------
#   This software is free software.
# ----------------------------------------------------------------------------------------------------------------------

class Item:
    """
    Model of item in the store.
    """

    def __init__(self, id: str, name: str, price:float):
        """
        Class constructor.
        :param id: The id of item
        :param name: The name of item
        :param price: The price of item
        """
        self.id = id
        self.name = name
        self.price = price