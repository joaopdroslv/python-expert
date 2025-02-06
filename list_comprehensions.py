x = [i for i in range(4)]  # Simplest list comprehension possible
print(x)  # Ouput: [0, 1, 2, 3]

# Nested list comprehension
x = [[j for j in range(6)] for i in range(3)]
print(x)  # Output: [[], [], []]

# Applying conditions
evens = [i for i in range(10) if i % 2 == 0]
print(evens)
