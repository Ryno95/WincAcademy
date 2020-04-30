# Function composition:
# def <function_name>([<parameters>]):
#    <statement(s)>

# BAsic function
def f():
    s = "--inside of f()"
    print(s)


# Function with positional arguments
# When calling a function with argumetns, all arguments must be given a value
# ex 3 arguments = 3 values
def productCost(qty, item, price):
    print(f"{qty} {item} cost ${price:.2f}")


productCost(2, "Burgers", 3.79)


# Calling a Function with keyword arguments, order of argumetns not important
productCost(item="bananas", qty=6, price=1.74)

# Functions with default/optional parameters
# When called without passing the arguments, the default parameters
def transactionCost(qty=10, item="oranges", price=2.39):
    print(f"{qty} {item} cost ${price:.2f}")


transactionCost()
