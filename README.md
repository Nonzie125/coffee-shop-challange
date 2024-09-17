COFFEE CODE CHALLANGE - Coffee Shop (Object Relationships)
For this assignment, I will be working with a Coffee shop-style domain.

I have three models: Coffee, Customer, and Order.

For our purposes, a Coffee has many Orders, a Customer has many Orders, and a Order belongs to a Customer and to a Coffee.

Coffee - Customer is a many to many relationship.

Instructions I Used;

To get started, run pipenv install while inside of this directory. Then run pipenv shell to jump into the shell.
I Sketched  domain model on paper or a whiteboard before coding:

STEPS

Identify the three main classes: Customer, Coffee, and Order.
Establish the relationships between these classes.
Determine the attributes and methods that each class will have.
Keep in mind the concept of a single source of truth for your data.

Create Class Files
Create three Python files in THE project directory:

customer.py: I Initialize a Customer with a name (string between 1 and 15 characters).
              Implement a property name with the necessary validation.
coffee.py:I Initialize a Coffee with a name (string, at least 3 characters long).
          Implement a property name with the necessary validation.
order.py: I Initialize an Order with a Customer instance, a Coffee instance, and a price (float between 1.0 and 10.0).
          Implement properties customer, coffee, and price with the necessary validation.
          In each file, a class is defined corresponding to the file name (e.g., class Customer in customer.py).
 
I later defined the  Object Relationship Methods and Properties between the three files and Implemented Aggregate and Association Methods 
where in the customer.py file 
  it create_order(coffee, price) method:
   Receives a Coffee instance and a price.
  Creates a new Order instance.
  Associates it with that customer and the coffee.

In the coffee.py file it num_orders() method it will:

     Returns the total number of times a coffee has been ordered.
      average_price() method:

      Returns the average price for a coffee based on its orders.num_orders() method:

      Returns the total number of times a coffee has been ordered.
      average_price() method:

      Returns the average price for a coffee based on its orders.num_orders() method:

      Returns the total number of times a coffee has been ordered.
      average_price() method:

      Returns the average price for a coffee based on its orders.
Testing
I Created a tests directory in your project directory.

Add test files (test_customer.py, test_coffee.py, test_order.py) to test each class and method.
I the Wrote test cases to validate that each method and property works correctly.
Later i used pytest to run my tests:
For any question feel free to reach me via 0727 207 156
