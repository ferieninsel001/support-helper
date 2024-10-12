import os
import shutil

# Dictionary to map file extensions to human-readable folder names
extension_to_folder = {
    'docx': 'Word',
    'doc': 'Word',
    'xlsx': 'Excel',
    'xls': 'Excel',
    'pptx': 'PowerPoint',
    'ppt': 'PowerPoint',
    # Add other common extensions or categories if needed
}

def get_desktop_path():
    # Path to the user's desktop
    user_profile = os.path.expanduser("~")
    
    # Check if the desktop is part of OneDrive
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

def sort_files_on_desktop():
    desktop_path = get_desktop_path()
    
    # Define the 'files' folder path on the desktop
    files_folder = os.path.join(desktop_path, "files")
    
    # Check if the 'files' folder already exists; create it if not
    if not os.path.exists(files_folder):
        print(f"Creating 'files' folder at {files_folder}")
        os.makedirs(files_folder, exist_ok=True)
    else:
        print(f"'files' folder already exists at {files_folder}, sorting files...")

    # Loop through all items on the desktop
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        
        # Check if the item is a file (not a directory)
        if os.path.isfile(item_path) and item != "files":  # Skip the 'files' folder itself
            # Get the file extension
            file_extension = os.path.splitext(item)[1][1:]  # Get the extension without the dot

            # Check if the extension is in our special dictionary
            if file_extension in extension_to_folder:
                folder_name = extension_to_folder[file_extension]
            else:
                # Default to the extension itself as the folder name
                folder_name = file_extension

            extension_folder = os.path.join(files_folder, folder_name)

            # Create a subfolder for the file extension if it doesn't exist
            os.makedirs(extension_folder, exist_ok=True)

            # Move the file into the corresponding subfolder
            shutil.move(item_path, os.path.join(extension_folder, item))
            print(f"Moved: {item} to {extension_folder}")


sort_files_on_desktop()
