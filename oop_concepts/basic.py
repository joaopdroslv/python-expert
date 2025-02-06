class Car:
    """Represents a car with basic attributes and behaviors."""
    
    def __init__(self, model, year, color, for_sale):
        """Initialize the car with model, year, color, and sale status."""
        # The __init__ constructor initializes the car instance with the given values.
        # Attributes:
        # model: The model of the car (e.g., 'Toyota Camry')
        # year: The year of the car (e.g., 2024)
        # color: The color of the car (e.g., 'Red')
        # for_sale: Indicates if the car is for sale (True or False)
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        """Simulate driving the car."""
        print(f'You are driving the {self.model}.')

    def stop(self):
        """Simulate stopping the car."""
        print(f'You stopped the {self.model}.')

    def describe(self):
        """Display a description of the car."""
        print(f'{self.year} {self.color} {self.model}')


# Creating car instances
car1 = Car('Toyota Camry', 2024, 'Red', True)
car2 = Car('Mustang', 2024, 'Black', True)

# Accessing attributes of car1
# Each attribute can be accessed directly using the attribute name.
print(f'Model: {car1.model}')
print(f'Year: {car1.year}')
print(f'Color: {car1.color}')
print(f'For sale: {car1.for_sale}')

# Using methods of car2
# Calling the methods drive, stop, and describe for car2.
car2.drive()
car2.stop()
car2.describe()
