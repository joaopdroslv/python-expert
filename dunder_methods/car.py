class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # __str__ is meant for user-friendly output
    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    # __repr__ is meant for a more detailed, unambiguous output
    def __repr__(self):
        return f'Car(make="{self.make}", model="{self.model}", year="{self.year}")'


my_car = Car('Toyota', 'Corolla', 2025)

print(str(my_car))      # User-friendly
print(repr(my_car))     # Developer-friendly
