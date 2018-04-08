from os import path 
import os
import winshell 

 
 
def createShortcut(target, shortcutName):
#target = r"G:\software\Program Files (x86) portable\_Reading_Editing\Typora markdown\Typora\Typora.exe"
	
	s = path.basename(target) 
	fname = path.splitext(s)[0] 

	winshell.CreateShortcut( 
#	Path = path.join(winshell.desktop(), fname + '.lnk'), 
			Path = path.join(os.getcwd(), shortcutName + '.lnk'), 
			Target = target, 
			Icon=(target, 0), 
			Description='shortcut' ) 
	
#createShortcut("G:\software\Program Files (x86) portable\_Reading_Editing\Typora markdown\Typora\Typora.exe", "ty")

shortcutFile = open("shortcuts.txt")

for line in shortcutFile:
	if line == "" :
		continue
	shortcutName = line.split(" ")[-1].strip("\n")
	targetFile = line[:-len(shortcutName)-2]
	print(shortcutName)
	print(targetFile)
	createShortcut(targetFile, shortcutName)
	
