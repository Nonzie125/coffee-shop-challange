class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []  # A list to store all orders made by this customer

    def orders(self):
        '''Returns a list of all Order instances for this customer'''
        return self._orders

    def coffees(self):
        '''Returns a unique list of Coffee instances that this customer has ordered'''
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        '''Creates a new order for the customer and adds it to the list of orders'''
        order = order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)  # inncase of an add method
    
        return order
