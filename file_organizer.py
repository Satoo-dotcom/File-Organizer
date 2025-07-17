import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import logging
import json
import threading
import time
from datetime import datetime

# Mapping of file extensions to folder names
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
}

LOG_FILE = "file_organizer.log"
UNDO_FILE = "undo_record.json"

# Setup logging
logging.basicConfig(filename=LOG_FILE,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Global variable for scheduling thread
scheduler_thread = None
stop_scheduler = threading.Event()

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Selected path is not a valid directory.")
        return False

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if not files:
        messagebox.showinfo("Info", "No files found in the selected folder.")
        return False

    moved_files = []  # To record moves for undo

    for file in files:
        src_path = os.path.join(folder_path, file)
        file_ext = os.path.splitext(file)[1].lower()
        moved = False
        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                dest_folder = os.path.join(folder_path, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, file)
                shutil.move(src_path, dest_path)
                logging.info(f"Moved '{src_path}' to '{dest_path}'")
                moved_files.append({'src': src_path, 'dest': dest_path})
                moved = True
                break
        if not moved:
            dest_folder = os.path.join(folder_path, 'Others')
            os.makedirs(dest_folder, exist_ok=True)
            dest_path = os.path.join(dest_folder, file)
            shutil.move(src_path, dest_path)
            logging.info(f"Moved '{src_path}' to '{dest_path}'")
            moved_files.append({'src': src_path, 'dest': dest_path})

    # Save moved files for undo
    with open(UNDO_FILE, 'w') as f:
        json.dump(moved_files, f, indent=2)

    messagebox.showinfo("Success", "Files have been organized successfully!")
    return True

def undo_last_organize():
    if not os.path.exists(UNDO_FILE):
        messagebox.showinfo("Info", "No organize operation to undo.")
        return

    with open(UNDO_FILE, 'r') as f:
        moved_files = json.load(f)

    errors = []
    for move in moved_files:
        try:
            if os.path.exists(move['dest']):
                os.makedirs(os.path.dirname(move['src']), exist_ok=True)
                shutil.move(move['dest'], move['src'])
                logging.info(f"Undo move: '{move['dest']}' back to '{move['src']}'")
        except Exception as e:
            errors.append(str(e))

    if errors:
        messagebox.showerror("Error", f"Some files could not be moved back:\n{errors}")
    else:
        messagebox.showinfo("Success", "Undo completed successfully!")

    # Remove undo record after undo
    os.remove(UNDO_FILE)

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

def start_undo():
    undo_last_organize()

def schedule_organizing():
    interval_str = schedule_interval_var.get()
    folder_path = folder_path_var.get()
    if not folder_path:
        messagebox.showwarning("Warning", "Please select a folder first.")
        return
    try:
        interval = int(interval_str)
        if interval <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for interval.")
        return

    global scheduler_thread, stop_scheduler
    if scheduler_thread and scheduler_thread.is_alive():
        messagebox.showinfo("Info", "Scheduler is already running.")
        return

    stop_scheduler.clear()
    scheduler_thread = threading.Thread(target=run_scheduler, args=(folder_path, interval), daemon=True)
    scheduler_thread.start()
    messagebox.showinfo("Scheduler", f"Started scheduling every {interval} minutes.")

def stop_scheduling():
    global stop_scheduler
    if scheduler_thread and scheduler_thread.is_alive():
        stop_scheduler.set()
        messagebox.showinfo("Scheduler", "Scheduling stopped.")
    else:
        messagebox.showinfo("Scheduler", "Scheduler is not running.")

def run_scheduler(folder_path, interval):
    while not stop_scheduler.is_set():
        logging.info(f"Scheduled organizing started for folder: {folder_path}")
        organize_files(folder_path)
        for _ in range(interval * 60):
            if stop_scheduler.is_set():
                break
            time.sleep(1)

# GUI Setup
root = tk.Tk()
root.title("File Organizer")
root.geometry("500x220")
root.resizable(False, False)

folder_path_var = tk.StringVar()
schedule_interval_var = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill='both', expand=True)

# Folder selection
label = tk.Label(frame, text="Select Folder to Organize:")
label.grid(row=0, column=0, sticky='w')

entry = tk.Entry(frame, textvariable=folder_path_var, width=50)
entry.grid(row=1, column=0, padx=(0, 5), sticky='w')

browse_btn = tk.Button(frame, text="Browse", command=browse_folder)
browse_btn.grid(row=1, column=1, sticky='w')

# Organize button
organize_btn = tk.Button(frame, text="Organize Files", command=start_organizing, bg='green', fg='white')
organize_btn.grid(row=2, column=0, pady=10, sticky='w')

# Undo button
undo_btn = tk.Button(frame, text="Undo Last Organize", command=start_undo, bg='orange')
undo_btn.grid(row=2, column=1, pady=10, sticky='w')

# Scheduling controls
schedule_label = tk.Label(frame, text="Schedule interval (minutes):")
schedule_label.grid(row=3, column=0, sticky='w')

schedule_entry = tk.Entry(frame, textvariable=schedule_interval_var, width=10)
schedule_entry.grid(row=4, column=0, sticky='w')

schedule_start_btn = tk.Button(frame, text="Start Scheduler", command=schedule_organizing, bg='blue', fg='white')
schedule_start_btn.grid(row=4, column=1, sticky='w')

schedule_stop_btn = tk.Button(frame, text="Stop Scheduler", command=stop_scheduling, bg='red', fg='white')
schedule_stop_btn.grid(row=5, column=1, pady=10, sticky='w')

root.mainloop()
