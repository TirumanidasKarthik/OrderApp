from RegCustomer import RegCustomer
class Company:
    def __init__(self, name : str):
        self._name = name
        self._items = []
        self._customers = []
    
    def getName(self):
        return self._name
    
    def setName(self, name : str):
        self._name = name

    def getItems(self):
        return self._items
    
    def setItems(self, items : list):
        self._items = []
        for item in items:
            self._items.append(item)
    
    def addItem(self, item : object):
        self._items.append(item)

    def getCustomers(self):
        return self._customers
    
    def setCustomers(self, customers : list):
        self._customers = []
        for customer in customers:
            self._customers.append(customer)
    
    def addCustomer(self, customer : object):
        self._customers.append(customer)

    def getTotalWorthOfOrdersPlaced(self):
        total = 0
        for customer in self.getCustomers():
            for order in customer.getOrders():
                for orderedItem in order.getOrderedItems():
                    price = orderedItem.getQuantity() * orderedItem.getItem().getItemRate()
                    if isinstance(customer, RegCustomer):
                        price -= (((customer.getSplDiscount()) / 100) * price)
                    total += price
        return total