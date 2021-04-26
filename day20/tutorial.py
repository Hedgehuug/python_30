"""
Day 20: Context Managers


When working with any programming language, if we use any resources, we must release them once we no longer need them
this is good programming practice as leaving dependancies open will slow down software
"""

# Let's suppose our operation requires us to open some files:
file = open('info.txt','r')
content = file.read()
file.close()
# Here we release the file after by literally closing it

# Python has a built-in way of handling this with, well, 'with'
# The previous example would look like this:
with open('info.txt','r') as file:
    content = file.read()
print(content)

# To use context managers with classes, we are going to be using some dunder methods
# more precisely __enter__ and __exit__

class ContextManager:
    def __init__(self,filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    # ----- FOR SOME REASON HAVING 4 PROPERTIES IS MANDATORY FOR __EXIT__
    def __exit__(self, type, value, traceback):
        self.file.close()

    # This class will just automatically open and then close the file as the class is called


with ContextManager('info.txt') as file:
    content = file.read()


# Context managers with Functions:
# We need to import contextmanager from contextlib to use a func()
from contextlib import contextmanager

# To get it working with functions, we need to use decorators to decorate functions
@contextmanager
def open_file(filename):
    file = open(filename)
    try:
        # Another thing about using it with functions is the necessity for Yield
        yield file
    except:
        # Exceptions that may occur
        pass
    finally:
        file.close()

with open_file('info.txt') as file:
    content = file.read()

print(content)


