class InventoryItem:
    """A class to demonstrate operator overloading for inventory management."""
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f'InventoryItem(name="{self.name}", quantity={self.quantity})'

    # Arithmetic Operators
    def __add__(self, other):  # +
        # Make sure its safe to perform the operation
        if isinstance(other, InventoryItem) and self.name == other.name:
            # Then return a new InventoryItem with the quantity added
            return InventoryItem(self.name, self.quantity + other.quantity)
        raise ValueError('Cannot add items of different types.')

    def __sub__(self, other):  # -
        if isinstance(other, InventoryItem) and self.name == other.name:
            if self.quantity >= other.quantity:
                return InventoryItem(self.name, self.quantity - other.quantity)
            raise ValueError('Cannot subtract more than the avaliable quantity.')
        raise ValueError('Cannot subtract items of different types.')

    def __mul__(self, factor):  # *
        if isinstance(factor, (int, float)):
            return InventoryItem(self.name, int(self.quantity * factor))
        raise ValueError('Multiplication factor must be a number.')

    def __truediv__(self, factor):  # /
        if isinstance(factor, (int, float)) and factor != 0:
            return InventoryItem(self.name, int(self.quantity / factor))
        return ValueError('Division factor mus be a non-zero number.')

    # Comparison Operators
    def __eq__(self, other):  # ===
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.quantity == other.quantity
        return False

    def __ne__(self, other):  # !=
        if isinstance(other, InventoryItem):
            return self.name != other.name and self.quantity != other.quantity
        return False

    def __lt__(self, other):  # <
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity < other.quantity
        raise ValueError('Cannot compare items of different types.')

    def __gt__(self, other):  # >
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity > other.quantity
        raise ValueError('Cannot compare items of different types.')

    # There are more operators like "!=", "<=" or "=>"

# Create some inventory items
item1 = InventoryItem('Apple', 50)
item2 = InventoryItem('Apple', 30)
item3 = InventoryItem('Orange', 20)

# Adding quantities of the same item
result_add = item1 + item2
print(result_add)  # Output: InventoryItem(name="Apple", quantity=80)

# Subtracting quantities of the same item
result_sub = item1 - item2
print(result_sub)  # Output: InventoryItem(name="Apple", quantity=20)

# Multiplying item quantities by a factor
result_mul = item1 * 2
print(result_mul)  # Output: InventoryItem(name="Apple", quantity=100)

# Comparing item quantities
print(item1 > item2)  # Output: True
print(item1 == InventoryItem("Apple", 50))  # Output: True

# Trying to add items of different types
try:
    result_invalid = item1 + item3
except ValueError as e:
    print(e)  # Output: Cannot add items of different types.

# Trying to subtract more than avaliable quantity
try:
    result_invalid = item2 - item1
except ValueError as e:
    print(e)  # Output: Cannot subtract more than the avaliable quantity.
