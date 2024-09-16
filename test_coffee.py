import pytest
from coffee import Coffee
from customer import Customer
from Order import Order

class TestCoffee:

    def test_coffee_creation(self):
        '''Test if a Coffee object is created with a valid name'''
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        
    def test_orders_method(self):
        '''Test if the orders method returns a list of all Order instances for the coffee'''
        coffee = Coffee("Latte")
        customer_1 = Customer("John")
        customer_2 = Customer("Alice")
        
        # Create orders and add to the coffee object
        order_1 = Order(customer_1, coffee, 5.0)
        order_2 = Order(customer_2, coffee, 6.0)
        coffee.add_order(order_1)
        coffee.add_order(order_2)

        # Check if the coffee object tracks all orders correctly
        orders = coffee.orders()
        assert len(orders) == 2
        assert order_1 in orders
        assert order_2 in orders

    def test_customers_method(self):
        '''Test if the customers method returns a unique list of Customer instances who ordered the coffee'''
        coffee = Coffee("Latte")
        customer_1 = Customer("John")
        customer_2 = Customer("Alice")
        
        # Create multiple orders from different customers
        order_1 = Order(customer_1, coffee, 5.0)
        order_2 = Order(customer_2, coffee, 6.0)
        coffee.add_order(order_1)
        coffee.add_order(order_2)

        # Test if coffee object tracks unique customers correctly
        customers = coffee.customers()
        assert len(customers) == 2
        assert customer_1 in customers
        assert customer_2 in customers

    def test_num_orders(self):
        '''Test if the num_orders method returns the correct number of orders'''
        coffee = Coffee("Espresso")
        customer_1 = Customer("John")
        customer_2 = Customer("Alice")
        
        # Add orders to the coffee
        order_1 = Order(customer_1, coffee, 5.0)
        order_2 = Order(customer_2, coffee, 6.0)
        coffee.add_order(order_1)
        coffee.add_order(order_2)
        
        # Test if num_orders returns the correct count
        assert coffee.num_orders() == 2

    def test_average_price(self):
        '''Test if the average_price method returns the correct average price of the coffee'''
        coffee = Coffee("Mocha")
        customer_1 = Customer("John")
        customer_2 = Customer("Alice")
        
        # Create orders with different prices
        order_1 = Order(customer_1, coffee, 5.0)
        order_2 = Order(customer_2, coffee, 7.0)
        coffee.add_order(order_1)
        coffee.add_order(order_2)
        
        # Check if the average price is correctly calculated
        assert coffee.average_price() == 6.0  # Average of 5.0 and 7.0 is 6.0

    def test_average_price_no_orders(self):
        '''Test if the average_price method returns 0 when there are no orders'''
        coffee = Coffee("Mocha")
        
        # Test with no orders
        assert coffee.average_price() == 0

