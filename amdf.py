# open sauce? what sauce? ohhh "The sauce"

import os
from pathlib import Path

def get_files_with_tags(tags, folder_path):

    result = [] # A varable in which a list of all file paths are stored.

    # Throw an error if the directory path doesn't exist.
    if not os.path.isdir(folder_path):
        raise FileNotFoundError("HEY DUMBASS, THERE IS NO DIRECTORY") # WIP Change error message.


    # Get a list of all the files in the folder (not recursive).
    folder = Path(folder_path)
    file_paths = [str(f) for f in folder.iterdir() if f.is_file()]

    # Read each file and add them to a list.
    for file in file_paths:
        if file.endswith(".amdf"):
            with open(file) as f:
                f_lines = f.readlines()
                try:
                    f_tags = [t.strip().lower() for t in f_lines[1].strip().split(',')]
                except:
                    f_tags = []
                if any([tag in f_tags for tag in tags]):
                    true_file = file.replace(".amdf", "")
                    result.append(true_file)
    return result

def get_files_with_authors(authors, folder_path):

    result = [] # A varable in which a list of all file paths are stored.

    # Throw an error if the directory path doesn't exist.
    if not os.path.isdir(folder_path):
        raise FileNotFoundError("directory not found") # Change error message.


    # Get a list of all the files in the folder (not recursive).
    folder = Path(folder_path)
    file_paths = [str(f) for f in folder.iterdir() if f.is_file()]

    # Read each file and add them to a list.
    for file in file_paths:
        if file.endswith(".amdf"):
            with open(file) as f:
                f_lines = f.readlines()
                try:
                    f_authors = [t.strip().lower() for t in f_lines[2].strip().split(',')]
                except:
                    f_authors = []
                if any([tag in f_authors for tag in authors]):
                    true_file = file.replace(".amdf", "")
                    result.append(true_file)
    return result

def write_amdf(file, folder_path, tags, authors):
    # Check if directory exists
    if not os.path.isdir(folder_path):
        raise FileNotFoundError("Directory not found")
    
    # Create full file path
    file_path = os.path.join(folder_path, file)

    # Open file in write mode
    with open(file_path, 'w') as f:
        # Line 1: (Empty or future use)
        f.write("\n")  
        
        # Line 2: Tags (comma-separated)
        if tags:
            f.write(",".join(str(tag) for tag in tags) + "\n")
        else:
            f.write("\n")  # Empty if no tags
        
        # Line 3: Authors (comma-separated)
        if authors:
            f.write(",".join(str(author) for author in authors) + "\n")
        else:
            f.write("\n")  # Empty if no authors
