import pytest
from customer import Customer
from coffee import Coffee
from Order import Order

class TestCustomer:

    def test_customer_creation(self):
        '''Test if a Customer object is created with a valid name'''
        customer = Customer("John")
        assert customer.name == "John"
        
    def test_orders_method(self):
        '''Test if the orders method returns a list of all orders for the customer'''
        customer = Customer("John")
        coffee_1 = Coffee("Latte")
        coffee_2 = Coffee("Espresso")
        
        # if Customer creates two orders
        order_1 = customer.create_order(coffee_1, 5.0)
        order_2 = customer.create_order(coffee_2, 4.0)
        
        orders = customer.orders()
        assert len(orders) == 2
        assert order_1 in orders
        assert order_2 in orders

    def test_coffees_method(self):
        '''Test if the coffees method returns a unique list of coffees the customer has ordered'''
        customer = Customer("Nonzamo")
        coffee_1 = Coffee("Latte")
        coffee_2 = Coffee("Espresso")
        
        # Nonzamo orders the same coffee multiple times
        customer.create_order(coffee_1, 5.0)
        customer.create_order(coffee_1, 6.0)
        customer.create_order(coffee_2, 4.0)  # A different coffee
        
        # coffee ordered
        coffees = customer.coffees()
        assert len(coffees) == 2
        assert coffee_1 in coffees
        assert coffee_2 in coffees
    
    def test_create_order_method(self):
        '''Test if create_order correctly establishes the relationships between customer, coffee, and order'''
        customer = Customer("Alice")
        coffee = Coffee("Cappuccino")
        
        # a order created by the customer
        # creates an order
        order = customer.create_order(coffee, 5.5)
        
        # this will Test if the order is added to the customer's orders list
        assert order in customer.orders()
        
        #  if the coffee object tracks the order
        assert order in coffee.orders()
        
        #  if the correct price was assigned
        assert order.price == 5.5
        assert order.customer == customer
        assert order.coffee == coffee
