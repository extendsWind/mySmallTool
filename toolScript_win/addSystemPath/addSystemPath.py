"""
Adding the directories in the "path.txt" to system variable %PATH%


Note:

- administrator authority is needed, suggest to run in cmd with admin
- only used in windows, and tested in win10

"""

import os

env_dist = os.environ

winPath_list = list(os.path.normpath(p) for p in env_dist["PATH"].split(";"))
winPath = set(winPath_list)
# print(env_dist["PATH"])

print(winPath)

pathFile = open("path.txt")

for line in pathFile:
    winPath_list.append(os.path.normpath(line.strip("\n")))

print(winPath_list)

addr_to = list(set(winPath_list))
addr_to.sort(key=winPath_list.index)

# why there is "." in the list sometimes?
if "." in addr_to:
    addr_to.remove(".")


rltPathStr = ";".join(addr_to)

cmdStr = "setx /M PATH \"" + rltPathStr + "\""

print(cmdStr)

os.system(cmdStr)
