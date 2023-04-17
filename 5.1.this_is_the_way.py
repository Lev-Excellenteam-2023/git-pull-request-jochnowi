import os

path = r"c:\Users\aron7\Pictures"

list_dir = os.listdir(path)

for dir in list_dir:
    if dir[:4] == 'deep':
        print(dir)
