class Countdown:
    """A simple iterator that counts down from a given number."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """Returns the next value in te countdown."""
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration


for number in Countdown(5):
    print(number)


# __iter__(Coundown(5)) -> Countdown(5)
# __next__(Countdown(5)) -> 5
# __next__(Countdown(5)) -> 4
# __next__(Countdown(5)) -> 3
# __next__(Countdown(5)) -> 2
# __next__(Countdown(5)) -> 1
# __next__(Countdown(5)) -> raise StopIteration
