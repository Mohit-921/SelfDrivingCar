import glob
import os

# Specify the directory path
directory_path = "C:\\Users\\user\\Desktop\\Downloads"

# List all .pdf files in the specified directory
txt_files = glob.glob(os.path.join(directory_path, "*.pdf"))
print("Text files in the specified directory:")
count  = 0
for file in txt_files:
    count+=1
    print(file)
print(f"Total Files : {count}")
