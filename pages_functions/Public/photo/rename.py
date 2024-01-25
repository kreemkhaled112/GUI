import os

def get_file_extension(filename):
    _, file_extension = os.path.splitext(filename)
    return file_extension

folder_path = os.getcwd()  
# List all files in the folder
files = os.listdir(folder_path)

name = 1
# Iterate through the files and rename them
for filename in files:
    ex = get_file_extension(filename)
    if ex == ".py" :
        continue
    new_name = f"{name}{ex}"
    
    # Create the full paths for the old and new names
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)
    name += 1
    
print("File names in the folder have been changed.")
