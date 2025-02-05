# Define a simple class called 'Foo'
class Foo:
    def show(self):  # 'show' method of the 'Foo' class
        print('Hi!')

# Define a function that will be used as a method for the 'Test' class
def add_attribute(self):  # Function that adds the 'z' attribute to the object
    self.z = 9

# Here, we are dynamically creating a new class called 'Test',
# which inherits from 'Foo', and adds an attribute 'x' and a method 'add_attribute'.
Test = type('Test', (Foo,), {'x': 5, 'add_attribute': add_attribute})

# Create an instance of 'Test'
t = Test()

# Call the 'add_attribute' method to add the 'z' attribute to the instance
t.add_attribute()

# Print the 'z' attribute that was added by the method
print(t.z)
