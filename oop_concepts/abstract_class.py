# Abstract class is a class that cannot be instantiated on its own
# It is meant to be subclassed, meaning you can't create objects directly from it.
# Abstract classes can contain abstract methods, which are methods that are declared 
# but have no implementation in the abstract class itself.
#   1. Prevents instantiation of the class itself (you can't create an object of the base class).
#   2. Forces subclasses to provide implementations for the abstract methods.

# Importing the abstract base class and the decorator for abstract methods
from abc import ABC, abstractmethod  


# The Vehicle class is an abstract class that inherits from ABC (Abstract Base Class)
# It has two abstract methods: go() and stop()
# Any subclass of Vehicle must provide implementations for these methods.
class Vehicle(ABC):  
    @abstractmethod  # Declares the method go() as abstract
    def go(self):  
        pass  # The method doesn't have an implementation in the base class.

    @abstractmethod  # Declares the method stop() as abstract
    def stop(self):
        pass  # The method doesn't have an implementation in the base class.


# The Car class inherits from Vehicle and provides concrete implementations
# for the abstract methods go() and stop().
class Car(Vehicle):
    # It must implement all abstract methods from Vehicle
    def go(self):  # Concrete implementation of go for the Car class
        print('You are driving the car.')

    def stop(self):  # Concrete implementation of stop for the Car class
        print('You stopped the car.')


# The Motorcycle class inherits from Vehicle and provides concrete implementations
# for the abstract methods go() and stop().
class Motorcycle(Vehicle):
    # It must implement all abstract methods from Vehicle
    def go(self):  # Concrete implementation of go for the Motorcycle class
        print('You are driving the motorcycle.')

    def stop(self):  # Concrete implementation of stop for the Motorcycle class
        print('You stopped the motorcycle.')


# vehicle = Vehicle()  # This will raise an error because 
# you can't instantiate an abstract class.
# You can only instantiate concrete subclasses like Car or Motorcycle.

# Now we can instantiate the subclasses, which have provided 
# concrete implementations of go and stop.
car = Car()
car.go()
car.stop()

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()
