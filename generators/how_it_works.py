# This code will raise a MemoryError because it tries to create a huge list in memory
# x = [i**2 for i in range(100000000000)]
# for el in x:
#     print(el)

# Instead of storing all values in memory, we can use a generator:
# for i in range(100000000000):
#     print(i**2)

# Creating a custom generator class
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0  # Track only the current state

    def __next__(self):
        return self.next()

    def next(self):
        """Generate the next value or raise StopIteration when done."""
        if self.last == self.n:
            raise StopIteration  # Stop when reaching the limit

        rv = self.last ** 2  # Compute the square
        self.last += 1  # Move to the next number
        return rv


g = Gen(10)

while True:
    try:
        print(next(g))
    except StopIteration:
        break
