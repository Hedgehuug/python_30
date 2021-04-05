"""
Use try/except to catch an error, you can try to validate
what happens when we do
my_list = ["a", "b", "c"]
print(my_list[10])
"""
my_list = ['a','b','c']
# print(my_list[10])
# This will return an error with IndexError so I'll use that
try:
    print(my_list[10])
except IndexError as err:
    print(f"An exception occured: {err}")


"""
Cause an exception to be raised using the raise keyword and
print a message after you have finished catching the error
at finally.
"""
try:
    raise ValueError
except ValueError:
    print('Value Error')
finally:
    print("What do I print here?")
    
#This one is really difficult, I looked at the solution, and I can just raise an error myself

"""
Use input function to request information to the user and in
the try/except structure catches multiple errors that can be
generated
"""
user_input = input("Type in a number: ")

try:
    int(user_input)
except ValueError as err:
    print(f"{err} is not a number")
except TypeError as err:
    print(f"{err} is not type used")
else:
    print("Your input is correct:",user_input)
finally:
    print("end")