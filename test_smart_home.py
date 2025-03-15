from smart_devices import SmartPlug, SmartOven, SmartHeater
from smart_home import SmartHome

def test_smart_home():
    """
    Test the functionality of the SmartHome class.
    
    This function tests:
    1. Adding devices to SmartHome
    2. Retrieving devices by index
    3. Toggling individual devices
    4. Switching all devices on/off
    5. Removing devices
    6. Updating device options
    7. Handling invalid operations
    """
    print("\n=== Testing SmartHome Class ===")
    
    # Create devices
    print("\nCreating devices:")
    plug = SmartPlug(45)
    oven = SmartOven()
    heater = SmartHeater()
    print(f"Created: {plug}")
    print(f"Created: {oven}")
    print(f"Created: {heater}")
    
    # Create SmartHome and add devices
    print("\nCreating SmartHome and adding devices:")
    home = SmartHome()
    home.add_device(plug)
    home.add_device(oven)
    home.add_device(heater)
    print(home)
    
    # Test get_device
    print("\nTesting get_device():")
    retrieved_plug = home.get_device(0)
    retrieved_oven = home.get_device(1)
    retrieved_heater = home.get_device(2)
    print(f"Device at index 0: {retrieved_plug}")
    print(f"Device at index 1: {retrieved_oven}")
    print(f"Device at index 2: {retrieved_heater}")
    
    # Test toggle_device
    print("\nTesting toggle_device():")
    print("Toggling device at index 0:")
    home.toggle_device(0)
    print("Toggling device at index 1:")
    home.toggle_device(1)
    print(home)
    
    # Test switch_all_on
    print("\nTesting switch_all_on():")
    home.switch_all_on()
    print(home)
    
    # Test switch_all_off
    print("\nTesting switch_all_off():")
    home.switch_all_off()
    print(home)
    
    # Test update_option
    print("\nTesting update_option():")
    print("Updating consumption_rate of device at index 0 to 100:")
    home.update_option(0, 100)
    print("Updating temperature of device at index 1 to 200:")
    home.update_option(1, 200)
    print("Updating setting of device at index 2 to 4:")
    home.update_option(2, 4)
    print(home)
    
    # Test invalid update_option
    print("\nTesting invalid update_option():")
    try:
        print("Attempting to update consumption_rate to 200:")
        home.update_option(0, 200)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    try:
        print("\nAttempting to update temperature to 300:")
        home.update_option(1, 300)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    try:
        print("\nAttempting to update setting to 6:")
        home.update_option(2, 6)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print(home)  # Should be unchanged
    
    # Test remove_device
    print("\nTesting remove_device():")
    print("Removing device at index 1:")
    home.remove_device(1)
    print(home)
    
    # Test invalid remove_device
    print("\nTesting invalid remove_device():")
    try:
        print("Attempting to remove device at index 10:")
        home.remove_device(10)
    except IndexError as e:
        print(f"Error caught: {e}")
    
    # Test max_items limit
    print("\nTesting max_items limit:")
    small_home = SmartHome(max_items=2)
    small_home.add_device(SmartPlug(50))
    small_home.add_device(SmartOven(180))
    print(small_home)
    
    try:
        print("\nAttempting to add a third device:")
        small_home.add_device(SmartHeater())
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print("\nSmartHome testing completed successfully.")

if __name__ == "__main__":
    test_smart_home() 