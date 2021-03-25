"""
Day 2: Range

Syntax: range(start,stop,step)
"""

#prints the details of the list
print(range(5))

#prints list
sequence = list(range(5))
print(sequence)


#two Parameters
two_para = list(range(2,8))
print(two_para)


#three Parameters
three_para = list(range(-3,14,2))
#last peremeter is the step, so this'll include every second number starting -3 and before 14
print(three_para)


#Only integers work with Range