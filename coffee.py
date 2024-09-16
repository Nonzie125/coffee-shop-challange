class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []  # A list to store all orders for this coffee

    def orders(self):
        '''Returns a list of all Order instances for this coffee'''
        return self._orders

    def customers(self):
        '''Returns a unique list of Customer instances who have ordered this coffee'''
        return list(set(order.customer for order in self._orders))

    def add_order(self, order):
        '''Adds an order to the list of orders for this coffee'''
        self._orders.append(order)

    def num_orders(self):
        '''Returns the total number of times this coffee has been ordered'''
        return len(self._orders)

    def average_price(self):
        '''Returns the average price for this coffee based on its orders'''
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)
