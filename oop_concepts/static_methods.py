# Static methods are functions that belong to a class 
# but do not have access to instance data.
# They are typically used for utility functions that do 
# not need to modify or interact with instance attributes.

# Instance methods are best suited for operations that depend on the 
# specific state of an instance of the class.
# Static methods are used for operations that are general and 
# do not require access to instance data.

class Employee:
    """Represents an employee in a company."""
    
    def __init__(self, name, position):
        """Initialize employee with name and position."""
        self.name = name
        self.position = position

    def info(self):
        """Return employee's information in a formatted string."""
        return f'[{self.position}] {self.name}'  # Returns a string with the employee's name and position

    @staticmethod
    def is_valid_position(position):
        """Check if a given position is valid within the company."""
        # List of valid positions in the company
        valid_positions = ['Manager', 'Cook', 'Cashier', 'Janitor']  
        return position in valid_positions  # Returns True if the position is valid, otherwise False


# Create employee instances
employee1 = Employee('Walter', 'Manager')
employee2 = Employee('Bob', 'Cook')
employee3 = Employee('Hernandez', 'Cashier')
employee4 = Employee('Camilla', 'Janitor')

# Use instance methods to get information about employees
print(employee1.info())
print(employee2.info())
print(employee3.info())
print(employee4.info())

# Use static methods directly from the class, without needing an instance

print(Employee.is_valid_position('Cook'))  
# Output: True, because 'Cook' is a valid position in the company

print(Employee.is_valid_position('Scientist'))  
# Output: False, because 'Scientist' is not a valid position in the company
