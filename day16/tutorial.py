"""
Day 16: Recursion

Recursive functions are functions that call themselves, and will repeat it indefinitely until we stop
^^ This is cool, reading the description this opens up a whole new dimension to things
"""

# We can turn any loop into a recursion
first_total = 0
for num in range(6):
    first_total += num

print(f'The sum of numbers from 1-5 is {first_total}')
# Output: The sum of numbers from 1-5 is 15


# We can convert this into a recursive function like:

def recursive_function(num):
    if num == 1:
        # The return of the terminating if has to be the same variable type as the regular return
        return num
    # this keeps repeating the function until the previous if condition gets validated
    return num + recursive_function(num-1)

times = 5
total = recursive_function(times)

print(f'the sum of numbers from 1-5 is {total}')
# Output: the sum of numbers from 1-5 is 15

# The first condition is used to end the recursion once the value of the 
# argument is 1 and it will go in a chain by returning the total and adding it to the previous number. In other words:

# First execution
>>> total = recursive_function(5)
>>> return 5 + recursive_function(4)
    # Second execution
    >>> return 4 + recursive_function(3)
        # Third execution
        >>> return 3 + recursive_function(2)
            # Fourth execution
            >>> return 2 + recursive_function(1)
                # Fifth execution
                >>> return 1
            >>> return 2 + 1 # 1 of the fifth execution
        >>> return 3 + 3 # 3 of the fourth execution
    >>> return 4 + 6 # 6 of the third execution
>>> return 5 + 10 # 10 of the second execution

# The sum of the numbers from 1 to 5 is equals to 15
# This is copied from the tutorial