# Define a decorator function that takes another function 'f' as an argument
def func(f):
    # The wrapper function will be executed instead of the original function 'f'
    # It accepts any number of arguments and keyword arguments
    def wrapper(*args, **kwargs):
        print('Started')  # Code to run before the function call
        returned_value = f(*args, **kwargs)  # Call the original function with the arguments
        print('Ended')  # Code to run after the function call
        return returned_value  # Return the result of the original function
    
    # Return the wrapped version of the function
    return wrapper


# Common way to apply the decorator: using the '@' syntax
@func  # This is equivalent to: func2 = func(func2)
def func2():
    print('I’m func2')


# The following code would cause an error because func2 does not take any arguments
# While the decorator `func` expects the wrapped function to handle any number of arguments.
# So we should modify the decorator to work for functions with arguments.

# To solve the issue of passing arguments to the decorator, we modify the wrapper function 
# to accept *args (any number of positional arguments) and **kwargs (any number of keyword arguments).

# Correct decorator that can handle functions with arguments
@func
def func3(x):  
    print(x)  # Print the argument passed to the function


@func
def func4(x):  
    print(x)  # Print the argument passed to the function
    return 'Done'  # Return a value

# Another way to apply the decorator manually, without using '@' syntax:
# func2 = func(func2)
# func2()  # This would call the wrapped func2()

# Call func4 with an argument, demonstrating how the decorator works
func4(10)  # Prints 'Started', the value '10', and 'Ended'
