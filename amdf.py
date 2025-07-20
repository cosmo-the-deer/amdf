import os
from pathlib import Path

def get_files_with_tags(tags, folder_path):

    result = [] # A varable in which a list of all file paths are stored.

    # Throw an error if the directory path doesn't exist.
    if not os.path.isdir(folder_path):
        raise FileNotFoundError("HEY DUMBASS, THERE IS NO DIRECTORY") # Change error message.


    # Get a list of all the files in the folder (not recursive).
    folder = Path(folder_path)
    file_paths = [str(f) for f in folder.iterdir() if f.is_file()]

    # Read each file and add them to a list.
    for file in file_paths:
        if file.endswith(".amdf"):
            with open(file) as f:
                f_lines = f.readlines()
                f_tags = [t.strip().lower() for t in f_lines[1].strip().split(',')]
                print(str(f_tags) + " | " + str(tags))
                if any([tag in f_tags for tag in tags]):
                    result.append(file)
    return result

    
print(get_files_with_tags(["furry"], "folder/"))