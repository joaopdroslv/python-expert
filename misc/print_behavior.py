name = 'Bob'
age = '20'

# Changing the separator between printed values
print('My name is', name, "I'm", age, 'years old.', sep=' ')
# The 'sep' parameter defines the separator between values
# It can be replaced with anything like '-', '|', '/', etc.

# Changing the ending of the print statement
print("You look beautiful today", end=f' - Said {name}.')  
# By default, print() adds a newline character '\n' at the end
# The 'end' parameter allows us to change this behavior
# We can replace '\n' with any string we want
