# 1. Positional parameters and keyword parameters
# A positional parameter is a required parameter that must be passed in the correct order.
# A keyword parameter is an optional parameter that has a default value and can be specified by name.

def func(x, y, z=True):  # 'z' is a keyword parameter with a default value of True
    print(x, y, z)

# Calling the function with positional arguments and a keyword argument
func('param1', 'param2', z=False)
# Output: param1 param2 False


# 2. Optional parameter
# An optional parameter is a parameter with a default value, making it optional in function calls.

def complicated_func(x, y, z=None):  
    # 'z=None' sets 'z' as an optional parameter
    print(x, y, z)

complicated_func(10, 20)  
# Output: 10 20 None


# 3. Using *args
# '*args' allows passing any number of positional arguments as a tuple.

def func_with_args(*args):
    print(args)

func_with_args(1, 2, 3, 4, 5)
# Output: (1, 2, 3, 4, 5)


# 4. Using **kwargs
# '**kwargs' allows passing any number of keyword arguments as a dictionary.

def func_with_kwargs(**kwargs):
    print(kwargs)

func_with_kwargs(name='Alice', age=25, city='New York')
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}


# 5. Using both *args and **kwargs
# This makes the function highly flexible, accepting both positional and keyword arguments.

def func1(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

func1(1, 2, 3, True, name='Bob', age=32)
# Output:
# Positional arguments: (1, 2, 3, True)
# Keyword arguments: {'name': 'Bob', 'age': 32}


# 6. Unpacking arguments from a list and a dictionary
# Using * to unpack a list into positional arguments
# Using ** to unpack a dictionary into keyword arguments

def func2(a, b, c, d=False, e=False):
    print(a, b, c, d, e)

func2(*[1, 2, 3], **{'d': 'hello', 'e': 'world'})
# *[1, 2, 3] unpacks the list into positional arguments (a=1, b=2, c=3)
# **{'d': 'hello', 'e': 'world'} unpacks the dictionary into keyword arguments (d='hello', e='world')
# Output: 1 2 3 hello world
