import os
import sys
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
                if any([tag in f_tags for tag in tags]):
                    true_file = file.replace(".amdf", "")
                    result.append(true_file)
    return result

def get_files_with_authors(authors, folder_path):

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
                f_authors = [t.strip().lower() for t in f_lines[2].strip().split(',')]
                if any([tag in f_authors for tag in authors]):
                    true_file = file.replace(".amdf", "")
                    result.append(true_file)
    return result

    
files = get_files_with_tags(["furry"], "folder/")
for i in range(len(files)):
    os.system("open " + str(files[i]))