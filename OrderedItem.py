class OrderedItem:
    def __init__(self, item : object, quantity : int):
        self._item = item
        self._quantity = quantity

    def getItem(self):
        return self._item
    
    def setItem(self, item : object):
        self._item = item

    def getQuantity(self):
        return self._quantity
    
    def setQuantity(self, quantity : int):
        self._quantity = quantity