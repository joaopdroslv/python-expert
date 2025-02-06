# Class methods allow operations that are related 
# to the class itself rather than instances of the class.
# They are defined with @classmethod and take 'cls' 
# as the first parameter, representing the class itself.

class Student:
    count = 0  # Class variable to keep track of total students
    total_gpa = 0  # Class variable to keep track of the sum of all GPA values

    def __init__(self, name, gpa):
        """Initialize the student with a name and GPA, and update class variables."""
        self.name = name
        self.gpa = gpa

        Student.count += 1  # Increment the student count every time a new instance is created
        Student.total_gpa += gpa  # Add this student's GPA to the running total GPA

    def info(self):
        """Return a string with the student's name and GPA."""
        return f'{self.name} {self.gpa}'  # Return a formatted string of student's name and GPA

    @classmethod
    def get_count(cls):
        """Return the total number of students."""
        return f'Total number of students: {cls.count}'  # Return the total count of students

    @classmethod
    def get_average_gpa(cls):
        """Return the average GPA of all students, or 0 if no students exist."""
        if cls.count == 0:
            return 0
        return f'Average GPA is: {cls.total_gpa / cls.count:.2f}'


# Creating student instances
student1 = Student('Patrick', 3.2)
student2 = Student('Eugene', 7)
student3 = Student('Amy', 9.9)

# Calling class methods using the class itself, not instances
print(Student.get_count())  # Output the total number of students
print(Student.get_average_gpa())  # Output the average GPA of all students
