# Opening a file manually
file = open('file.txt', 'w')  # Opens the file in write mode ('w')

# If an error occurs here, the file may remain open, causing potential resource leaks.
# file.write('Hello, world!')  
# file.close()  # It's necessary to close the file manually.

# Using try-finally to ensure the file is always closed:
try:
    file.write('Hello, world!')  # Writing to the file
finally:
    file.close()  # Ensures the file is closed even if an error occurs

# The above code works exactly the same as this:
with open('file.txt', 'w') as file:  # Opens the file using a context manager
    # Inside this block, we can read, write, or modify the file
    file.write('Hello, world!')  # Writing to the file
# Once the block ends, the file is automatically closed, even if an error occurs.
