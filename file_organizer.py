import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Mapping of file extensions to folder names
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    # Add more categories and extensions as needed
}

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Selected path is not a valid directory.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if not files:
        messagebox.showinfo("Info", "No files found in the selected folder.")
        return

    for file in files:
        file_ext = os.path.splitext(file)[1].lower()
        moved = False
        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                dest_folder = os.path.join(folder_path, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(os.path.join(folder_path, file), os.path.join(dest_folder, file))
                moved = True
                break
        if not moved:
            # Files with unknown extensions go to 'Others'
            dest_folder = os.path.join(folder_path, 'Others')
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(os.path.join(folder_path, file), os.path.join(dest_folder, file))

    messagebox.showinfo("Success", "Files have been organized successfully!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_var.set(folder_selected)

def start_organizing():
    folder_path = folder_path_var.get()
    if not folder_path:
        messagebox.showwarning("Warning", "Please select a folder first.")
        return
    organize_files(folder_path)

# GUI Setup
root = tk.Tk()
root.title("File Organizer")
root.geometry("450x150")
root.resizable(False, False)

folder_path_var = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill='both', expand=True)

label = tk.Label(frame, text="Select Folder to Organize:")
label.pack(anchor='w')

entry = tk.Entry(frame, textvariable=folder_path_var, width=50)
entry.pack(side='left', padx=(0, 5))

browse_btn = tk.Button(frame, text="Browse", command=browse_folder)
browse_btn.pack(side='left')

organize_btn = tk.Button(root, text="Organize Files", command=start_organizing, bg='green', fg='white')
organize_btn.pack(pady=10)

root.mainloop()