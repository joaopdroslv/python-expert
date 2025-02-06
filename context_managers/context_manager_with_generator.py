from contextlib import contextmanager


@contextmanager
def file(filename, mode):
    """
    A context manager for handling file operations.

    It ensures the file is properly opened and closed,
    even if an exception occurs within the context block.
    """
    print('Entering context')
    file = open(filename, mode)  # Open the file
    try:
        yield file  # Provide the file object to the context block
    finally:
        file.close()  # Ensure the file is closed after use
        print('Exiting context')


# Using the custom context manager
with file('file.txt', 'w') as f:
    print('Inside context block')
    f.write('Hello, world!')

    # If an exception occurs here, the 'finally' block in the context manager ensures cleanup.
    # Uncomment the next line to test exception handling.
    # raise Exception("Something went wrong")
