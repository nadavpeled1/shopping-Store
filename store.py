import yaml

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
        
        # Sorting using a tuple as the key. The first element is the rank, the second is the item's name.
        # we multiply the rank by -1 to get the highest rank first, while the item's name is sorted by default(earlier alphabetically comes first).
        search_result.sort(key=lambda item: ((-1)*self._shopping_cart.get_item_rank_in_cart(item), item.name))

        return search_result # keys are the item's names, so it sorts by item names by default

    def search_by_hashtag(self, hashtag: str) -> list:
        """
        :args: the current instance of Store and an instance of str.
        :return: a sorted list of all the items matching the search criterion. The sort order is described below.
        
        The items in the returned list must have the given hashtag in their hashtag list.
        For example, when searching for the hashtag "paper", items with hashtags such as "tissue paper" must not be returned."""
        search_result = [item for item in self._shopping_cart.items if hashtag in item.hashtags]
        return sorted(search_result, key=lambda item: item.name)
    

    def add_item(self, item_name: str):
        # TODO: Complete
        pass

    def remove_item(self, item_name: str):
        # TODO: Complete
        pass

    def checkout(self) -> int:
        # TODO: Complete
        pass
