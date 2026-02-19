import math

def get_circle_details(radius):
    """Calculates area and circumference of a circle."""
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)

def calculate_logistics(items):
    """Simple math logic for splitting items."""
    count = len(items)
    square_root = math.sqrt(count)
    return count, round(square_root, 2)

# Demonstration block
if __name__ == "__main__":
    a, c = get_circle_details(5)
    print(f"Sample Circle - Area: {a}, Circumference: {c}")
    print(f"Square root of 100 is: {math.isqrt(100)}")
    print(f"Factorial of 4 is: {math.factorial(4)}")
    print("Math module loaded successfully.")
