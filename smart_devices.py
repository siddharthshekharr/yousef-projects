class SmartPlug:
    """
    A class representing a smart plug device.
    
    Attributes:
        switched_on (bool): Indicates whether the plug is on or off.
        consumption_rate (int): Power consumption in watts (0-150).
    """
    
    def __init__(self, consumption_rate):
        """
        Initialize a SmartPlug with a given consumption rate.
        
        Args:
            consumption_rate (int): Power consumption in watts (0-150).
            
        Raises:
            ValueError: If consumption_rate is not between 0 and 150.
        """
        if not isinstance(consumption_rate, int) or consumption_rate < 0 or consumption_rate > 150:
            raise ValueError("Consumption rate must be an integer between 0 and 150")
        self.__consumption_rate = consumption_rate
        self.__switched_on = False
    
    @property
    def consumption_rate(self):
        """Get the current consumption rate."""
        return self.__consumption_rate
    
    @consumption_rate.setter
    def consumption_rate(self, value):
        """
        Set the consumption rate.
        
        Args:
            value (int): New consumption rate.
            
        Raises:
            ValueError: If value is not between 0 and 150.
        """
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("Consumption rate must be an integer between 0 and 150")
        self.__consumption_rate = value
    
    @property
    def switched_on(self):
        """Get the current switch state."""
        return self.__switched_on
    
    def toggle_switch(self):
        """Toggle the switch state between on and off."""
        self.__switched_on = not self.__switched_on
    
    def __str__(self):
        """
        Return a string representation of the SmartPlug.
        
        Returns:
            str: A string describing the SmartPlug's state and consumption rate.
        """
        status = "on" if self.__switched_on else "off"
        return f"SmartPlug is {status} with a consumption rate of {self.__consumption_rate}"


class SmartDevice:
    """
    Base class for all smart devices.
    
    Attributes:
        switched_on (bool): Indicates whether the device is on or off.
    """
    
    def __init__(self):
        """Initialize a SmartDevice with switched_on set to False."""
        self._switched_on = False
    
    @property
    def switched_on(self):
        """Get the current switch state."""
        return self._switched_on
    
    def toggle_switch(self):
        """Toggle the switch state between on and off."""
        self._switched_on = not self._switched_on


class SmartOven(SmartDevice):
    """
    A class representing a smart oven device.
    
    Attributes:
        switched_on (bool): Indicates whether the oven is on or off.
        temperature (int): Temperature setting (0-260 degrees Celsius).
    """
    
    def __init__(self, temperature=150):
        """
        Initialize a SmartOven with a given temperature.
        
        Args:
            temperature (int, optional): Temperature setting (0-260). Defaults to 150.
            
        Raises:
            ValueError: If temperature is not between 0 and 260.
        """
        super().__init__()
        if not isinstance(temperature, int) or temperature < 0 or temperature > 260:
            raise ValueError("Temperature must be an integer between 0 and 260 degrees Celsius")
        self.__temperature = temperature
    
    @property
    def temperature(self):
        """Get the current temperature setting."""
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        """
        Set the temperature.
        
        Args:
            value (int): New temperature setting.
            
        Raises:
            ValueError: If value is not between 0 and 260.
        """
        if not isinstance(value, int) or value < 0 or value > 260:
            raise ValueError("Temperature must be an integer between 0 and 260 degrees Celsius")
        self.__temperature = value
    
    def __str__(self):
        """
        Return a string representation of the SmartOven.
        
        Returns:
            str: A string describing the SmartOven's state and temperature.
        """
        status = "on" if self._switched_on else "off"
        return f"SmartOven is {status} with a temperature of {self.__temperature}"


class SmartHeater(SmartDevice):
    """
    A class representing a smart heater device.
    
    Attributes:
        switched_on (bool): Indicates whether the heater is on or off.
        setting (int): Heat setting (0-5).
    """
    
    def __init__(self, setting=2):
        """
        Initialize a SmartHeater with a given setting.
        
        Args:
            setting (int, optional): Heat setting (0-5). Defaults to 2.
            
        Raises:
            ValueError: If setting is not between 0 and 5.
        """
        super().__init__()
        if not isinstance(setting, int) or setting < 0 or setting > 5:
            raise ValueError("Setting must be a whole number between 0 and 5")
        self.__setting = setting
    
    @property
    def setting(self):
        """Get the current heat setting."""
        return self.__setting
    
    @setting.setter
    def setting(self, value):
        """
        Set the heat setting.
        
        Args:
            value (int): New heat setting.
            
        Raises:
            ValueError: If value is not between 0 and 5.
        """
        if not isinstance(value, int) or value < 0 or value > 5:
            raise ValueError("Setting must be a whole number between 0 and 5")
        self.__setting = value
    
    def __str__(self):
        """
        Return a string representation of the SmartHeater.
        
        Returns:
            str: A string describing the SmartHeater's state and setting.
        """
        status = "on" if self._switched_on else "off"
        return f"SmartHeater is {status} with a setting of {self.__setting}" 