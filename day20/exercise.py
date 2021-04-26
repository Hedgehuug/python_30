"""
Try to solve one of your problems by creating a context
manager, I give you some suggestions:
- Open and close the browser (Selenium).
- Connect and Close the connection of a database.
"""

# Well the only thing I can think of for this is using it to import some txt files with lists of references to send to an API
# This I can do in another project

# I'll instead just recreate what I did 


class ContextManager:
    def __init__(self,file_name):
        self.__file = open(file_name)

    def __enter__(self):
        return self.__file
        

    def __exit__(self,file,value,traceback):
        self.__file.close()


with ContextManager('info.txt') as file:
    print(file.read())



"""
You can investigate the "contextlib" module and see other
types of context managers you can create, try one to
*suppress* any ValueError exceptions.
"""

import contextlib


help(contextlib)
