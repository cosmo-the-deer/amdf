import amdf
import os

files = amdf.get_files_with_tags(["furry"], "folder")
for file in files:
    os.system("open " + file)

amdf.write_amdf(
    "song.amdf", 
    "folder", 
    ["rock", "80s"], 
    ["Queen", "Freddie Mercury"]
)