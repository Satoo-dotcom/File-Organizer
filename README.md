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
