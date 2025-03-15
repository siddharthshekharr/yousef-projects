# Python Smart Home System

This project implements a smart home management system with a graphical user interface using Python and Tkinter. The system allows users to manage smart devices within a home, as well as manage multiple smart homes.

## Features

- Create and manage smart devices (SmartPlug, SmartOven, SmartHeater)
- Toggle devices on/off
- Edit device settings
- Add and remove devices
- View device status
- Manage multiple smart homes (Challenge Task)
- Persistent storage of smart homes data

## Project Structure

```
.
├── main.py                  # Main entry point
├── smart_devices.py         # Smart device classes
├── smart_home.py            # SmartHome class
├── smart_home_app.py        # GUI for single smart home
├── smart_homes_app.py       # GUI for multiple smart homes (Challenge Task)
├── test_smart_devices.py    # Tests for smart device classes
├── test_smart_home.py       # Tests for SmartHome class
└── README.md                # This file
```

## Requirements

- Python 3.10+
- Tkinter (included in standard Python distribution)

## How to Run

1. Make sure you have Python 3.10 or higher installed.
2. Run the main.py file:

```bash
python main.py
```

3. Choose one of the following options:
   - Run tests: Executes all test functions to verify functionality
   - Run Smart Home App: Launches the single smart home GUI
   - Run Smart Homes App: Launches the multiple smart homes GUI (Challenge Task)

## Implementation Details

### Smart Devices

The system supports the following smart devices:

1. **SmartPlug**
   - Option: Consumption rate (0-150 watts)
   - Can be toggled on/off

2. **SmartOven**
   - Option: Temperature (0-260 degrees Celsius)
   - Can be toggled on/off

3. **SmartHeater**
   - Option: Setting (0-5)
   - Can be toggled on/off

### SmartHome

The SmartHome class manages a collection of smart devices, allowing users to:

- Add devices
- Remove devices
- Toggle devices
- Update device options
- Switch all devices on/off

### GUI Applications

1. **SmartHomeApp**
   - Displays all devices in a single smart home
   - Provides controls to toggle, edit, and delete devices
   - Allows adding new devices

2. **SmartHomesApp (Challenge Task)**
   - Manages multiple smart homes
   - Displays summary information for each home
   - Allows opening individual homes in separate windows
   - Provides persistent storage using CSV files

## Testing

The project includes comprehensive test functions for each component:

- `test_smart_plug()`: Tests the SmartPlug class
- `test_custom_device()`: Tests the custom device classes (SmartOven and SmartHeater)
- `test_smart_home()`: Tests the SmartHome class
- `test_smart_home_system()`: Tests the SmartHomeApp GUI
- `test_smart_homes_system()`: Tests the SmartHomesApp GUI (Challenge Task)

## Author

This project was created as a coursework assignment for a Python programming course. 