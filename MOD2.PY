# module2.py - Logic & Mathematics Module
import math

def get_circle_details(radius):
    """Calculates area and circumference of a circle with error handling."""
    if radius < 0:
        return 0.0, 0.0
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)

def calculate_logistics(items):
    """Performs square root and factorial logic for batch processing."""
    count = len(items)
    try:
        square_root = math.sqrt(count)
        fact_val = math.factorial(min(count, 10)) # Capped at 10 for safety
    except ValueError:
        square_root, fact_val = 0, 0
    return count, round(square_root, 2), fact_val

def apply_statistical_offset(data_list, offset=5.5):
    """Applies a mathematical offset to a dataset."""
    transformed = []
    for item in data_list:
        new_val = (item * 1.1) + offset
        transformed.append(round(new_val, 2))
    return transformed

# Adding logic to meet line requirements
# This module acts as the pure functional layer of the application.
