import os
import shutil

root_dir = "POP909/"
paths = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        # construct the full file path
        file_path = os.path.join(dirpath, filename)
        # print the file path
        #print(file_path)
        paths.append(file_path)

for path in paths:
    
    if path.endswith('.mid') and len(path) == 18:
        print(path)
        shutil.move(path, './MY_POP/')
