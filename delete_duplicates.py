import os
import imagehash
from PIL import Image
from multiprocessing import Pool

def find_duplicates(folder_path):
    """Finds duplicate images in a folder based on pHash."""
    hashes = {}
    duplicates = []
    for filename in os.listdir(folder_path):
        if filename.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
            filepath = os.path.join(folder_path, filename)
            try:
                with Image.open(filepath) as img:
                    img_hash = imagehash.phash(img)
                    if img_hash in hashes:
                        duplicates.append(filepath)
                    else:
                        hashes[img_hash] = filepath
            except OSError:
                print(f"Error reading {filename}. Skipping...")
    return duplicates

def delete_duplicates(duplicates):
    """Deletes the given duplicate image files."""
    for filepath in duplicates:
        try:
            os.remove(filepath)
            print(f"Deleted {filepath}")
        except OSError:
            print(f"Error deleting {filepath}. Skipping...")

def process_subfolder(subfolder_path):
    """Finds and deletes duplicates in a single subfolder."""
    duplicates = find_duplicates(subfolder_path)
    if duplicates:
        print(f"\nDuplicate images found in {subfolder_path}:")
        for filepath in duplicates:
            print(filepath)

        delete_duplicates(duplicates)
    else:
        print(f"No duplicate images found in {subfolder_path}.")

def main():
    root_folder_path = input("Enter the root folder path: ")
    subfolders = [os.path.join(root_folder_path, subfolder_name)
                 for subfolder_name in os.listdir(root_folder_path)
                 if os.path.isdir(os.path.join(root_folder_path, subfolder_name))]

    with Pool() as pool:  # Create a process pool
        pool.map(process_subfolder, subfolders)  # Process subfolders in parallel
        
    print("\nFinished processing all subfolders.")

if __name__ == "__main__":
    main()
