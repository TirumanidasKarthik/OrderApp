class Item:
    def __init__(self, desc : str, rate : float):
        self._desc = desc
        self._rate = rate

    def getItemDescription(self):
        return self._desc
    
    def setItemDescription(self, desc : str):
        self._desc = desc

    def getItemRate(self):
        return self._rate
    
    def setItemRate(self, rate : float):
        self._rate = rate