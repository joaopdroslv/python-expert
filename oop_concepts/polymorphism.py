# Polymorphism allows objects of different classes to be treated as instances of the same class.
# There are two ways to achieve polymorphism:
#   1. Inheritance: A child class inherits from a parent class and can be used interchangeably.
#   2. 'Duck typing': An object is considered valid as long as it implements the necessary methods.

from abc import ABC, abstractmethod


# Abstract base class for shapes, ensuring that all shapes must implement the area method
class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method to compute the area of a shape."""
        pass  # This is a placeholder method that must be implemented by any subclass


# Circle class that inherits from Shape
class Circle(Shape):
    """Represents a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize the circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return 3.14 * self.radius ** 2  # Area formula: π * radius²


# Square class that inherits from Shape
class Square(Shape):
    """Represents a square, inheriting from Shape."""

    def __init__(self, side):
        """Initialize the square with a given side length."""
        self.side = side

    def area(self):
        """Calculate and return the area of the square."""
        return self.side ** 2  # Area formula: side²


# Triangle class that inherits from Shape
class Triangle(Shape):
    """Represents a triangle, inheriting from Shape."""

    def __init__(self, base, height):
        """Initialize the triangle with a base and height."""
        self.base = base
        self.height = height

    def area(self):
        """Calculate and return the area of the triangle."""
        return (self.base * self.height) / 2  # Area formula: ½ * base * height


# Pizza class that inherits from Circle, extending functionality for a pizza
class Pizza(Circle):
    """Represents a pizza, which is conceptually a circular shape."""

    def __init__(self, topping, radius):
        """Initialize the pizza with a topping and radius."""
        super().__init__(radius)  # Calls the Circle constructor
        self.topping = topping  # Topping is a unique feature for Pizza


# List of different shape objects to demonstrate polymorphism
shapes = [Circle(5), Square(5), Triangle(5, 10), Pizza('Pepperoni', 15)]

# Demonstrating polymorphism: all objects in the list respond to the `area()` method
for shape in shapes:
    # Calls area() for each object, regardless of the class
    print(f'{shape.__class__.__name__} area: {shape.area()} cm²')  
