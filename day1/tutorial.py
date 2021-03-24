"""
*args and **kwargs
Positional and Keyword arguments 

"""
#Positional arguments don't have a default value

def positional_multiply(a,b):
    print(a*b)

positional_multiply(5,4)

#Keyword arguments have their value set

def keyword_multiply(a=1,b=2):
    print(a*b)

#This can be edited when invoking the function
keyword_multiply()
keyword_multiply(5,3)
keyword_multiply(b=5,a=8)

# *args == positional --- **kwargs == keyword

#using *args returns the arguments as tuples
def positional_fun(*args):
    print(args)

positional_fun(1,2,3)

#**kwargs expects and returns a Dict as arguments
def keyword_fun(**kwargs):
    print(kwargs)

keyword_fun(a=1,b=2,c=3)

#Both of them can be used in the same function
def mixed_fun(*args,**kwargs):
    print(args)
    print(kwargs)

mixed_fun(1,2,apple='red',b=2)

#The * and ** can be used the other way too, allowing us to interpret inputs differently
def func(a,b,c):
    print(a,b,c)

numbers = [1,2,3]
func(*numbers)

kwNumbers = {"a":1,"c":2,"b":3}

func(**kwNumbers)

#Hello world
text = ['hello','world']
print(*text)