"""
Given an integer k, print the first k non-prime positive integers,
each on a new line. For example, if k = 10, the output would be:
1 4 6 8 9 10 12 14 15 16 18 20
Test 1:
- Inputs
    12
- Outputs
    1 4 6 8 9 10 12 14 15 16 18 20
"""

# Prime numbers are only divisible by 1 and themselves

# Try to divide the input by all numbers leading up to half of it
# get a range from 2-num, since we don't count 1, and look for leftovers

total_iterations = 18

def non_prime():
    counter = 1
    last_value = 1
    while counter < total_iterations:
        for i in range(2,last_value):
            if last_value % i == 0:
                yield last_value
                last_value += 1


        counter += 1
        last_value +=1

end_value = non_prime()


for i in range(total_iterations):
    print(next(end_value))

