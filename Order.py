class Order:
    def __init__(self):
        self._id = None
        self._customer = None
        self._orderItems = []

    def getCustomer(self):
        return self._customer
    
    def setCustomer(self, customer : object):
        self._customer = customer

    def getOrderId(self):
        return self._id
    
    def setOrderId(self, id : int):
        self._id = id

    def getOrderedItems(self):
        return self._orderItems
    
    def setOrderedItems(self, orderItems : list):
        self._orderItems = []
        for orderItem in orderItems:
            self._orderItems.append(orderItem)
    
    def addOrderedItem(self, orderItem : object):
        self._orderItems.append(orderItem)
    