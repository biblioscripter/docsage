import os
from glob import glob

def get_subfolder_names(path):
    subfolders = glob(os.path.join(path, '*/'))
    subfolder_names = [os.path.basename(os.path.normpath(subfolder)) for subfolder in subfolders]
    return subfolder_names

# Example usage:
folder_path = 'train'
subfolder_names = get_subfolder_names(folder_path)
print(subfolder_names)
