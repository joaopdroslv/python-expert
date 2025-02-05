def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

    return Dog  # Where returning the class itself, not a instance


cls = make_class(10)
print(cls)

# Python compiler don't check if this is valid or not
# it just read from the top to the bottom

dog = cls('Rex')
print(dog.name)

dog.print_value()
