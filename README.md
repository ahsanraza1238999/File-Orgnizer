# File Organizer

A simple file organizer utility built with Python and packaged into a standalone `.exe` file using PyInstaller.  

## How It Works
Just place the `organizer.exe` file in any folder you want to organize, and **double-click it**.  
It will automatically sort the files inside that folder into categorized subfolders (e.g., Images, Documents, Videos, etc.).  

No terminal or command prompt is required — it runs silently in the background and does its job on its own.  

## Usage
1. Download the `organizer.exe` file from the releases (or build it yourself with PyInstaller).
2. Copy or move `organizer.exe` into the folder you want to organize.
3. Double-click `organizer.exe`.
4. Sit back and let it organize your messy folder into clean categories.

## Build Instructions (Optional)
If you want to build the `.exe` yourself from the Python script:
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole organizer.py
