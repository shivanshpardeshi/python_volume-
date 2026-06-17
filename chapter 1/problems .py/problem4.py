import os

directory_path = '/'

contents = os.listdir(directory_path)  # Current directory

for item in contents:
    print(item)