import os
import shutil
from glob import glob

def get_subfolder_names(path):
    subfolders = glob(os.path.join(path, '**', '*/'), recursive=True) # Find all subfolders recursively
    subfolder_names = [os.path.basename(os.path.normpath(subfolder)) for subfolder in subfolders]
    return subfolders, subfolder_names

def create_folders_from_names(base_dir, subfolder_names):
    for name in subfolder_names:
        new_folder_path = os.path.join(base_dir, name)
        if not os.path.exists(new_folder_path):  
            os.makedirs(new_folder_path)
            print(f"Created folder: {new_folder_path}")
        else:
            print(f"Folder already exists: {new_folder_path}")

def copy_images_to_folders(subfolders, base_dir):
    for subfolder in subfolders:
        subfolder_name = os.path.basename(os.path.normpath(subfolder))
        destination_folder = os.path.join(base_dir, subfolder_name)
        for file in glob(os.path.join(subfolder, "*")):
            if file.endswith((".png", ".jpg", ".jpeg")): 
                shutil.copy2(file, destination_folder)

def process_folder(folder_path, base_dir):
    subfolders, subfolder_names = get_subfolder_names(folder_path)
    create_folders_from_names(base_dir, subfolder_names)
    copy_images_to_folders(subfolders, base_dir)

# Example usage:
main_folders = ['train', 'val', 'test'] 
base_dir = '.'         

for folder in main_folders:
    folder_path = os.path.join(base_dir, folder)  
    process_folder(folder_path, base_dir)
