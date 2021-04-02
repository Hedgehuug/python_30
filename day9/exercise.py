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
    print(counter+'. '+names)