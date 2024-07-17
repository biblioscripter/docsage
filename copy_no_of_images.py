import os
import shutil
from random import sample

# Define source and destination paths
source_train_path = 'train'
source_val_path = 'val'
dest_train_path = 'new_train'
dest_val_path = 'new_val'

# Create destination directories if they do not exist
os.makedirs(dest_train_path, exist_ok=True)
os.makedirs(dest_val_path, exist_ok=True)

# Function to copy images
def copy_images(source, dest, max_images=500):
    for folder in os.listdir(source):
        source_folder = os.path.join(source, folder)
        dest_folder = os.path.join(dest, folder)
        os.makedirs(dest_folder, exist_ok=True)
        
        if os.path.isdir(source_folder):
            images = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
            images_to_copy = sample(images, min(len(images), max_images))
            
            for image in images_to_copy:
                shutil.copy(os.path.join(source_folder, image), os.path.join(dest_folder, image))

# Copy images from 'train' and 'val' folders
copy_images(source_train_path, dest_train_path)
copy_images(source_val_path, dest_val_path)

print("Images copied successfully.")
