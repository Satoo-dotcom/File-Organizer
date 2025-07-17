# 🗂️ File Organizer GUI (Python + Tkinter)

This is a simple and intuitive File Organizer desktop application built using Python and Tkinter. It allows you to organize files in a selected folder based on their file types (e.g., Images, Documents, Videos, Archives, etc.).

---

## ✅ Features

- Organizes files by extensions into categorized folders.
- Supports common file types (e.g., `.jpg`, `.pdf`, `.mp4`, etc.).
- Files with unrecognized extensions are placed into an **"Others"** folder.
- Easy-to-use graphical interface with folder selection and one-click organization.

---

## 🛠 Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python on most systems)
- No third-party libraries required

---

## 📦 How to Use

### 1. **Clone or Download the Script**
You can copy the script to a `.py` file, for example:

```bash
file_organizer.py
Or create it with:

bash
Copy
Edit
touch file_organizer.py
Paste the provided Python code into that file.

2. Run the Script
Open a terminal (or command prompt), navigate to the script's directory, and run:

bash
Copy
Edit
python file_organizer.py
Make sure you're using Python 3. If you have multiple versions, use python3.

3. Using the GUI
The application window will open.

Click the "Browse" button to select the folder you want to organize.

Once selected, the folder path will appear in the text box.

Click "Organize Files".

The files in the selected folder will be moved into categorized subfolders such as:

Copy
Edit
📁 YourFolder/
├── 📁 Images/
├── 📁 Documents/
├── 📁 Archives/
├── 📁 Videos/
├── 📁 Music/
└── 📁 Others/
You’ll get a success message once organizing is complete.

📂 File Categories
Folder	File Extensions
Images	.jpg, .jpeg, .png, .gif, .bmp, .tiff
Documents	.pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx
Archives	.zip, .rar, .7z, .tar, .gz
Videos	.mp4, .mov, .avi, .mkv
Music	.mp3, .wav, .aac, .flac
Others	Any file with an unrecognized extension

🧼 Notes
Files are moved, not copied. So make sure you don't need them in their original location.

The application does not scan subfolders, only the top-level files in the selected folder.
