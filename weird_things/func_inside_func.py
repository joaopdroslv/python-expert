import inspect


def func(x):
    if x == 1:
        def rv():  # Defining a function inside a function
            print('X is equal to 1')
    else:
        def rv():
            print('X is not 1')

    return rv


new_func = func(1)
new_func()

print(id(new_func))  # Prints the memory ID of the function

print(inspect.getmembers(new_func))  # Prints extra info about the function

print('\n\n')

print(inspect.getsource(new_func))  # Prints the source code of the function
