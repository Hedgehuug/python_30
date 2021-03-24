"""
Create a function that receives N numbers and returns
each of these multiplied by 2
"""

def multiply_by_2(*args):
    output = []
    for i in args:
        i2 = i*2
        output.append(i2)
        print(i2)
    return output
        
#multiply_by_2(1,2,3,4)

"""
Create a function that receives N arguments with your
personal information: name, age, phone, country, etc
Then print those values with their names

name: your name
country: your country
"""
def personal_information(**kwargs):
    for item in kwargs.items():
        print(item[0]+":",item[1])
    

personal_information(name='Ben',age=21,nationality='Hungary')


"""
The Python print function receives positional and named arguments,
the named arguments are used to alter the way this print works:
sep = It indicates how all the values we pass will be separated
end = Indicates what you will put at the end of printing
Default Values:
sep = " "
end = "\n"
Use the *args and **kwargs to pass these arguments and print a phrase
depending on a tuple/list of values.
"""

to_print = ['This','text','will','display','in','a','bunch','of','ways']

print(*to_print,sep=' ',end='.\n')
print(*to_print,sep=',',end='.\n')
print(*to_print,sep=', ',end='.\n')
print(*to_print,sep='-',end='.:)\n')