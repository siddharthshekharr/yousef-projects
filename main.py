import tkinter as tk
from smart_homes_app import SmartHomesApp
from smart_home_app import SmartHomeApp
from test_smart_devices import test_smart_plug, test_custom_device
from test_smart_home import test_smart_home

def run_tests():
    """Run all test functions."""
    print("Running tests...")
    test_smart_plug()
    test_custom_device()
    test_smart_home()
    print("\nAll tests completed successfully.")

def run_smart_home_app():
    """Run the SmartHomeApp (single home)."""
    root = tk.Tk()
    app = SmartHomeApp(root)
    root.mainloop()

def run_smart_homes_app():
    """Run the SmartHomesApp (multiple homes)."""
    root = tk.Tk()
    app = SmartHomesApp(root)
    root.mainloop()

if __name__ == "__main__":
    print("Python Smart Home System")
    print("1. Run tests")
    print("2. Run Smart Home App (single home)")
    print("3. Run Smart Homes App (multiple homes)")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        run_tests()
    elif choice == "2":
        run_smart_home_app()
    elif choice == "3":
        run_smart_homes_app()
    else:
        print("Invalid choice. Exiting.") 