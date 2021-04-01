"""
Day 8: Comprehensions

Comprehensions allow in a clear way to create sequences from sequences

Syntax:
new_list = [output for i in sequence if condition]

I've used these before, they are very useful when working with big data
"""
#common example:
totals = []
for number in range(1,7):
    totals.append(number*2)

print(totals)

#Comprehension
new_totals = [i*2 for i in range(1,7)]
print(new_totals)
#We can also do this with map, as I've learned a couple days ago


#Filtering odd numbers
odd_nums = [i for i in range(1,19) if i%2==1]
print(odd_nums)
#Output: [1, 3, 5, 7, 9, 11, 13, 15, 17]

"""
Dict Comprehensions
Works the same, but obviously you have to determine key:value

syntax:
new_dict = {output_key: output_value for i in sequence if condition}
"""
new_dict = {}
numbers = [6,2,6,8,1]
for i in numbers:
    new_dict[i] = i*i

print(new_dict)
#{6: 36, 2: 4, 8: 64, 1: 1}

#With Comprehension
newest_dict = {i:i*i for i in numbers}
print(newest_dict)