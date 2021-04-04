"""
Create a list of 5 names and use the enumerate function to
display them as follows:
1. Name One
2. Name Two
...
5. Name Five
"""

list_of_names = ["tim",'tom','ben','bin','bim']

for counter,names in enumerate(list_of_names,start=1):
    print(counter,'. ',names,sep='')
#I actually did not know how to change the separator for print, but I made an educated guess


"""
Use the enumerate function on a string (your name) and print
each character with its corresponding index
"""

my_name = 'Ben Dover'

for counter,letter in enumerate(my_name):
    print(str(counter)+':',letter)
#I don't get this one, it's the same question as before, I did it in a different way I guess