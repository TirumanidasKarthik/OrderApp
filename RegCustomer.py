from Customer import Customer
class RegCustomer(Customer):
    def __init__(self, name : str, splDiscount):
        super().__init__(name)
        self._splDiscount = splDiscount

    def getSplDiscount(self):
        return self._splDiscount
    
    def setSplDiscount(self, splDiscount : float):
        self._splDiscount = splDiscount

 
