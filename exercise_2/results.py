#!/usr/bin/python

import os
import fnmatch

picturesFolder = 'main_folder'
pictures = list()
folders= list()
d = dict()

# 2. Write a python script to find all the pictures in all the folders.

for root, directories, files in os.walk(picturesFolder):
    for filename in fnmatch.filter(files, '*.jpg') :
        pictures.append(filename)
        parentDir = os.path.split(root)[1] 
        d[parentDir] = filename
    for dir in directories:
        rootFullPath = os.path.join(os.getcwd(), root)
        folders.append(os.path.join(rootFullPath, dir))

# 3. Print the names of all the pictures.
print('Name of the pictures:')
print(*pictures, sep='\n')

# 4. Print the numbers of all the pictures.
print('Number of pictures is', len(pictures))

# 5. Print the number of all the folders.
print('Number of folders is', len(folders))

# 6. Print the full paths to all the folders.
print('Full path of the folders:')
print(*folders, sep='\n')

# 7. Print dictionary with the key being the name of each picture's parent folder and value as the picture's name.
print('Dictionary of pictures filename with parent folder:')
print(d)

# 8. Print a filtered list with the name of the folders that contains the letter 's'
noPathFolders = [os.path.split(folderWithPath)[1] for folderWithPath in folders]
foldersWithS = fnmatch.filter(noPathFolders, '*s*')
print('Folders containing letter \'s\' are:', foldersWithS)