# Function to get the 'n' largest numbers from a list
def get_largest_numbers(numbers, n):
    numbers.sort()  # This modifies the original list because lists are mutable
    return numbers[-n:]  # Returns the last 'n' elements, which are the largest after sorting

# Creating a list (which is a mutable type)
nums = [2, 3, 4, 34, 123, 321, 1]

print("Original list:", nums)
largest = get_largest_numbers(nums, 2)  # This function modifies 'nums' because of 'sort()'
print("Modified list after function call:", nums)  # Notice that 'nums' is now sorted
print("Largest numbers:", largest)


# --- Demonstrating Mutability and Immutability ---


# Example with a mutable type (list)
print('\nMutable (list)')
mutable_list = [10, 20, 30]
print("Before modification:", mutable_list)
mutable_list.append(40)  # Modifies the original list
print("After modification:", mutable_list)


# Example with an immutable type (tuple)
print('\nImmutable (tuple)')
immutable_tuple = (10, 20, 30)
print("Before attempting modification:", immutable_tuple)
# immutable_tuple[0] = 100  # This would raise an error because tuples are immutable


# Example with an immutable type (string)
print('\nImmutable (string)')
immutable_string = "hello"
print("Before attempting modification:", immutable_string)
new_string = immutable_string.upper()  # This creates a new string instead of modifying the original
print("After calling upper():", new_string)
print("Original string remains unchanged:", immutable_string)


# Example of unexpected behavior with function arguments
def modify_list(lst):
    lst.append(100)  # This modifies the original list
    print("Inside function:", lst)

my_list = [1, 2, 3]
print('\nBehavior with function arguments')
print("Before function call:", my_list)
modify_list(my_list)
print("After function call:", my_list)  # The list is changed because lists are mutable


# Example of preventing modification by passing a copy
def safe_modify_list(lst):
    lst = lst[:]  # Creates a shallow copy
    lst.append(200)
    print("Inside function with copy:", lst)

print('\nPreventing modification by passing a copy')
print("Before safe function call:", my_list)
safe_modify_list(my_list)
print("After safe function call:", my_list)  # Original list remains unchanged
