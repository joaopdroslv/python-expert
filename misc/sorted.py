# Simple sorting example:
numbers = [4, 5, 2, 3, -1, 9, 0]
# sorted() returns a new list that is sorted, it does not modify the original list
sorted_nums = sorted(numbers)
print(sorted_nums)  # Output: [-1, 0, 2, 3, 4, 5, 9]


# More complex example of sorting using the 'key' parameter
people = [
    {'name': 'Kate', 'age': 54},
    {'name': 'Bob', 'age': 27},
    {'name': 'Michael', 'age': 31},
    {'name': 'Alice', 'age': 15},
]
# The 'key' parameter specifies a function to be applied to each item before sorting
# In this case, we're sorting based on the 'age' key of each dictionary
sorted_people = sorted(people, key=lambda person: person['age'])
print(sorted_people)
# Output: [{'name': 'Alice', 'age': 15}, {'name': 'Bob', 'age': 27}, {'name': 'Michael', 'age': 31}, {'name': 'Kate', 'age': 54}]
