"""
Create a recursive function which calculates the
factorial of a given number
Factorial: factorial(5) => 1*2*3*4*5 => 120
3 => 6
5 => 120
7 => 5040
10 => 3628800
"""


def recursive_factorial(num):
    if num == 1:
        return num
    return num * recursive_factorial(num-1)

count_list = [3,5,7,12]
total = map(recursive_factorial,count_list)

print(list(total))
# Output: [6, 120, 5040, 479001600]
# for 3,5,7,12

"""
Let's simulate the operation of the operator module (%).
4 % 2 => 0
59 % 6 => 5
"""
# I'm gonna try and reduce the given amount from the total amount every time
def recursive_operator(total,divisor):
    if total < divisor:
        return total
    # This feels a little cheaty, not quite sure how it works
    return recursive_operator(total - divisor,divisor)

count = 59
divisor = 6

total = recursive_operator(count,divisor)
print(total)
# Output: 6
