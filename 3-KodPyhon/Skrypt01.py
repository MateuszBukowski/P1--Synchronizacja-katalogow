import os
import linecache
import time
import datetime
from datetime import datetime

# This program compares two dirs
# The dirs are store in txt file
############################################################################
#
# TODO: Os path join
# TODO: os.path.abspath()
############################################################################
# Read dir(s) from txt file
############################################################################
#
#  Get the path from the txt file
dirConf = "./PythonSkrypt01/dirConf.txt"

# Czas jest podawany w liczbie sekund jaka mineła od 00:00 01.01.1970 r.
currentTime = time.time()
print(currentTime)

# Date and time
# from datetime import datetime
currentDate = datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d %H:%M:%S')
print(currentDate)
currentDateForFileName = datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d_%H-%M-%S')
print(currentDateForFileName)

# Hostname from OS
myhost = os.uname()[1]
print(myhost)

# Open file
confFile = open(dirConf, 'r')

# Get each row separately
# Even row is source
# Not even is destination
source01 = linecache.getline(dirConf, 1)
destination01 = linecache.getline(dirConf, 2)
source02 = linecache.getline(dirConf, 3)
destination02 = linecache.getline(dirConf, 4)

# Change string to path. Delete last character \n
src01 = source01[0:len(source01)-1]
dst01 = destination01[0:len(destination01)-1]
src02 = source02[0:len(source02)-1]
dst02 = destination02[0:len(destination02)-1]

# Dir, subdir, files
NumberOfSubDirsSRC = 0
NumberOfFilesSRC = 0
NumberOfSubDirsDST = 0
NumberOfFilesDST = 0

confFile.close()

############# Save source subdirectories ana files state #####################
# Open directory changes file (tryb zapisu)
# Jeżeli nazwa pliku przekazana metodzie open() nie istnieje,
# wówczas w trybach zapisu i dołączania nastąpi utworzenie nowego, pustego pliku.
# baconFile.write('Witaj, świecie!\n')
##############################################################################

srcDirChangesFile = open(currentDateForFileName + '_SOURCE_' + myhost + '.txt','w')

for folderName, subfolders, filenames in os.walk(src01):
    srcDirChangesFile.write('======================================================================================\n')
    srcDirChangesFile.write('Katalog bieżący to: ' + folderName + '\n\n')
    srcDirChangesFile.write('--------------------------------------------------------------------------------------\n')
    for subfolder in subfolders:
        srcDirChangesFile.write('Podkatalog: ' + folderName + ': ' + subfolder + '\n')
        NumberOfSubDirsSRC += 1
    for filename in filenames:
        srcDirChangesFile.write('Plik: ' + folderName + ': ' + filename + '\n')
        NumberOfFilesSRC += 1

srcDirChangesFile.write("\nLiczba podkatalogów: ")
srcDirChangesFile.write(str(NumberOfSubDirsSRC))
srcDirChangesFile.write('\n')
srcDirChangesFile.write("Liczba plików: ")
srcDirChangesFile.write(str(NumberOfFilesSRC))

# Close directory changes file
srcDirChangesFile.close()
print("Zapisano dane katalogu  źródłowego do pliku.")

############# Save destination subdirectories ana files state ################
# Open directory changes file (tryb zapisu)
##############################################################################
dstDirChangesFile = open(currentDateForFileName + '_DESTINATION_' + myhost + '.txt','w')

for folderName, subfolders, filenames in os.walk(dst01):
    dstDirChangesFile.write('======================================================================================\n')
    dstDirChangesFile.write('Katalog bieżący to: ' + folderName + '\n')
    dstDirChangesFile.write('--------------------------------------------------------------------------------------\n')
    for subfolder in subfolders:
        dstDirChangesFile.write('Podkatalog: ' + folderName + ': ' + subfolder + '\n')
        NumberOfSubDirsDST += 1
    for filename in filenames:
        dstDirChangesFile.write('Plik: ' + folderName + ': ' + filename + '\n')
        NumberOfFilesDST += 1

dstDirChangesFile.write("\nLiczba podkatalogów: ")
dstDirChangesFile.write(str(NumberOfSubDirsDST))
dstDirChangesFile.write('\n')
dstDirChangesFile.write("Liczba plików: ")
dstDirChangesFile.write(str(NumberOfFilesDST))

