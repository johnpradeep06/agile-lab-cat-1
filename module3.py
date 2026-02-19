# module3.py

def format_circle_report(radius, area, circumference):
    """Formats circle data into a readable string."""
    return (f"Circle Report (Radius: {radius}):\n"
            f" - Area: {area}\n"
            f" - Circumference: {circumference}\n"
            f"{'-' * 30}")

def generate_logistics_summary(total_items, root_val):
    """Formats the logistics math into a summary."""
    return f"Logistics Update: Processing {total_items} items (Grid Size: {root_val}x{root_val})"
