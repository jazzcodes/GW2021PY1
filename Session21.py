import os

print(os.name)
print(os.uname())
print(os.getlogin())
print(os.getcwd())
print(os.getppid())

path_to_directory = "/Users/ishantkumar/Downloads/profilepage"
path_to_file = "/Users/ishantkumar/Downloads/Ishant.pdf"

print(os.path.isdir(path_to_directory))
print(os.path.isfile(path_to_file))

# path_to_directory = "/Users/ishantkumar/Downloads/GW2020PY1"
# os.mkdir(path_to_directory)

files = os.walk(path_to_directory)
files = list(files)
for file in files:
    print(file)

for data in files[0]:
    print(data, len(data))

print("Directories:", len(files[0][1]))
print("Files:", len(files[0][2]))

# Mini Project: File Explorer -> Extract different types of files :)

