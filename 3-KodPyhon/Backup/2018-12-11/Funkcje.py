totalSize = 0
 for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
 print(totalSize)

from datetime import datetime
datetime.fromtimestamp(1382189138.4196026).strftime('%Y-%m-%d %H:%M:%S')
'2013-10-19 16:25:38'

############################## Example
import os

print("My Path: "+os.getcwd())
print(os.listdir("."))
print("Root/: ",os.listdir("/"))


for items in os.listdir("."):
    if os.path.isdir(items):
        print(items+" "+"Is a Directory")
        print("---Information:")
        print("    *Full Name: ",os.path.dirname(items))
        print("    *Created Time: ",os.path.getctime(items))
        print("    *Modified Time: ",os.path.getmtime(items))
        print("    *Size: ",os.path.getsize(items))
    else:
        print(items+" Is a File")