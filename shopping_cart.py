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
        Arguments: the current instance of ShoppingCart and an instance of str.
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

    def get_tags_list(self) -> list:
        """
        :return: a list of all the hashtags of the items currently in the shopping cart (with repetitions).
        """
        return [tag for item in self.items.values() for tag in item.hashtags]

    def get_tags_ranks(self) -> dict:
        """
        :return: a dict of all the hashtags of the items currently in the shopping cart as keys,
        and the number of times they appear in the shopping cart as values.
        """
        tags = self.get_tags_list()
        tags_ranks = {tag: tags.count(tag) for tag in tags}
        return tags_ranks

    def get_item_rank_in_cart(self, item: Item) -> int:
        """
        :args: the current instance of ShoppingCart and an item to check its rank.
        :return: the number of common hashtags between the given item and the items currently in the shopping cart.
        """
        if len(self.items) == 0: # empty cart
            return 0

        cart_tags_ranks = self.get_tags_ranks()
        rank = sum(cart_tags_ranks[tag] for tag in item.hashtags if tag in cart_tags_ranks)
        return rank
