# The super() function allows a child class to call methods 
# from a parent class (superclass).
# It enables extending and reusing the functionality of inherited methods.

class Shape:
    """Base class representing a geometric shape."""
    
    def __init__(self, color, is_filled):
        """Initialize the shape with a color and filled status."""
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        """Describe the shape's color and whether it's filled."""
        print(f'It is {self.color} and it is {"filled" if self.is_filled else "not filled"}.')


class Circle(Shape):
    """Represents a circle, inheriting from Shape."""
    
    def __init__(self, color, is_filled, radius):
        """Initialize the circle with a color, filled status, and radius."""
        # Call the parent class (Shape) constructor to set color and filled status
        super().__init__(color, is_filled)  
        self.radius = radius

    def describe(self):
        """Extend the description to include the circle's area."""
        # Call the parent class's describe method to print the color and filled status
        super().describe()  
        print(f'It is a circle with an area of {3.14 * self.radius ** 2:.2f} cm².')  


class Square(Shape):
    """Represents a square, inheriting from Shape."""
    
    def __init__(self, color, is_filled, width):
        """Initialize the square with a color, filled status, and width."""
        super().__init__(color, is_filled)  # Call the parent class constructor
        self.width = width

    def describe(self):
        """Extend the description to include the square's area."""
        super().describe()  # Call the parent class's describe method
        print(f'It is a square with an area of {self.width ** 2} cm².')


class Triangle(Shape):
    """Represents a triangle, inheriting from Shape."""
    
    def __init__(self, color, is_filled, width, height):
        """Initialize the triangle with a color, filled status, width, and height."""
        super().__init__(color, is_filled)  # Call the parent class constructor
        self.width = width
        self.height = height

    def describe(self):
        """Extend the description to include the triangle's area."""
        super().describe()  # Call the parent class's describe method
        print(f'It is a triangle with an area of {self.width * self.height / 2:.2f} cm².')


# Creating and describing different shapes
circle = Circle(color='Red', is_filled=True, radius=10)
square = Square(color='Green', is_filled=True, width=10)
triangle = Triangle(color='Blue', is_filled=False, width=10, height=5)

print("\nCircle Details:")
circle.describe()  # Calling describe method of Circle

print("\nSquare Details:")
square.describe()  # Calling describe method of Square

print("\nTriangle Details:")
triangle.describe()  # Calling describe method of Triangle
