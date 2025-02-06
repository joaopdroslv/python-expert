# In composition, the composed object directly owns its components, 
# which cannot exist independently.
# It's an "owns-a" relationship, meaning the lifecycle of 
# the parts depends on the whole.

class Engine:
    """Represents the engine of a car."""
    
    def __init__(self, horse_power):
        """Initialize the engine with a specific horsepower."""
        self.horse_power = horse_power


class Wheel:
    """Represents a wheel of a car."""
    
    def __init__(self, size):
        """Initialize the wheel with a specific size."""
        self.size = size


class Car:
    """Represents a car, composed of an engine and wheels."""
    
    def __init__(self, make, model, horse_power, wheel_size):
        """Initialize the car with a make, model, engine, and wheels."""
        self.make = make
        self.model = model
        # Every car owns an Engine (composition)
        self.engine = Engine(horse_power)
        # Every car owns four wheels (composition)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]

    def describe(self):
        """Describe the car's make, model, engine, and wheel size."""
        return f'{self.make} {self.model}, {self.engine.horse_power} (hp) engine and {self.wheels[0].size} (inches) wheels.'


# Create car instances with specific properties
car1 = Car(make='Honda', model='Civic', horse_power=818, wheel_size=18)
print(car1.describe())

car2 = Car(make='Ford', model='Mustang', horse_power=500, wheel_size=18)
print(car2.describe())
