# Python Smart Home System

A comprehensive Python application for managing smart home devices using object-oriented programming principles and a graphical user interface built with Tkinter.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Implementation Details](#implementation-details)
  - [Smart Devices](#smart-devices)
  - [Smart Home](#smart-home)
  - [GUI Applications](#gui-applications)
  - [Data Persistence](#data-persistence)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Error Handling](#error-handling)
- [Future Enhancements](#future-enhancements)

## Overview

This Python Smart Home System simulates the management of various smart devices within one or multiple smart homes. The application demonstrates object-oriented programming concepts, GUI development with Tkinter, and data persistence using CSV files.

The system allows users to:
- Create and manage multiple smart homes
- Add, remove, and control various smart devices
- Toggle devices on and off
- Adjust device-specific settings
- Save and load smart home configurations

## Features

### Smart Devices
- **SmartPlug**: A basic smart device with a consumption rate (0-150)
- **SmartOven**: A smart oven with adjustable temperature (0-260°C)
- **SmartHeater**: A smart heater with adjustable settings (0-5)

### Smart Home Management
- Create multiple smart homes
- Add and remove devices from each home
- Toggle individual devices on/off
- Toggle all devices on/off simultaneously
- Edit device-specific settings
- Enforce maximum device limits per home

### User Interface
- Console menu for selecting application mode
- Graphical user interface for interacting with smart homes and devices
- Responsive design with proper error handling
- Visual feedback through message boxes

### Data Persistence
- Save smart home configurations to CSV files
- Load previously saved configurations
- Automatic saving when closing the application

## Project Structure

The project consists of the following key files:

- `main.py`: Entry point for the application
- `smart_devices.py`: Defines the smart device classes
- `smart_home.py`: Implements the SmartHome class
- `smart_home_app.py`: GUI for managing a single smart home
- `smart_homes_app.py`: GUI for managing multiple smart homes
- `test_smart_devices.py`: Unit tests for smart device classes
- `test_smart_home.py`: Unit tests for the SmartHome class
- `smart_homes.csv`: Data file for storing smart home configurations

## Implementation Details

### Smart Devices

All smart devices inherit from a common base class and implement the following functionality:

#### SmartPlug
- Represents a smart plug with a consumption rate
- Attributes:
  - `switched_on`: Boolean indicating if the device is on/off
  - `consumption_rate`: Integer between 0-150
- Methods:
  - `toggle_switch()`: Toggles the device on/off
  - `__str__()`: Returns a string representation of the device

#### SmartOven
- Represents a smart oven with adjustable temperature
- Attributes:
  - `switched_on`: Boolean indicating if the device is on/off
  - `temperature`: Integer between 0-260°C
- Methods:
  - `toggle_switch()`: Toggles the device on/off
  - `__str__()`: Returns a string representation of the device

#### SmartHeater
- Represents a smart heater with adjustable settings
- Attributes:
  - `switched_on`: Boolean indicating if the device is on/off
  - `setting`: Integer between 0-5
- Methods:
  - `toggle_switch()`: Toggles the device on/off
  - `__str__()`: Returns a string representation of the device

### Smart Home

The `SmartHome` class manages a collection of smart devices:

- Attributes:
  - `devices`: List of smart devices
  - `max_devices`: Maximum number of devices allowed (default: unlimited)
- Methods:
  - `add_device(device)`: Adds a device to the home
  - `remove_device(index)`: Removes a device at the specified index
  - `get_device(index)`: Returns the device at the specified index
  - `toggle_device(index)`: Toggles the device at the specified index
  - `switch_all_on()`: Turns on all devices
  - `switch_all_off()`: Turns off all devices
  - `update_option(index, option_value)`: Updates a device-specific setting
  - `__str__()`: Returns a string representation of the smart home

### GUI Applications

#### SmartHomeApp

The `SmartHomeApp` class provides a GUI for managing a single smart home:

- Features:
  - Display a list of devices with their status
  - Toggle devices on/off
  - Edit device settings
  - Add new devices
  - Remove existing devices
  - Turn all devices on/off

#### SmartHomesApp

The `SmartHomesApp` class provides a GUI for managing multiple smart homes:

- Features:
  - Display a list of smart homes with summary information
  - Open a smart home for detailed management
  - Add new smart homes
  - Delete existing smart homes
  - Save all smart homes to a file
  - Load smart homes from a file

### Data Persistence

The application uses CSV files to store and retrieve smart home configurations:

- Format:
  - First row: Number of smart homes
  - For each smart home:
    - First row: Number of devices
    - For each device: Device type, option value, switch state

## Running the Application

To run the application, execute the `main.py` file:

```bash
python3 main.py
```

This will display a menu with three options:
1. Run tests
2. Run Smart Home App (single home)
3. Run Smart Homes App (multiple homes)

### Option 1: Run Tests
This option runs all the unit tests for the smart device classes and the SmartHome class.

### Option 2: Run Smart Home App
This option launches the GUI for managing a single smart home with the following features:
- View and control devices
- Toggle devices on/off
- Edit device settings
- Add and remove devices
- Turn all devices on/off

### Option 3: Run Smart Homes App
This option launches the GUI for managing multiple smart homes with the following features:
- View a list of smart homes
- Open a smart home for detailed management
- Add and delete smart homes
- Save and load smart home configurations

## Testing

The project includes comprehensive unit tests for the smart device classes and the SmartHome class:

- `test_smart_devices.py`: Tests the functionality of all smart device classes
  - Initialization with default and custom values
  - Toggle switch functionality
  - Error handling for invalid values

- `test_smart_home.py`: Tests the functionality of the SmartHome class
  - Adding and removing devices
  - Getting devices by index
  - Toggling individual devices
  - Switching all devices on/off
  - Updating device options
  - Error handling for invalid operations

## Error Handling

The application implements robust error handling throughout:

- Input validation for device settings
- Exception handling for device operations
- Boundary checking for device indices
- User-friendly error messages in the GUI
- Graceful handling of file operations

## Future Enhancements

Potential future enhancements for the project:

- Additional smart device types
- Device grouping and scenes
- Scheduling and automation
- User authentication
- Remote access capabilities
- Integration with real smart home protocols
- Energy usage statistics and reporting

---

This project was developed as a demonstration of object-oriented programming principles, GUI development with Tkinter, and data persistence in Python. 