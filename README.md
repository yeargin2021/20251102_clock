# Digital Clock App

A simple, elegant digital clock application built with Python and tkinter.

## Features

- Real-time digital clock display
- Clean, modern interface with green text on black background
- Shows both time (HH:MM:SS) and date (Day, Month DD, YYYY)
- Centered window that stays in focus
- Cross-platform compatibility (Windows, macOS, Linux)

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)

## Installation & Setup

1. **Clone or download this project**
2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Method 1: Run directly
```bash
python digital_clock_app.py
```

### Method 2: Run as a module
```bash
python -m digital_clock_app
```

### Method 3: Make executable (macOS/Linux)
```bash
chmod +x run_clock.sh
./run_clock.sh
```

## Project Structure

```
digital_clock_app/
├── digital_clock_app.py    # Main application file
├── mod01.py               # Original version
├── requirements.txt       # Python dependencies
├── run_clock.sh          # Shell script to run the app
├── setup.py              # Package setup file
└── README.md             # This file
```

## Customization

You can easily customize the clock by modifying `digital_clock_app.py`:

- **Colors:** Change `fg` and `bg` parameters in the label configurations
- **Fonts:** Modify the `font` tuples (family, size, style)
- **Window size:** Adjust the `geometry()` method
- **Time format:** Change the `strftime()` format strings

## Troubleshooting

### Common Issues

1. **"tkinter not found" error:**
   - On Ubuntu/Debian: `sudo apt-get install python3-tk`
   - On CentOS/RHEL: `sudo yum install tkinter`
   - On macOS: tkinter should be included with Python

2. **Window doesn't appear:**
   - Check if you have a display server running
   - On SSH connections, use X11 forwarding: `ssh -X`

3. **Permission denied:**
   - Make sure the script is executable: `chmod +x digital_clock_app.py`

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.