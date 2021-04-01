"""
Day 7: Lambdas
oh finally single line functions, this is something I've been wanting to learn about but never knew what they were called
Lambda functions, also called anonymous functions

Syntax:
lambda arguments: expression
"""

"""Example 1:"""

#Normal function
def normal_multiply(num1,num2):
    return num1 * num2

#Lambda function
lambda_multiply = lambda num1,num2: num1*num2

print(normal_multiply(2,5))
print(lambda_multiply(2,5))
#Output: 10

#Lambda functions are perfect for simple functions that don't need to take up multiple lines of code
#Also works very well with higher order functions

"""Example 2:"""
#Example of using Filter() with lambda functions

#normal function
def multiple(number):
    return number % 2 == 0

numbers = range(1,101)
mutiple_filter = filter(multiple,numbers)
print(list(mutiple_filter))
#Output: [2, 4, 6, 8...96, 98, 100]

#lambda function: (will use numbers range from before)

lambda_function = lambda num: num % 2 == 0
lambda_filter = filter(lambda_function,numbers)

print(list(lambda_filter))

#       OR IF YOU WANT IT IN A SINGLE LINE
print(list(filter(lambda num:num%2==0,range(1,101))))


