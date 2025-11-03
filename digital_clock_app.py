#!/usr/bin/env python3
"""
Digital Clock App
A simple, elegant digital clock application with GUI.
"""

import tkinter as tk
from datetime import datetime
import sys
import os

class DigitalClock:
    """A digital clock application using tkinter."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.create_widgets()
        self.update_time()
        
    def setup_window(self):
        """Configure the main window."""
        self.root.title("Digital Clock")
        self.root.geometry("350x100")
        self.root.resizable(False, False)
        
        # Center the window on screen
        self.center_window()
        
        # Set window properties
        self.root.configure(bg="black")
        
        # Make window stay on top (optional)
        # self.root.attributes('-topmost', True)
        
    def center_window(self):
        """Center the window on the screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_widgets(self):
        """Create and configure the UI widgets."""
        # Create main frame
        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Create label for displaying time
        self.time_label = tk.Label(
            main_frame,
            font=("Courier", 18, "bold"),
            bg="black",
            fg="#00FF00",  # Bright green
            text="Loading..."
        )
        self.time_label.pack(expand=True)
        
        # Create label for displaying date
        self.date_label = tk.Label(
            main_frame,
            font=("Courier", 12, "normal"),
            bg="black",
            fg="#00AA00",  # Darker green
            text=""
        )
        self.date_label.pack()
        
    def update_time(self):
        """Update the time and date display."""
        try:
            current_time = datetime.now()
            
            # Format time and date
            time_string = current_time.strftime("%H:%M:%S")
            date_string = current_time.strftime("%A, %B %d, %Y")
            
            # Update the labels
            self.time_label.config(text=time_string)
            self.date_label.config(text=date_string)
            
        except Exception as e:
            print(f"Error updating time: {e}")
            self.time_label.config(text="Error")
            
        # Schedule the next update after 1000ms (1 second)
        self.root.after(1000, self.update_time)
        
    def run(self):
        """Start the application."""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nApplication closed by user.")
            self.root.quit()
        except Exception as e:
            print(f"Application error: {e}")
            sys.exit(1)


def main():
    """Main entry point for the application."""
    try:
        # Create and run the clock
        app = DigitalClock()
        app.run()
    except Exception as e:
        print(f"Failed to start Digital Clock: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()