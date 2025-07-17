# File Organizer App

This is a simple Python-based GUI application that organizes files in a selected folder by their file types. It uses `tkinter` for the interface and `shutil`/`os` for organizing the files.

## Features

- Organizes files into subfolders by type (Images, Documents, Videos, etc.)
- Supports drag-and-drop folder selection via GUI
- Automatically handles unknown file extensions by putting them in an "Others" folder

## Supported Categories

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`
- **Music**: `.mp3`, `.wav`, `.aac`, `.flac`

## How to Use

1. Run the application using:

   ```bash
   python file_organizer.py
