import os

file_path = "path_to_your_directory/background.png"

if os.path.exists(file_path):
    print("The file exists!")
else:
    print("The file does not exist.")