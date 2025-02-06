strings = ['apple', 'banana', 'coconut', 'orange']

# Applying the len() function to every item in the list
lengths = map(len, strings)
print(list(lengths))  # Output: [5, 6, 7, 6]


# Using map with a lambda function to append 's' to each word
new = map(lambda item: item + 's', strings)
print(list(new))  # Output: ['apples', 'bananas', 'coconuts', 'oranges']


# The same operation using a regular function instead of lambda
def add_s(word):
    return word + 's'

new = map(add_s, strings)
print(list(new))  # Output: ['apples', 'bananas', 'coconuts', 'oranges']
