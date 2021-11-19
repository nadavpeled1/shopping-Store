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
        # TODO: Complete
        pass

    def search_by_hashtag(self, hashtag: str) -> list:
        # TODO: Complete
        pass

    def add_item(self, item_name: str):
        # TODO: Complete
        pass

    def remove_item(self, item_name: str):
        # TODO: Complete
        pass

    def checkout(self) -> int:
        # TODO: Complete
        pass
