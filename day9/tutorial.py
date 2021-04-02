"""
Day 9: Enumerate

I have used enumerate before, it is used to number sequence elements
Definition from the tutorial: used to provide an iterator for a sequence and return each of its elements in a tuple

syntax:
enumerate(sequence,start=0)
default start value is 0
"""

#example 1:
languages = ['Python','swift','Java']

print(list(enumerate(languages)))
#Output: [(0, 'Python'), (1, 'swift'), (2, 'Java')]

for counter,element in enumerate(languages):
    print(counter,element)

#previous example with start=1

for counter,element in enumerate(languages,start=1):
    print(counter,element)