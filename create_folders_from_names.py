import os
from glob import glob

def get_subfolder_names(path):
    subfolders = glob(os.path.join(path, '*/'))  
    subfolder_names = [os.path.basename(os.path.normpath(subfolder)) for subfolder in subfolders]
    return subfolder_names

def create_folders_from_names(base_dir, subfolder_names):
    for name in subfolder_names:
        new_folder_path = os.path.join(base_dir, name)
        if not os.path.exists(new_folder_path):  # Avoid creating duplicates
            os.makedirs(new_folder_path)
            print(f"Created folder: {new_folder_path}")
        else:
            print(f"Folder already exists: {new_folder_path}")

# Example usage:
folder_path = 'train'  # Assuming 'train' is directly in your current working directory
base_dir = '.'         # Create new folders in the current working directory

subfolder_names = get_subfolder_names(folder_path)
create_folders_from_names(base_dir, subfolder_names)
