class Order:
    def __init__(self, customer, coffee, price):
        self._customer = customer  # Use private attributes to store customer and coffee
        self._coffee = coffee
        self.price = price

    @property
    def customer(self):
        '''Returns the Customer instance associated with this order'''
        return self._customer

    @property
    def coffee(self):
        '''Returns the Coffee instance associated with this order'''
        return self._coffee
