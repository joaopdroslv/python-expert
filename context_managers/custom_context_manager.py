class File:
    def __init__(self, filename, mode):
        """Initialize the File object and open the file."""
        self.file = open(filename, mode)

    def __enter__(self):
        """Called when entering the context. Returns the file object."""
        print('Entering context')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Called when exiting the context.  

        If an exception occurs, its type, value, and traceback are passed to this method.
        The method ensures the file is closed and can handle exceptions if needed.
        """
        print(f'Exception details: {exc_type}, {exc_value}, {traceback}')
        print('Exiting context')
        self.file.close()

        # Returning True suppresses any exception that occurred inside the context block.
        return True  


# Using the File class as a context manager
with File('file.txt', 'w') as file:
    # The __enter__ method is called before this block executes.
    print('Inside context block')
    file.write('Hello, world!')

    # If an exception occurs here, __exit__ will handle it.
    # raise Exception("Something went wrong")
