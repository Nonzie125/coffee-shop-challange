import pytest
from Order import Order
from coffee import Coffee
from customer import Customer

class TestOrder:

    def test_order_creation(self):
        '''Test if an Order object is created with valid customer, coffee, and price'''
        customer = Customer("John")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)

        assert order.customer == customer  # Test customer association
        assert order.coffee == coffee  # Test coffee association
        assert order.price == 5.0  # Test price

    def test_customer_property(self):
        '''Test if the customer property returns the correct Customer instance'''
        customer = Customer("Alice")
        coffee = Coffee("Cappuccino")
        order = Order(customer, coffee, 6.0)

        assert order.customer == customer  # Test customer retrieval

    def test_coffee_property(self):
        '''Test if the coffee property returns the correct Coffee instance'''
        customer = Customer("Bob")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 4.5)

        assert order.coffee == coffee  # Test coffee retrieval

    def test_order_price(self):
        '''Test if the order has the correct price'''
        customer = Customer("John")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 7.0)

        assert order.price == 7.0  # Test price value

    def test_order_invalid_price_low(self):
        '''Test if an order raises a ValueError for too low a price'''
        customer = Customer("John")
        coffee = Coffee("Mocha")
        
        # Expect a ValueError if price is less than 1.0
        with pytest.raises(ValueError, match="Price is too low"):
            Order(customer, coffee, 0.5)

    def test_order_invalid_price_high(self):
        '''Test if an order raises a ValueError for too high a price'''
        customer = Customer("Alice")
        coffee = Coffee("Cappuccino")
        
        # Expect a ValueError if price is greater than 10.0
        with pytest.raises(ValueError, match="Price is too high"):
            Order(customer, coffee, 12.0)
