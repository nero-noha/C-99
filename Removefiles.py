import os
import shutil
import time

# Set the path to the directory you want to clean
path = "C:\\Users\\dharp\\Desktop\\python\\Project 99\\Removefiles.py"

# Set the number of days as a threshold
days = 30

# Calculate the threshold time in seconds
threshold_time = time.time() - (days * 24 * 3600)

# Check if the path exists
if os.path.exists(path):
    # Iterate over the files and folders using os.walk
    for root, dirs, files in os.walk(path):
        for item in files + dirs:
            item_path = os.path.join(root, item)
            # Get the creation time of the item
            ctime = os.path.getctime(item_path)

            # Compare the creation time with the threshold time
            if ctime < threshold_time:
                if os.path.isfile(item_path):
                    # If it's a file, remove it
                    os.remove(item_path)
                    print(f"Removed file: {item_path}")
                elif os.path.isdir(item_path):
                    # If it's a directory, remove it and its contents
                    shutil.rmtree(item_path)
                    print(f"Removed directory: {item_path}")
else:
    print(f"Path '{path}' not found.")
