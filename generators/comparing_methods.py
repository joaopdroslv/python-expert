import sys


def gen(n):
    for i in range(n):
        yield i**2


# Creating a list comprehension that stores all values in memory
x = [i**2 for i in range(100000)]  

# Creating a generator that produces values on demand
g = gen(100000)  

# Measuring memory usage
print('Uses ' + str(sys.getsizeof(x)) + ' bytes')  # Uses 85,176 bytes (stores all values in memory)
print('Uses ' + str(sys.getsizeof(g)) + ' bytes')  # Uses only 104 bytes (stores only the current state)

# The generator is significantly more memory efficient because it does not 
# store all elements in memory at once; it produces them one by one as needed.
