import os

folder_path = "Week-2\\8_April"
file_name = "filename.txt"


# # Check if the folder exists, if not create it
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)


# Combine the folder path and file name
file_path = os.path.join(folder_path, file_name)


# Open a file in write mode in the specified folder

with open(file_path, "w") as file:
    file.write("Hello, this is the content of the file.")
