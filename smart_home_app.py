import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from smart_devices import SmartPlug, SmartOven, SmartHeater
from smart_home import SmartHome

class SmartHomeApp:
    """
    A GUI application for managing a smart home system.
    
    This class provides a graphical interface for interacting with a SmartHome
    instance, allowing users to view and control smart devices.
    """
    
    def __init__(self, root):
        """
        Initialize the SmartHomeApp with a root window.
        
        Args:
            root: The Tkinter root window.
        """
        self.root = root
        self.root.title("Smart Home Control System")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Create and initialize SmartHome with default devices
        self.smart_home = SmartHome()
        self._initialize_devices()
        
        # Print SmartHome to console for verification
        print(self.smart_home)
        
        # Create the GUI layout
        self._create_widgets()
        
        # Update the device display
        self._update_device_display()
    
    def _initialize_devices(self):
        """Initialize SmartHome with default devices."""
        # Add a SmartPlug with default consumption rate of 45W
        self.smart_home.add_device(SmartPlug(45))
        
        # Add a SmartOven with default temperature
        self.smart_home.add_device(SmartOven())
        
        # Add a SmartHeater with default setting
        self.smart_home.add_device(SmartHeater())
    
    def _create_widgets(self):
        """Create the GUI widgets."""
        # Create a main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create a title label
        title_label = ttk.Label(
            main_frame, 
            text="Smart Home Control Panel", 
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=10)
        
        # Create global control buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            control_frame, 
            text="Turn All On", 
            width=15,
            command=self._switch_all_on
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            control_frame, 
            text="Turn All Off", 
            width=15,
            command=self._switch_all_off
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            control_frame, 
            text="Add Device", 
            width=15,
            command=self._add_device
        ).pack(side=tk.RIGHT, padx=5)
        
        # Create a frame for the device list
        self.devices_frame = ttk.LabelFrame(main_frame, text="Devices", padding="10")
        self.devices_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create a canvas with scrollbar for the device list
        canvas_frame = ttk.Frame(self.devices_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(canvas_frame)
        scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create a frame inside the canvas to hold device widgets
        self.devices_container = ttk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window(
            (0, 0), 
            window=self.devices_container, 
            anchor=tk.NW, 
            tags="self.devices_container"
        )
        
        # Configure canvas scrolling
        self.devices_container.bind(
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
    
    def _update_device_display(self):
        """Update the device display in the GUI."""
        # Clear existing widgets
        for widget in self.devices_container.winfo_children():
            widget.destroy()
        
        # Create a frame for each device
        for i in range(self.smart_home.__str__().count('\n')):
            try:
                device = self.smart_home.get_device(i)
                
                # Create a frame for this device
                device_frame = ttk.Frame(self.devices_container)
                device_frame.pack(fill=tk.X, pady=5)
                
                # Device information
                info_frame = ttk.Frame(device_frame)
                info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
                
                # Device number and type
                device_type = str(device).split(' is ')[0]
                ttk.Label(
                    info_frame, 
                    text=f"{i+1}. {device_type}", 
                    font=("Arial", 12, "bold")
                ).pack(anchor=tk.W)
                
                # Device status
                status_text = str(device)
                ttk.Label(
                    info_frame, 
                    text=status_text, 
                    font=("Arial", 10)
                ).pack(anchor=tk.W)
                
                # Control buttons
                button_frame = ttk.Frame(device_frame)
                button_frame.pack(side=tk.RIGHT)
                
                ttk.Button(
                    button_frame, 
                    text="Toggle", 
                    width=10,
                    command=lambda idx=i: self._toggle_device(idx)
                ).pack(side=tk.LEFT, padx=2)
                
                ttk.Button(
                    button_frame, 
                    text="Edit", 
                    width=10,
                    command=lambda idx=i: self._edit_device(idx)
                ).pack(side=tk.LEFT, padx=2)
                
                ttk.Button(
                    button_frame, 
                    text="Delete", 
                    width=10,
                    command=lambda idx=i: self._delete_device(idx)
                ).pack(side=tk.LEFT, padx=2)
                
                # Add a separator
                ttk.Separator(self.devices_container, orient=tk.HORIZONTAL).pack(
                    fill=tk.X, 
                    pady=5
                )
                
            except IndexError:
                break
    
    def _switch_all_on(self):
        """Turn on all devices."""
        try:
            self.smart_home.switch_all_on()
            self._update_device_display()
            messagebox.showinfo("Success", "All devices turned on successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to turn on all devices: {str(e)}")
    
    def _switch_all_off(self):
        """Turn off all devices."""
        try:
            self.smart_home.switch_all_off()
            self._update_device_display()
            messagebox.showinfo("Success", "All devices turned off successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to turn off all devices: {str(e)}")
    
    def _toggle_device(self, index):
        """
        Toggle a device at the specified index.
        
        Args:
            index (int): The index of the device to toggle.
        """
        try:
            self.smart_home.toggle_device(index)
            self._update_device_display()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to toggle device: {str(e)}")
    
    def _edit_device(self, index):
        """
        Edit a device at the specified index.
        
        Args:
            index (int): The index of the device to edit.
        """
        try:
            device = self.smart_home.get_device(index)
            
            # Create a new top-level window for editing
            edit_window = tk.Toplevel(self.root)
            edit_window.title(f"Edit {str(device).split(' is ')[0]}")
            edit_window.geometry("300x200")
            edit_window.resizable(False, False)
            edit_window.transient(self.root)
            edit_window.grab_set()
            
            # Create a frame for the form
            form_frame = ttk.Frame(edit_window, padding="20")
            form_frame.pack(fill=tk.BOTH, expand=True)
            
            # Determine which attribute to edit based on device type
            if isinstance(device, SmartPlug):
                ttk.Label(form_frame, text="Consumption Rate (0-150):").pack(anchor=tk.W, pady=5)
                value_var = tk.IntVar(value=device.consumption_rate)
                ttk.Spinbox(
                    form_frame, 
                    from_=0, 
                    to=150, 
                    textvariable=value_var, 
                    width=10
                ).pack(anchor=tk.W, pady=5)
                
                def save_changes():
                    try:
                        self.smart_home.update_option(index, value_var.get())
                        edit_window.destroy()
                        self._update_device_display()
                        messagebox.showinfo("Success", "Device updated successfully.")
                    except ValueError as e:
                        messagebox.showerror("Error", str(e))
                
            elif isinstance(device, SmartOven):
                ttk.Label(form_frame, text="Temperature (0-260):").pack(anchor=tk.W, pady=5)
                value_var = tk.IntVar(value=device.temperature)
                ttk.Spinbox(
                    form_frame, 
                    from_=0, 
                    to=260, 
                    textvariable=value_var, 
                    width=10
                ).pack(anchor=tk.W, pady=5)
                
                def save_changes():
                    try:
                        self.smart_home.update_option(index, value_var.get())
                        edit_window.destroy()
                        self._update_device_display()
                        messagebox.showinfo("Success", "Device updated successfully.")
                    except ValueError as e:
                        messagebox.showerror("Error", str(e))
                
            elif isinstance(device, SmartHeater):
                ttk.Label(form_frame, text="Setting (0-5):").pack(anchor=tk.W, pady=5)
                value_var = tk.IntVar(value=device.setting)
                ttk.Spinbox(
                    form_frame, 
                    from_=0, 
                    to=5, 
                    textvariable=value_var, 
                    width=10
                ).pack(anchor=tk.W, pady=5)
                
                def save_changes():
                    try:
                        self.smart_home.update_option(index, value_var.get())
                        edit_window.destroy()
                        self._update_device_display()
                        messagebox.showinfo("Success", "Device updated successfully.")
                    except ValueError as e:
                        messagebox.showerror("Error", str(e))
            
            # Add buttons
            button_frame = ttk.Frame(form_frame)
            button_frame.pack(fill=tk.X, pady=10)
            
            ttk.Button(
                button_frame, 
                text="Save", 
                command=save_changes
            ).pack(side=tk.RIGHT, padx=5)
            
            ttk.Button(
                button_frame, 
                text="Cancel", 
                command=edit_window.destroy
            ).pack(side=tk.RIGHT, padx=5)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to edit device: {str(e)}")
    
    def _delete_device(self, index):
        """
        Delete a device at the specified index.
        
        Args:
            index (int): The index of the device to delete.
        """
        try:
            device = self.smart_home.get_device(index)
            if messagebox.askyesno(
                "Confirm Deletion", 
                f"Are you sure you want to delete {str(device).split(' is ')[0]}?"
            ):
                self.smart_home.remove_device(index)
                self._update_device_display()
                messagebox.showinfo("Success", "Device deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete device: {str(e)}")
    
    def _add_device(self):
        """Add a new device to the smart home."""
        try:
            # Create a new top-level window for adding a device
            add_window = tk.Toplevel(self.root)
            add_window.title("Add Device")
            add_window.geometry("300x250")
            add_window.resizable(False, False)
            add_window.transient(self.root)
            add_window.grab_set()
            
            # Create a frame for the form
            form_frame = ttk.Frame(add_window, padding="20")
            form_frame.pack(fill=tk.BOTH, expand=True)
            
            # Device type selection
            ttk.Label(form_frame, text="Device Type:").pack(anchor=tk.W, pady=5)
            device_type_var = tk.StringVar(value="SmartPlug")
            device_type_combo = ttk.Combobox(
                form_frame, 
                textvariable=device_type_var, 
                values=["SmartPlug", "SmartOven", "SmartHeater"], 
                state="readonly"
            )
            device_type_combo.pack(anchor=tk.W, pady=5)
            
            # Frame for device-specific options
            options_frame = ttk.Frame(form_frame)
            options_frame.pack(fill=tk.X, pady=5)
            
            # Variables for device options
            option_var = tk.IntVar(value=45)  # Default for SmartPlug
            option_label = ttk.Label(options_frame, text="Consumption Rate (0-150):")
            option_label.pack(anchor=tk.W, pady=5)
            
            option_widget = ttk.Spinbox(
                options_frame, 
                from_=0, 
                to=150, 
                textvariable=option_var, 
                width=10
            )
            option_widget.pack(anchor=tk.W, pady=5)
            
            # Update options based on device type selection
            def update_options(*args):
                # Clear existing widgets
                for widget in options_frame.winfo_children():
                    widget.destroy()
                
                if device_type_var.get() == "SmartPlug":
                    option_var.set(45)
                    ttk.Label(options_frame, text="Consumption Rate (0-150):").pack(anchor=tk.W, pady=5)
                    ttk.Spinbox(
                        options_frame, 
                        from_=0, 
                        to=150, 
                        textvariable=option_var, 
                        width=10
                    ).pack(anchor=tk.W, pady=5)
                    
                elif device_type_var.get() == "SmartOven":
                    option_var.set(150)
                    ttk.Label(options_frame, text="Temperature (0-260):").pack(anchor=tk.W, pady=5)
                    ttk.Spinbox(
                        options_frame, 
                        from_=0, 
                        to=260, 
                        textvariable=option_var, 
                        width=10
                    ).pack(anchor=tk.W, pady=5)
                    
                elif device_type_var.get() == "SmartHeater":
                    option_var.set(2)
                    ttk.Label(options_frame, text="Setting (0-5):").pack(anchor=tk.W, pady=5)
                    ttk.Spinbox(
                        options_frame, 
                        from_=0, 
                        to=5, 
                        textvariable=option_var, 
                        width=10
                    ).pack(anchor=tk.W, pady=5)
            
            # Bind the update function to the combobox selection
            device_type_var.trace_add("write", update_options)
            
            # Add buttons
            button_frame = ttk.Frame(form_frame)
            button_frame.pack(fill=tk.X, pady=10)
            
            def add_new_device():
                try:
                    device_type = device_type_var.get()
                    option_value = option_var.get()
                    
                    if device_type == "SmartPlug":
                        new_device = SmartPlug(option_value)
                    elif device_type == "SmartOven":
                        new_device = SmartOven(option_value)
                    elif device_type == "SmartHeater":
                        new_device = SmartHeater(option_value)
                    
                    self.smart_home.add_device(new_device)
                    add_window.destroy()
                    self._update_device_display()
                    messagebox.showinfo("Success", f"{device_type} added successfully.")
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            
            ttk.Button(
                button_frame, 
                text="Add", 
                command=add_new_device
            ).pack(side=tk.RIGHT, padx=5)
            
            ttk.Button(
                button_frame, 
                text="Cancel", 
                command=add_window.destroy
            ).pack(side=tk.RIGHT, padx=5)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add device: {str(e)}")

def test_smart_home_system():
    """
    Test the SmartHomeApp GUI.
    
    This function creates and displays the SmartHomeApp GUI for visual inspection.
    """
    root = tk.Tk()
    app = SmartHomeApp(root)
    root.mainloop()

if __name__ == "__main__":
    test_smart_home_system() 