# 1. Simplest list comprehension possible
# Generates a list containing numbers from 0 to 3
x = [i for i in range(4)]  
print(x)  # Output: [0, 1, 2, 3]

# 2. Nested list comprehension
# Creates a list of lists where each sublist contains numbers from 0 to 5
x = [[j for j in range(6)] for i in range(3)]
print(x)  # Output: [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]

# 3. Using if condition
# Filters only even numbers from 0 to 9
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# 4. Using if-else condition
# Creates a list labeling numbers as "even" or "odd"
labels = ['even' if i % 2 == 0 else 'odd' for i in range(10)]
print(labels)  # Output: ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# 5. Using tuples
# Generates a list of tuples where each tuple contains a number and its square
tuples = [(x, x**2) for x in range(5)]
print(tuples)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# 6. Using zip to combine two lists
# Creates a list of formatted strings combining names and ages
names = ['Alice', 'Bob', 'Charlie']
ages = [20, 30, 40]
info = [f'{name} is {age} years old.' for name, age in zip(names, ages)]
print(info)  # Output: ['Alice is 20 years old.', 'Bob is 30 years old.', 'Charlie is 40 years old.']

# 7. Flattening a nested list
# Converts a list of lists into a single list containing all elements
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8], [9]]
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 8. Using list comprehension to manipulate objects
# Defines a Car class with make, model, and year attributes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creates a list of Car objects
cars = [
    Car('Honda', 'Civic', 2011),
    Car('Toyota', 'Corolla', 2019),
    Car('Ford', 'Mustang', 2024),
    Car('Dodge', 'Hellcat', 2025),
]

# Filters and extracts only the models of cars manufactured in 2020 or later
models = [car.model for car in cars if car.year >= 2020]
print(models)  # Output: ['Mustang', 'Hellcat']
