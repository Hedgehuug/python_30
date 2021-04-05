"""
Day 10: Error handling

Python has the try/except notation to handle errors, I have used this before, but never actually learned about it
"""

# try block is the code we're gonna try to run, and except is what to return in-case of an error
value = 'hello'
try:
    print(int(value))
except:
    print("not int")

# You can define specific errors to catch, we did not do this in previous example

"""
Python has some built in exceptions

int('hello') would generate:
Traceback (most recent call last):
  File "tutorial.py", line 17, in <module>
    int('hello')
ValueError: invalid literal for int() with base 10: 'hello'
"""
# From this we can take away that we need to look for ValueErrors, so let's do that

try:
    print(int('Hello'))
except ValueError as err:
    print("An exception occured:",err)

# Multiple Exceptions:

try:
    int('Hello')
except (ValueError,TypeError) as err:
    print("An exception occured:",err)
    # we can define multiple exceptions in one block
except ZeroDivisionError:
    # we can also separate them for the same try block
    print("an exception occured")


# Raising Exceptions
# Not sure I understand the need for Raise besides another notation, but it seems like best practices push away from that

try:
    number = "Hello"
    if not number.isnumeric():
        raise ValueError(f"{number} is not numeric")
except (ValueError,TypeError) as err:
    print("An exception occured:",err)

# Else: else can also be used with error handling to run an alternative if nothing is raised

try:
    number = 12
    int(number)
except ValueError as err:
    print("An exception was raised:",err)
else:
    print("No exception occured")
    print(f"Number: {number}")

# Finally: finally is another clause we can use with try/except, it'll run at the end regardless of the outcome

try:
    int('Hello')
except ValueError as err:
    print('An exception occured')
else:
    print('No exception occured')
finally:
    print("this'll print regardless of the outcome")
# Outcome:
# An exception occured
# this'll print regardless of the outcome