# Close directory changes file
dstDirChangesFile.close()
##############################################################################
print("Zapisano dane katalogu  docelowego do pliku.")
############# Save log file #####################
# Open directory changes file (tryb dołączania)
logFile = open('syncLog.txt','a')
logFile.write("======================================================================================\n")
logFile.write(currentDate + "\n")
logFile.write("Komputer: " + myhost + "\n")
logFile.write('--------------------------------------------------------------------------------------\n')
logFile.write("Katalog źródłowy: " + src01 + "\n")
logFile.write("Liczba podkatalogów: " + str(NumberOfSubDirsSRC) + "\n")
logFile.write("Liczba plików: " + str(NumberOfFilesSRC) + "\n")
logFile.write('--------------------------------------------------------------------------------------\n')
logFile.write("Katalog docelowy: " + dst01 + "\n")
logFile.write("Liczba podkatalogów: " + str(NumberOfSubDirsDST) + "\n")
logFile.write("Liczba plików: " + str(NumberOfFilesDST) + "\n")
logFile.write('--------------------------------------------------------------------------------------\n')
logFile.write("Zapisano dane katalogu  źródłowego do pliku.\n")
logFile.write("Zapisano dane katalogu  docelowego do pliku.\n")
logFile.write("Zapisano dane do pliku loga.\n")
# Close directory changes file
logFile.close()
##############################################################################
print("Zapisano dane do pliku loga.")
# Print info about folders
# SOURCE 01
print()
src01Abs = os.path.abspath(src01)
print("SOURCE 01")
print("Name:", src01)
# Size of all files in dir
totalSizeSource = 0
numberOfFilesSource = 0
for filename in os.listdir(src01Abs):
    totalSizeSource = totalSizeSource + os.path.getsize(os.path.join(src01Abs, filename))
    numberOfFilesSource += 1
print("Size:", totalSizeSource)
print("Number of files:", numberOfFilesSource)
print("Subfolders and files:", os.listdir(src01Abs))
# Converting timestamp to datetime
srcCreationTimeStamp = os.path.getctime(src01Abs)
srcCreationDataTime = datetime.fromtimestamp(srcCreationTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
print("Creation time:", srcCreationDataTime)
# Converting timestamp to datetime
srcLastModTimeStamp = os.path.getmtime(src01Abs)
srcLastModDataTime = datetime.fromtimestamp(srcLastModTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
print("Last modification time:", srcLastModDataTime)
# print("current time: ", currentTime)

# DESTINATION 01
print()
dst01Abs = os.path.abspath(dst01)
print("DESTINATION 01")
print("Name:", dst01)
# Size of all files in dir
totalSizeDestination = 0
numberOfFilesDestination = 0
for filename in os.listdir(dst01Abs):
    totalSizeDestination = totalSizeDestination + os.path.getsize(os.path.join(dst01Abs, filename))
    numberOfFilesDestination += 1
print("Size:", totalSizeDestination)
print("Number of files:", numberOfFilesDestination)
print("Subfolders and files:", os.listdir(dst01Abs))
# Converting timestamp to datetime
dstCreationTimeStamp = os.path.getctime(dst01Abs)
dstCreationDataTime = datetime.fromtimestamp(dstCreationTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
print("Creation time:", dstCreationDataTime)
# Converting timestamp to datetime
dstLastModTimeStamp = os.path.getmtime(dst01Abs)
dstLastModDataTime = datetime.fromtimestamp(dstLastModTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
print("Last modification time:", dstLastModDataTime)

# Differences between source and destination
print()
print("DIFFERENCES")
# print(totalSizeSource, "- size of all files is in source directory.")
# print(totalSizeDestination, "- size of all files is in destination directory.")
print(totalSizeSource-totalSizeDestination, "- difference between source and destination in size of all files (byte).")
# print("Number of files in source:", numberOfFilesSource)
# print("Number of files in destination:", numberOfFilesDestination)
print(numberOfFilesSource-numberOfFilesDestination, "- difference between source and destination in number of all files.")
print((os.path.getmtime(src01Abs))-(os.path.getmtime(dst01Abs)), "- difference between Last modyfication time of source and destination directory (sec).")
print("-----------------------------------------------------------------")

#
#
#
# # SOURCE 02
# print()
# src02Abs = os.path.abspath(src02)
# print("SOURCE 02")
# print("Name:", src02)
# print("Subfolders and files:", os.listdir(src02Abs))
#
# # DESTINATION 01
# print()
# dst02Abs = os.path.abspath(dst02)
# print("DESTINATION 02")
# print("Name:", dst02)
# print("Subfolders and files:", os.listdir(dst02Abs))
# print()
# print("-----------------------------------------------------------------")

##############################################################################################
# TODO: Print quantity of all dir and file in it
# TODO: Compare and print size and quantity of both readed dirs
# TODO: Compare files nad dirs of both readed dirs, print diferences or ok
# TODO: Store results to txt file








