import os

# List all files and directories in the current directory
print("Files and directories in the current directory:")
for item in os.listdir():
    print(item)

# Check if a file exists
file_name = "sys test.py"
if os.path.exists(file_name):
    print(f"{file_name} exists!")
else:
    print(f"{file_name} does not exist!")
