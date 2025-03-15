import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import os
from smart_devices import SmartPlug, SmartOven, SmartHeater
from smart_home import SmartHome
from smart_home_app import SmartHomeApp

class SmartHomesApp:
    """
    A GUI application for managing multiple smart homes.
    
    This class provides a graphical interface for interacting with multiple
    SmartHome instances, allowing users to view, add, remove, and modify
    smart homes and their devices.
    """
    
    def __init__(self, root):
        """
        Initialize the SmartHomesApp with a root window.
        
        Args:
            root: The Tkinter root window.
        """
        self.root = root
        self.root.title("Smart Homes Management System")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # List to store smart homes
        self.smart_homes = []
        
        # Load smart homes from file
        self._load_smart_homes()
        
        # Create the GUI layout
        self._create_widgets()
        
        # Update the smart homes display
        self._update_smart_homes_display()
        
        # Bind close event to save data
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
    
    def _create_widgets(self):
        """Create the GUI widgets."""
        # Create a main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create a title label
        title_label = ttk.Label(
            main_frame, 
            text="Smart Homes Management System", 
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=10)
        
        # Create control buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            control_frame, 
            text="Add Smart Home", 
            width=15,
            command=self._add_smart_home
        ).pack(side=tk.LEFT, padx=5)
        
        # Create a frame for the smart homes list
        self.homes_frame = ttk.LabelFrame(main_frame, text="Smart Homes", padding="10")
        self.homes_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create a canvas with scrollbar for the smart homes list
        canvas_frame = ttk.Frame(self.homes_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(canvas_frame)
        scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create a frame inside the canvas to hold smart home widgets
        self.homes_container = ttk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window(
            (0, 0), 
            window=self.homes_container, 
            anchor=tk.NW, 
            tags="self.homes_container"
        )
        
        # Configure canvas scrolling
        self.homes_container.bind(
            "<Configure>", 
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.bind(
            "<Configure>", 
            lambda e: self.canvas.itemconfig(
                self.canvas_window, 
                width=e.width
            )
        )
    
    def _update_smart_homes_display(self):
        """Update the smart homes display in the GUI."""
        # Clear existing widgets
        for widget in self.homes_container.winfo_children():
            widget.destroy()
        
        if not self.smart_homes:
            # Display a message if no smart homes exist
            ttk.Label(
                self.homes_container, 
                text="No smart homes available. Click 'Add Smart Home' to create one.", 
                font=("Arial", 12)
            ).pack(pady=20)
            return
        
        # Create a frame for each smart home
        for i, home in enumerate(self.smart_homes):
            # Create a frame for this smart home
            home_frame = ttk.Frame(self.homes_container)
            home_frame.pack(fill=tk.X, pady=10)
            
            # Smart home information
            info_frame = ttk.Frame(home_frame)
            info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            # Smart home name and summary
            ttk.Label(
                info_frame, 
                text=f"Smart Home {i+1}", 
                font=("Arial", 14, "bold")
            ).pack(anchor=tk.W)
            
            # Count total devices and devices that are on
            total_devices = home.__str__().count('\n')
            devices_on = 0
            for j in range(total_devices):
                try:
                    device = home.get_device(j)
                    if device.switched_on:
                        devices_on += 1
                except IndexError:
                    pass
            
            ttk.Label(
                info_frame, 
                text=f"Devices: {total_devices} total, {devices_on} on", 
                font=("Arial", 12)
            ).pack(anchor=tk.W)
            
            # Control buttons
            button_frame = ttk.Frame(home_frame)
            button_frame.pack(side=tk.RIGHT)
            
            ttk.Button(
                button_frame, 
                text="Open", 
                width=10,
                command=lambda idx=i: self._open_smart_home(idx)
            ).pack(side=tk.LEFT, padx=2)
            
            ttk.Button(
                button_frame, 
                text="Delete", 
                width=10,
                command=lambda idx=i: self._delete_smart_home(idx)
            ).pack(side=tk.LEFT, padx=2)
            
            # Add a separator
            ttk.Separator(self.homes_container, orient=tk.HORIZONTAL).pack(
                fill=tk.X, 
                pady=5
            )
    
    def _add_smart_home(self):
        """Add a new smart home."""
        try:
            # Create a new smart home
            new_home = SmartHome()
            
            # Add default devices
            new_home.add_device(SmartPlug(45))
            new_home.add_device(SmartOven())
            new_home.add_device(SmartHeater())
            
            # Add to the list
            self.smart_homes.append(new_home)
            
            # Update the display
            self._update_smart_homes_display()
            
            messagebox.showinfo("Success", "New smart home added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add smart home: {str(e)}")
    
    def _delete_smart_home(self, index):
        """
        Delete a smart home at the specified index.
        
        Args:
            index (int): The index of the smart home to delete.
        """
        try:
            if messagebox.askyesno(
                "Confirm Deletion", 
                f"Are you sure you want to delete Smart Home {index+1}?"
            ):
                self.smart_homes.pop(index)
                self._update_smart_homes_display()
                messagebox.showinfo("Success", "Smart home deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete smart home: {str(e)}")
    
    def _open_smart_home(self, index):
        """
        Open a smart home at the specified index in a new window.
        
        Args:
            index (int): The index of the smart home to open.
        """
        try:
            # Create a new top-level window
            home_window = tk.Toplevel(self.root)
            home_window.title(f"Smart Home {index+1}")
            home_window.geometry("600x500")
            home_window.resizable(True, True)
            
            # Create a SmartHomeApp instance for this smart home
            app = SmartHomeApp(home_window)
            
            # Replace the default smart home with the selected one
            app.smart_home = self.smart_homes[index]
            
            # Update the device display
            app._update_device_display()
            
            # Bind close event to update the main display
            home_window.protocol(
                "WM_DELETE_WINDOW", 
                lambda: self._on_home_close(home_window, index, app)
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open smart home: {str(e)}")
    
    def _on_home_close(self, window, index, app):
        """
        Handle the closing of a smart home window.
        
        Args:
            window: The window to close.
            index (int): The index of the smart home.
            app: The SmartHomeApp instance.
        """
        # Update the smart home in the list
        self.smart_homes[index] = app.smart_home
        
        # Update the display
        self._update_smart_homes_display()
        
        # Close the window
        window.destroy()
    
    def _on_close(self):
        """Handle the closing of the main window."""
        # Save smart homes to file
        self._save_smart_homes()
        
        # Close the window
        self.root.destroy()
    
    def _save_smart_homes(self):
        """Save smart homes to a CSV file."""
        try:
            with open("smart_homes.csv", "w", newline="") as file:
                writer = csv.writer(file)
                
                # Write the number of smart homes
                writer.writerow([len(self.smart_homes)])
                
                # For each smart home
                for home in self.smart_homes:
                    # Write the number of devices in this home
                    device_count = home.__str__().count('\n')
                    writer.writerow([device_count])
                    
                    # For each device in this home
                    for i in range(device_count):
                        try:
                            device = home.get_device(i)
                            
                            # Determine device type and option
                            if isinstance(device, SmartPlug):
                                device_type = "SmartPlug"
                                option_value = device.consumption_rate
                            elif isinstance(device, SmartOven):
                                device_type = "SmartOven"
                                option_value = device.temperature
                            elif isinstance(device, SmartHeater):
                                device_type = "SmartHeater"
                                option_value = device.setting
                            else:
                                continue
                            
                            # Write device information
                            writer.writerow([
                                device_type, 
                                option_value, 
                                1 if device.switched_on else 0
                            ])
                        except IndexError:
                            pass
            
            print("Smart homes saved successfully.")
        except Exception as e:
            print(f"Error saving smart homes: {str(e)}")
    
    def _load_smart_homes(self):
        """Load smart homes from a CSV file."""
        try:
            if not os.path.exists("smart_homes.csv"):
                print("No saved smart homes found.")
                return
            
            with open("smart_homes.csv", "r", newline="") as file:
                reader = csv.reader(file)
                
                # Read the number of smart homes
                row = next(reader)
                home_count = int(row[0])
                
                # For each smart home
                for _ in range(home_count):
                    # Create a new smart home
                    home = SmartHome()
                    
                    # Read the number of devices in this home
                    row = next(reader)
                    device_count = int(row[0])
                    
                    # For each device in this home
                    for _ in range(device_count):
                        row = next(reader)
                        device_type = row[0]
                        option_value = int(row[1])
                        switched_on = int(row[2]) == 1
                        
                        # Create the device
                        if device_type == "SmartPlug":
                            device = SmartPlug(option_value)
                        elif device_type == "SmartOven":
                            device = SmartOven(option_value)
                        elif device_type == "SmartHeater":
                            device = SmartHeater(option_value)
                        else:
                            continue
                        
                        # Set the switch state
                        if switched_on:
                            device.toggle_switch()
                        
                        # Add the device to the home
                        home.add_device(device)
                    
                    # Add the home to the list
                    self.smart_homes.append(home)
            
            print("Smart homes loaded successfully.")
        except Exception as e:
            print(f"Error loading smart homes: {str(e)}")
            # If there's an error, start with an empty list
            self.smart_homes = []

def test_smart_homes_system():
    """
    Test the SmartHomesApp GUI.
    
    This function creates and displays the SmartHomesApp GUI for visual inspection.
    """
    root = tk.Tk()
    app = SmartHomesApp(root)
    root.mainloop()

if __name__ == "__main__":
    test_smart_homes_system() 