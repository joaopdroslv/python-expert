# Dunder (Magic) Methods in Python

# Everything in Python is an object, including functions
def func():
    pass

print(type(func))  # Output: <class 'function'>

str1 = 'Hello, '
str2 = 'world'

# The + operator internally calls a dunder method (__add__)
# Strings in Python are objects, and their behavior is defined by a class
new_str1 = str1 + str2  
print(new_str1)  # Output: Hello, world

# Another way to achieve the same result:
new_str2 = str1.__add__(str2)  # Directly calling the __add__ dunder method

# The __len__() method returns the length of the string
# It's equivalent to calling len(new_str2)
print(new_str2.__len__())  