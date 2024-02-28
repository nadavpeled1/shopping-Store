class ItemNotExistError(Exception):
    """ when trying to operate on an item that does not exist in the shopping cart"""
    def __init__(self, item_name: str):
        self.item_name = item_name
        super().__init__(f'Item {item_name} does not exist in the shopping cart.')
    


class ItemAlreadyExistsError(Exception):
    """when trying to add an item that already exists in the shopping cart"""
    def __init__(self, item_name: str):
        self.item_name = item_name
        super().__init__(f'Item {item_name} already exists in the shopping cart.')


class TooManyMatchesError(Exception):
    """when trying to add an item substring that matches multiple items (and no such item with the exact name exists)"""
    def __init__(self, item_name: str):
        self.item_name = item_name
        super().__init__(f'Too many matches for the item name "{item_name}".')
