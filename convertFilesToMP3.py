from pydub import AudioSegment
import sys
import re
import os
from os import listdir
from os.path import isfile, join, splitext

def sanitizeFileName(input):
    # Replace any character that is not alphanumeric with an empty string
    return re.sub(r'[^a-zA-Z0-9]', '', input)

# Set the encoding of stdout to 'utf-8' for the terminal (otherwise nothing works, this is great for printing and stuff)
sys.stdout.reconfigure(encoding='utf-8')

mypath = "." # current dir
target_dir = './mp3FilesHere'
exclude_extensions = ['.txt', '.py'] # no need for folders, they're auto banned the way the next line works

# List all files in the current directory that are not py/txt/folder (ensures only audio files for this context essentially)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and not any(f.endswith(ext) for ext in exclude_extensions)]

# isfile(join(mypath, f)): This function checks if the path created by join(mypath, f) refers to a file (as opposed to a directory). It returns True if the path points to a file and False if it's a directory.
# [f for f in listdir(mypath) if isfile(join(mypath, f))]: This is the list comprehension part. It iterates over each entry returned by listdir(mypath). For each entry, it checks if it's a file using isfile(join(mypath, f)). If it's a file, that file name (f) is included in the resulting list onlyfiles.


# Print the list of files
print(onlyfiles)


for file in onlyfiles:
    nameOfFile = ""
    name, ext = splitext(file)
    #print("File Name (without extension): ", name)
    nameOfFile = sanitizeFileName(name)
    #print("nameOfFile: ", nameOfFile)


    command = f'ffmpeg -i "{file}" "{nameOfFile}.mp3"' # ffmpeg -i "fileName.extension" fileName.mp3 
    #print("Running command:", command)
    os.system(command)
    mp3_file = f"{nameOfFile}.mp3"
    if os.path.exists(mp3_file):
                os.rename(mp3_file, os.path.join(target_dir, mp3_file))
                #print(f"Moved {mp3_file} to {target_dir}")
                os.remove(file)
                #print(f"Deleted {file} after conversion.")

print("DONE!!!")