def gen(n):
    """Generator function that yields the square of numbers from 0 to n-1."""
    for i in range(n):
        # The function runs until it encounters 'yield'
        # At this point, it pauses and returns the current value
        yield i**2

        # Execution resumes from this point when 'next()' is called again

    # A generator can have multiple 'yield' statements, for example:
    # yield 1
    # yield 10
    # yield 100
    # The generator continues running until there are no more 'yield' statements,
    # at which point it raises StopIteration and stops.


# Creating a generator instance
g = gen(10)

# Iterating over the generator
for i in g:
    print(i)

    # The next iteration of the loop calls the generator again, resuming execution


# Creating a new generator instance
g2 = gen(10)

# Another way to get values from a generator is by calling 'next()' manually
print(next(g2))  # Retrieves the first value (0**2)
print(next(g2))  # Retrieves the second value (1**2)
print(next(g2))  # Retrieves the third value (2**2)
print(next(g2))  # Retrieves the fourth value (3**2)

# If we keep calling 'next(g2)', it will continue yielding values
# until 'n' is reached, at which point it raises StopIteration.
