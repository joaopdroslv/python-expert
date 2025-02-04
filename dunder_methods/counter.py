class Counter:
    def __init__(self):
        self.value = 1

    def count_up(self):
        self.value += 1

    def count_down(self):
        self.value -= 1

    # When attempting to print the object, this method is called to return its string representation
    def __str__(self):
        return f'Count={self.value}'

    # When using the + operator, Python calls the __add__ dunder method on the left operand
    # The right operand is passed as the "other" parameter
    def __add__(self, other):
        if isinstance(other, Counter):
            return self.value + other.value
        raise Exception('Invalid type.')  # Raises an exception for unsupported types


count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_up()

print(count1, count2)  # Output: Count=2 Count=2
print(count1 + count2)  # Output: 4
print(count1 + 2)  # Raises 'Invalid type' exception