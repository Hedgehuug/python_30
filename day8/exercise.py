"""
Create a list of words and with it, create a new dictionary
in which the key is the word and the value is the same word
reversed.
"""

word_list = ['Tree','Apple','Snake','flowers']
word_dict = {word:word[::-1] for word in word_list}
print(word_dict)
#Output: {'Tree': 'eerT', 'Apple': 'elppA', 'Snake': 'ekanS', 'flowers': 'srewolf'}

"""
Let's try this one again:
Using the range function, create a sequence of numbers
from 1 to 100, and using the comprehension to return only
those that are multiplies of 2.
"""
use_range = range(1,101)
multiple_list = [i for i in use_range if i%2==0]
print(multiple_list)


"""
[[1, 2, 3, 4], [5, 6, 7, 8]]
Use the list above and create nested comprehensions so that
the final value is a new list like the following
[[2, 4, 6, 8], [10, 12, 14, 16]] The number multiplied by 2
"""
list_above = [[1, 2, 3, 4], [5, 6, 7, 8]]

final_list = [[bottom*2 for bottom in top] for top in list_above]
print(final_list)