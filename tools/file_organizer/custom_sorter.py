import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

extension_to_folder = {
    'docx': 'Word',
    'doc': 'Word',
    'xlsx': 'Excel',
    'xls': 'Excel',
    'pptx': 'PowerPoint',
    'ppt': 'PowerPoint',
}

def get_desktop_path():
    user_profile = os.path.expanduser("~")
    
    onedrive_path = os.path.join(user_profile, "OneDrive", "Desktop")
    regular_desktop_path = os.path.join(user_profile, "Desktop")
    
    if os.path.exists(onedrive_path):
        print("OneDrive Desktop detected.")
        return onedrive_path
    elif os.path.exists(regular_desktop_path):
        print("Regular Desktop detected.")
        return regular_desktop_path
    else:
        raise Exception("Desktop folder not found.")

def select_folder():
    root = Tk()
    root.withdraw()

    folder_selected = askdirectory(title="Select Folder to Search for Files")
    
    return folder_selected

def sort_files(selected_folder):
    desktop_path = get_desktop_path()
    
    files_folder = os.path.join(desktop_path, "files")
    
    if not os.path.exists(files_folder):
        print(f"Creating 'files' folder at {files_folder}")
        os.makedirs(files_folder, exist_ok=True)
    else:
        print(f"'files' folder already exists at {files_folder}, sorting files...")

    for item in os.listdir(selected_folder):
        item_path = os.path.join(selected_folder, item)
        
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1][1:]

            if file_extension in extension_to_folder:
                folder_name = extension_to_folder[file_extension]
            else:
                folder_name = file_extension

            extension_folder = os.path.join(files_folder, folder_name)

            os.makedirs(extension_folder, exist_ok=True)

            shutil.move(item_path, os.path.join(extension_folder, item))
            print(f"Moved: {item} to {extension_folder}")

selected_folder = select_folder()
if selected_folder:
    sort_files(selected_folder)
else:
    print("No folder selected")
