class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self._width = width  # Private attribute for width
        self._height = height  # Private attribute for height

    @property
    def width(self):
        """Getter method for width, formatted as a string with one decimal place."""
        return f'{self._width:.1f} cm'  # Returns width in cm with one decimal

    @property
    def height(self):
        """Getter method for height, formatted as a string with one decimal place."""
        return f'{self._height:.1f} cm'  # Returns height in cm with one decimal

    @width.setter
    def width(self, new_width):
        """Setter method for width, ensuring the value is positive."""
        if new_width > 0:
            self._width = new_width  # Assign new width if it's valid
        else:
            print('Width must be greater than zero.')  # Output if the value is invalid

    @height.setter
    def height(self, new_height):
        """Setter method for height, ensuring the value is positive."""
        if new_height > 0:
            self._height = new_height  # Assign new height if it's valid
        else:
            print('Height must be greater than zero.')  # Output if the value is invalid

    @width.deleter
    def width(self):
        """Delete the width attribute."""
        del self._width  # Deletes the width attribute
        print('Width has been deleted.')  # Notify that width has been deleted

    @height.deleter
    def height(self):
        """Delete the height attribute."""
        del self._height  # Deletes the height attribute
        print('Height has been deleted.')  # Notify that height has been deleted


# Test the Rectangle class
rectangle = Rectangle(20, 5)

# Calling the setter methods
rectangle.width = 0  # This will print: "Width must be greater than zero."
rectangle.height = 10  # No output because 10 is a valid height

# Accessing the properties (getting the values)
print(rectangle.width)  # Output: 20.0 cm (formatted width)
print(rectangle.height)  # Output: 10.0 cm (formatted height)

# Calling the deleter methods
del rectangle.width  # This will print: "Width has been deleted."
del rectangle.height  # This will print: "Height has been deleted."
