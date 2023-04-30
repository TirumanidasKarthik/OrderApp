class Customer:
    def __init__(self, name : str):
        self._name = name
        self._orders = []

    def getName(self):
        return self._name   
    
    def setName(self, name : str):
        self._name = name

    def getOrders(self):
        return self._orders
    
    def setOrders(self, orders : list):
        self._orders = []
        for order in orders:
            self._orders.append(order)
    
    def addOrder(self, order : object):
        self._orders.append(order)

    
