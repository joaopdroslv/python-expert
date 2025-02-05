# Define a custom metaclass 'Meta' that inherits from 'type'
class Meta(type):
    # The __new__ method is called when a new class is created using this metaclass
    def __new__(cls, class_name, bases, attributes):
        print("Original attributes:", attributes)

        # Create a new dictionary to store the modified attributes
        modified_attributes = {}

        # Iterate over the attributes to make changes
        for name, val in attributes.items():
            # If the attribute name starts with '__', keep it as is (for special methods)
            if name.startswith('__'):
                modified_attributes[name] = val
            else:
                # Convert other attribute names to uppercase
                modified_attributes[name.upper()] = val

        print("Modified attributes:", modified_attributes)

        # Return the new class with the modified attributes
        return super().__new__(cls, class_name, bases, modified_attributes)


# Define a class 'Dog' that uses the 'Meta' metaclass
class Dog(metaclass=Meta):
    name = 'Rex'  # Instance variable 'name'
    age = 3       # Instance variable 'age'

    def bark(self):  # Instance method 'bark'
        print('Whoof!')

# Create an instance of the 'Dog' class
dog = Dog()

# Access the attributes with modified names (uppercased) using the custom metaclass
print(dog.NAME)  # Output: Rex
print(dog.AGE)   # Output: 3

# Call the 'bark' method on the 'Dog' instance
dog.BARK()       # Output: Whoof!
