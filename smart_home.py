class SmartHome:
    """
    A class representing a smart home that manages a collection of smart devices.
    
    Attributes:
        devices (list): A list of smart devices in the home.
        max_items (int): Maximum number of devices that can be added to the home.
    """
    
    def __init__(self, max_items=10):
        """
        Initialize a SmartHome with an empty collection of devices.
        
        Args:
            max_items (int, optional): Maximum number of devices. Defaults to 10.
        """
        self.__devices = []
        self.__max_items = max_items
    
    def add_device(self, device):
        """
        Add a device to the smart home.
        
        Args:
            device: The smart device to add.
            
        Raises:
            ValueError: If the maximum number of devices has been reached.
        """
        if len(self.__devices) >= self.__max_items:
            raise ValueError(f"Cannot add more devices. Maximum of {self.__max_items} reached.")
        self.__devices.append(device)
    
    def get_device(self, index):
        """
        Get a device at the specified index.
        
        Args:
            index (int): The index of the device to retrieve.
            
        Returns:
            The device at the specified index.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.__devices):
            raise IndexError("Device index out of range")
        return self.__devices[index]
    
    def toggle_device(self, index):
        """
        Toggle the switch of a device at the specified index.
        
        Args:
            index (int): The index of the device to toggle.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.__devices):
            raise IndexError("Device index out of range")
        self.__devices[index].toggle_switch()
    
    def switch_all_on(self):
        """Turn on all devices in the smart home."""
        for device in self.__devices:
            if not device.switched_on:
                device.toggle_switch()
    
    def switch_all_off(self):
        """Turn off all devices in the smart home."""
        for device in self.__devices:
            if device.switched_on:
                device.toggle_switch()
    
    def remove_device(self, index):
        """
        Remove a device at the specified index.
        
        Args:
            index (int): The index of the device to remove.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.__devices):
            raise IndexError("Device index out of range")
        self.__devices.pop(index)
    
    def update_option(self, index, value):
        """
        Update the option attribute of a device at the specified index.
        
        Args:
            index (int): The index of the device to update.
            value: The new value for the option attribute.
            
        Raises:
            IndexError: If the index is out of range.
            AttributeError: If the device doesn't have the appropriate option attribute.
        """
        device = self.get_device(index)
        
        # Determine which attribute to update based on device type
        if hasattr(device, 'consumption_rate'):
            device.consumption_rate = value
        elif hasattr(device, 'temperature'):
            device.temperature = value
        elif hasattr(device, 'setting'):
            device.setting = value
        else:
            raise AttributeError("Device does not have a recognized option attribute")
    
    def __str__(self):
        """
        Return a string representation of the SmartHome.
        
        Returns:
            str: A string describing the SmartHome and its devices.
        """
        result = f"SmartHome with {len(self.__devices)} device(s):"
        for i, device in enumerate(self.__devices):
            result += f"\n{i+1}- {device}"
        return result 