# Nested classes are defined within other classes and are 
# typically used to logically group 
# closely related classes, encapsulate private details, and 
# reduce namespace conflicts.

class Company:
    """Represents a company with employees."""

    class Employee:  
        """Represents an employee working at the company."""

        def __init__(self, name, position):
            """Initialize employee with name and position."""
            self.name = name
            self.position = position

        def info(self):
            """Return a formatted string of employee info."""
            return f'[{self.position}] {self.name}'

    def __init__(self, company_name):
        """Initialize company with a name and an empty list of employees."""
        self.company_name = company_name
        self.employees = []  # List to store employees

    def add_employee(self, name, position):
        """Add a new employee to the company."""
        # Create an instance of the nested Employee class and append to the employees list
        new_employee = self.Employee(name, position)  
        self.employees.append(new_employee)

    def list_employees(self):
        """List info of all employees."""
        # List comprehension to get formatted info of each employee in the company
        return [employee.info() for employee in self.employees]


# Create a company instance
company1 = Company('First Company')

# Add employees to the company
company1.add_employee('Kate', 'Manager')
company1.add_employee('John', 'Cook')
company1.add_employee('Michael', 'Janitor')
company1.add_employee('Will', 'Cashier')

for employee in company1.list_employees():
    print(employee)
