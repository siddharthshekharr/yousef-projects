from smart_devices import SmartPlug, SmartOven, SmartHeater

def test_smart_plug():
    """
    Test the functionality of the SmartPlug class.
    
    This function tests:
    1. Initialization with valid consumption rate
    2. Toggle switch functionality
    3. Updating consumption rate with valid value
    4. Toggling switch again
    5. Handling invalid consumption rates
    """
    print("\n=== Testing SmartPlug Class ===")
    
    # Test initialization and initial state
    print("\nTesting initialization with consumption_rate=45:")
    plug = SmartPlug(45)
    print(plug)  # Should be off with rate of 45
    
    # Test toggle_switch method
    print("\nTesting toggle_switch() to turn on:")
    plug.toggle_switch()
    print(plug)  # Should be on with rate of 45
    
    # Test updating consumption_rate
    print("\nTesting updating consumption_rate to 75:")
    plug.consumption_rate = 75
    print(plug)  # Should be on with rate of 75
    
    # Test toggle_switch again
    print("\nTesting toggle_switch() to turn off:")
    plug.toggle_switch()
    print(plug)  # Should be off with rate of 75
    
    # Test invalid consumption_rate values
    print("\nTesting invalid consumption_rate values:")
    
    # Test setting to negative value
    try:
        print("Attempting to set consumption_rate to -10:")
        plug.consumption_rate = -10
    except ValueError as e:
        print(f"Error caught: {e}")
    print(f"Current state: {plug}")  # Should still be off with rate of 75
    
    # Test setting to value > 150
    try:
        print("\nAttempting to set consumption_rate to 200:")
        plug.consumption_rate = 200
    except ValueError as e:
        print(f"Error caught: {e}")
    print(f"Current state: {plug}")  # Should still be off with rate of 75
    
    # Test invalid initialization
    print("\nTesting invalid initialization:")
    
    # Test with negative value
    try:
        print("Attempting to create SmartPlug with consumption_rate=-5:")
        invalid_plug = SmartPlug(-5)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Test with value > 150
    try:
        print("\nAttempting to create SmartPlug with consumption_rate=160:")
        invalid_plug = SmartPlug(160)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print("\nSmartPlug testing completed successfully.")


def test_custom_device():
    """
    Test the functionality of the custom device classes.
    
    This function tests:
    1. Initialization with default values
    2. Toggle switch functionality
    3. Updating option attributes with valid values
    4. Handling invalid option values
    """
    print("\n=== Testing Custom Device Classes ===")
    
    # Test SmartOven
    print("\n--- Testing SmartOven ---")
    
    # Test initialization with default values
    print("\nTesting initialization with default temperature:")
    oven = SmartOven()
    print(oven)  # Should be off with temperature of 150
    
    # Test toggle_switch method
    print("\nTesting toggle_switch() to turn on:")
    oven.toggle_switch()
    print(oven)  # Should be on with temperature of 150
    
    # Test updating temperature
    print("\nTesting updating temperature to 200:")
    oven.temperature = 200
    print(oven)  # Should be on with temperature of 200
    
    # Test invalid temperature values
    print("\nTesting invalid temperature values:")
    
    # Test setting to value < 0
    try:
        print("Attempting to set temperature to -10:")
        oven.temperature = -10
    except ValueError as e:
        print(f"Error caught: {e}")
    print(f"Current state: {oven}")  # Should still be on with temperature of 200
    
    # Test setting to value > 260
    try:
        print("\nAttempting to set temperature to 300:")
        oven.temperature = 300
    except ValueError as e:
        print(f"Error caught: {e}")
    print(f"Current state: {oven}")  # Should still be on with temperature of 200
    
    # Test SmartHeater
    print("\n--- Testing SmartHeater ---")
    
    # Test initialization with default setting
    print("\nTesting initialization with default setting:")
    heater = SmartHeater()
    print(heater)  # Should be off with setting of 2
    
    # Test toggle_switch method
    print("\nTesting toggle_switch() to turn on:")
    heater.toggle_switch()
    print(heater)  # Should be on with setting of 2
    
    # Test updating setting
    print("\nTesting updating setting to 5:")
    heater.setting = 5
    print(heater)  # Should be on with setting of 5
    
    # Test invalid setting values
    print("\nTesting invalid setting values:")
    
    # Test setting to value < 0
    try:
        print("Attempting to set setting to -1:")
        heater.setting = -1
    except ValueError as e:
        print(f"Error caught: {e}")
    print(f"Current state: {heater}")  # Should still be on with setting of 5
    
    # Test setting to value > 5
    try:
        print("\nAttempting to set setting to 6:")
        heater.setting = 6
    except ValueError as e:
        print(f"Error caught: {e}")
    print(f"Current state: {heater}")  # Should still be on with setting of 5
    
    print("\nCustom device testing completed successfully.")


if __name__ == "__main__":
    test_smart_plug()
    test_custom_device() 