# module3.py - Presentation & Formatting Module
from datetime import datetime

def create_styled_header(title):
    """Creates a decorative header for console reports."""
    line = "=" * 40
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"\n{line}\n{title.upper()}\nGenerated: {now}\n{line}"

def format_item_list(label, items):
    """Formats a list of items into a bulleted string."""
    formatted_string = f"{label}:\n"
    for idx, item in enumerate(items, 1):
        formatted_string += f"  {idx}. Value: {item}\n"
    return formatted_string

def generate_footer(status_code="SUCCESS"):
    """Creates a system footer with status messages."""
    return f"{'-' * 40}\nSystem Status: {status_code}\nEnd of Report\n"

def log_event(event_type, message):
    """Logs system events to the console with custom formatting."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{event_type}] {message}")

# Module 3 ensures that all numeric data is digestible by the end user.
# It serves as the UI layer for this terminal-based application.
