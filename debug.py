# debug.py

from customer import Customer
from coffee import Coffee
from orders import Order

def main():
    # we create customers
    customer_1 = Customer("Nonzamo")
    customer_2 = Customer("nyakagwa")
    customer_3 = Customer("Bob")

    # Create Coffees
    coffee_1 = Coffee("Latte")
    coffee_2 = Coffee("Espresso")
    coffee_3 = Coffee("Mocha")

    # lets create Orders
    order_1 = customer_1.create_order(coffee_1, 4.5)
    order_2 = customer_1.create_order(coffee_2, 5.0)
    order_3 = customer_2.create_order(coffee_1, 4.0)
    order_4 = customer_3.create_order(coffee_3, 6.5)

    # Debugging Output goes here
    print("Customer 1 Orders:")
    for order in customer_1.orders():
        print(f"Order: {order.coffee.name} - ${order.price}")

  