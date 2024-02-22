from item import Item
from errors import ItemNotExistError, ItemAlreadyExistsError

class ShoppingCart:

    def __init__(self):
        """
        Initializes the shopping cart with an empty dict of items(item names are the keys).
        """
        self.items = {}

    def add_item(self, item: Item):
        """
        Adds the given item to the shopping cart.
        Arguments: the current instance of ShoppingCart and an instance of Item.
        Exceptions: if the item name already exists in the shopping cart, raises ItemAlreadyExistsError.
        """
        if item.name in self.items:
            raise ItemAlreadyExistsError(item.name)
        else:
            self.items[item.name] = item
    def remove_item(self, item_name: str):
        """
        Removes the item with the given name from the shopping cart
        Aguments: the current instance of ShoppingCart and an instance of str.
        Exceptions: if no item with the given name exists, raises ItemNotExistError.
        """
        if item_name not in self.items:
            raise ItemNotExistError(item_name)
        else:
            self.items.pop(item_name)

    def get_subtotal(self) -> int:
        """:return: the subtotal price of all the items currently in the shopping cart."""
        subtotal = sum(item.price for item in self.items.values())
        return subtotal
