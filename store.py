import yaml

from errors import ItemNotExistError, TooManyMatchesError
from item import Item
from shopping_cart import ShoppingCart

class Store:
    def __init__(self, path):
        with open(path) as inventory:
            items_raw = yaml.load(inventory, Loader=yaml.FullLoader)['items']
        self._items = self._convert_to_item_objects(items_raw)
        self._shopping_cart = ShoppingCart()

    @staticmethod
    def _convert_to_item_objects(items_raw):
        return [Item(item['name'],
                     int(item['price']),
                     item['hashtags'],
                     item['description'])
                for item in items_raw]

    def get_items(self) -> list:
        return self._items

    def search_by_name(self, item_name: str) -> list:
        """
        :args: the current instance of Store and an instance of str.
        :return: a sorted list of all the items that match the search term, and not already in the shopping cart.
    
        The items in the returned list must contain the given phrase (and do not have to exactly match it).
        For example, when searching for "soap", items such as "dish soap" and "body soap" should be returned.
        """
        # for each item, check: contains the given item_name & not in shopping cart
        search_result = [item for item in self._items if item_name in item.name and item_name not in self._shopping_cart.items]
        
        # Sorting using a tuple as the key. The first element is the rank, the second is the item's name. we multiply
        # the rank by -1 to get the highest rank first, while the item's name is sorted by default(earlier
        # alphabetically comes first).
        search_result.sort(key=lambda item: ((-1)*self._shopping_cart.get_item_rank_in_cart(item), item.name))

        return search_result

    def search_by_hashtag(self, hashtag: str) -> list:
        """
        :args: the current instance of Store and an instance of str.
        :return: a sorted list of all the items that has the given exact hashtag, and not already in the shopping cart.

        For example, when searching for the hashtag "paper", items with hashtags such as "tissue paper" must not be returned.
        """
        # for each item, check: contains the given hashtag & not in shopping cart
        search_result = [item for item in self._items if hashtag in item.hashtags and item.name not in self._shopping_cart.items]
        # Sorting using a tuple as the key. The first element is the rank, the second is the item's name. we multiply
        # the rank by -1 to get the highest rank first, while the item's name is sorted by default(earlier
        # alphabetically comes first).
        search_result.sort(key=lambda item: ((-1)*self._shopping_cart.get_item_rank_in_cart(item), item.name))
        return search_result

    def add_item(self, item_name: str):
        """
        Adds an item with the given name to the customer’s shopping cart.
        Arguments: the current instance of Store and an instance of str.
        Exceptions: no such item exists, raises ItemNotExistError.
                    there are multiple items matching the given name, raises TooManyMatchesError.
                    the given item is already in the shopping cart, raises ItemAlreadyExistsError.
        To ease the search for the customers, not the whole item’s name must be given, but rather a distinct substring.
        For example, when adding "soap" to the cart, if an item such as "body soap" exists, and no other item with the
        substring "soap" in its name, "body soap" should be added to the list.
        You may assume that no two items exist such that one's name is a substring of the other.
        """
        #FIXME
        # we need to search for the item in all items, and not only items that are not in the shopping cart
        # not sure about this case. maybe we do need to search only in items that are not in the shopping cart

        search_result = [item for item in self._items if item_name in item.name]

        # no matches found, raises ItemNotExistError
        if len(search_result) == 0:
            raise ItemNotExistError(item_name)

        # if multiple matches found, and there is no item with the exact name, raises TooManyMatchesError
        if len(search_result) > 1 and not any(item_name == item.name for item in search_result):
            raise TooManyMatchesError(item_name)

        # if item already exists in the shopping cart, add_item will raise ItemAlreadyExistsError
        if item_name in self._shopping_cart.items:
            raise ItemAlreadyExistsError(item_name)

        item = self.search_by_name(item_name)[0]
        self._shopping_cart.add_item(item)

    def check_distinct_substring(self, item_name: str):
        """
        Checks if the given item_name is a distinct substring of an item's name.
        :param item_name: the given item_name
        :return: True if the item_name is a distinct substring of an item's name, False otherwise.
        """
        return len(self.search_by_name(item_name)) == 1

    def remove_item(self, item_name: str):
        """
        Removes an item with the given name from the customer’s shopping cart.
        Arguments: the current instance of Store and an instance of str.
        Exceptions: if no such item exists, raises ItemNotExistError. If there are multiple items matching the given name, raises TooManyMatchesError.
        In a similar fashion to add_item, here too, not the whole item’s name must be given for it to be removed.
        """
        pass

    def checkout(self) -> int:
        """:return: the total price of all the items in the costumer’s shopping cart."""
        return self._shopping_cart.get_subtotal()
