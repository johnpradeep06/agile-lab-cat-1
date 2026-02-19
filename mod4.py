# module4.py
import module2
import module3

def run_system_analysis(radii_list, inventory_items):
    print("=== STARTING INTEGRATED SYSTEM ===\n")

    # 1. Integrate Circle Calculations (Mod 2) and Reporting (Mod 3)
    print("--- Circle Analysis Section ---")
    for r in radii_list:
        # Calculate using Module 2
        area, circum = module2.get_circle_details(r)
        
        # Format using Module 3
        report = module3.format_circle_report(r, area, circum)
        print(report)

    # 2. Integrate Logistics Calculations (Mod 2) and Summaries (Mod 3)
    print("\n--- Logistics Section ---")
    # Calculate using Module 2
    count, root = module2.calculate_logistics(inventory_items)
    
    # Format using Module 3
    summary = module3.generate_logistics_summary(count, root)
    print(summary)
    
    print("\n=== SYSTEM ANALYSIS COMPLETE ===")

if __name__ == "__main__":
    # Sample data for integration
    sample_radii = [3, 7, 10]
    sample_items = ["Widget A", "Widget B", "Widget C", "Widget D"]
    
    # Run the integrated workflow
    run_system_analysis(sample_radii, sample_items)
