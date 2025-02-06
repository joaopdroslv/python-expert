# Class variables are shared among all instances of a class.
# They are defined outside the class constructor and allow data sharing
# among all objects created from that class.

class Student:
    """Represents a student with shared class attributes."""

    # Class variables shared among all instances
    class_year = 2025  # This is the graduation year for all students
    num_students = 0  # This will track the total number of students

    def __init__(self, name, age):
        """Initialize an individual student with a name and age."""
        self.name = name
        self.age = age

        # Increment the number of students whenever a new instance is created
        Student.num_students += 1  # Accessing and modifying the class variable


# Creating student instances
student1 = Student('John', 20)
student2 = Student('Emma', 20)
student3 = Student('Emilia', 20)
student4 = Student('Vicky', 20)

# Accessing the shared class variable through instances
print(student1.class_year)  # All instances share the same 'class_year' (2025)
print(student2.class_year)

# Displaying the total number of students
print(f'My graduating class of {Student.class_year} has {Student.num_students} students.')
