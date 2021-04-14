"""
Day 15: Else

Starting day 15, we are in the advanced concepts section of python30, meaning we are gonna learn advanced versions of concepts such as else

as we've seen in Error Handling, Else can be used for more than if-statements
"""

# For/Else

# Example 1
numbers = range(10,21)
# The break function will break the loop and continute outside of it
for number in numbers:
    if number == 60:
        break
    #print(number)
# If the break is not executed, whatever's in Else will run:
else:
    print("Number 60 was not found")
# Output: 10 11 12 13 14 15 16 17 18 19 20
# Number 60 was not found


# While/Else
# Else also works with While the same way

second_numbers = range(40,74)
i=0
while second_numbers[i]<50:
    if second_numbers[i] == 51:
        print('found 51')
        break
    i+=1
else:
    print('number not found')

