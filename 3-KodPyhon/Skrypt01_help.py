import os

# Windows and Linux path resolution:
#######################################
# joinPath = os.path.join("usr","bin","spam")
# print(joinPath)

# Current Work Directory
#########################
# cwd = os.getcwd()
# print(cwd)

# Change current work dir
#########################
# os.chdir("/home/mateusz")
# cwd = os.getcwd()
# print(cwd)

# Make directory
#################
# os.makedirs("/home/mateusz/test/test01/test0101")
# os.chdir("/home/mateusz")
# cwd = os.getcwd()
# print(cwd)
# os.chdir("/home/mateusz/test")
# cwd = os.getcwd()
# print(cwd)

# Absolute and Relative Path
##############################
# print()
#
# here = os.path.abspath(".")
# print(here)
#
# elsewere = os.path.abspath("../../test/test01/test0101")
# print(elsewere)
#
# isAbs = os.path.isabs(".")
# print(isAbs)
# isAbs = os.path.isabs(os.path.abspath("."))
# print(isAbs)

# Directory, Base and Split name
################################
# print()
#
# path = "/home/mateusz/test.txt"
# print("Path - ", path)
#
# baseName = os.path.basename(path)
# print("Baze - ", baseName)
#
# directoryName = os.path.dirname(path)
# print("Dir - ", directoryName)
#
# splitPath = os.path.split(path)
# print("Split - ", splitPath)
#
# sepPath = path.split(os.path.sep)
# print("Separate - ", sepPath)
#
# sepPath2 = "/home/mateusz/test.txt".split(os.path.sep)
# print("Separate 02 - ", sepPath2)

# File size and content
#######################
# print()
#
# path = "/home/mateusz/test.txt"
# fileSize = os.path.getsize(path)
# print("Size of file: ", path, "is - ", fileSize)
#
# print()
# directoryName = os.path.dirname(path)
# myListDir = os.listdir(directoryName)
# print("Dir - ", myListDir)
#
# Size of all files
# path = "/home/mateusz"
# totalSize = 0
# for fileName in os.listdir(path):
#     totalSize = totalSize + os.path.getsize(os.path.join(path,fileName))
# print(totalSize)
# OS WALK
#########
# import os
# for folderName, subfolders, filenames in os.walk('C:\\delicious'):
#    print('Katalog bieżący to ' + folderName)
# for subfolder in subfolders:
#     print('PODKATALOG KATALOGU ' + folderName + ': ' + subfolder)
# for filename in filenames:
#     print('PLIK KATALOGU ' + folderName + ': ' + filename)
#
# print('')
