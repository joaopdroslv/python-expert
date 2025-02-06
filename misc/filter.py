# Function that checks if the string length is greater than 6
def longer_than_6(string):  
    return len(string) > 6


strings = ['apple', 'banana', 'coconut', 'orange']

# Using filter to apply the 'longer_than_6' function to each item in the list
filtered = filter(longer_than_6, strings)
print(list(filtered))  # Output: ['coconut']  
# The 'filter' function filters out items for which the function returns False

# Doing the same thing using a lambda function
filtered = filter(lambda item: len(item) > 6, strings)
print(list(filtered))  # Output: ['coconut']
# The lambda function is used for the same filtering condition
