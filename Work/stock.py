class Stock:
    __slots__ = ("name", "_shares", "price")
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})' 
    
    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("expected an integer")
        self._shares = value

    def sell(self, amt):
        if self.shares < amt:
            raise RuntimeError("Amount of sell exceeds stock holdings")
        self.shares -= amt

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor
    def panic(self):
        self.sell(self.shares)
    
    def cost(self):
        actual_cost = super().cost()
        return self.factor * actual_cost