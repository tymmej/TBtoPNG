#!/usr/bin/env python
from glob import glob as ls
from os.path import join
from re import match
from re import escape
from os import rename
from os import system
#from numpy import unique
import numpy
import sys

Dir = "/Users/tymmej/Downloads/"
mapName = sys.argv[1]
baseDir = join(Dir, mapName)
setDir = join(baseDir, "set")

print(setDir)
listOfFiles = ls(join(setDir, "*.png"))
#print(listOfFiles)
regex = r'' + escape(mapName) + r"_(\d+)_(\d+).png"
renamePattern = join(setDir, regex)

firstNumList = []
for item in listOfFiles:
    filePath = join(setDir, item)
    r = match(renamePattern, item)

    if not(r is None):
        firstNum = '%05d' % int(r.group(1))
        secondNum = '%05d' % int(r.group(2))

        firstNumList.append(firstNum)

        newFileName = mapName + "_" + firstNum + "_" + secondNum + ".png"
        newFilePath = join(setDir, newFileName)
        #print(newFileName)
        rename(filePath, newFilePath)

firstNumList = numpy.unique(firstNumList)

for item in firstNumList:
    listOfFiles = ls(join(baseDir, mapName + "_" + item + "*"))
    numOfFiles = len(listOfFiles)
    cmd = "montage \"" + join(setDir, mapName + "_" + item + "_*.png") + "\" -mode Concatenate -tile 1x \"" + join(baseDir, mapName + "_" + item + ".png") + "\""
    print(cmd)
    system(cmd)


cmd = "montage \"" + join(baseDir, mapName + "_*.png") + "\" -mode Concatenate -tile x1 \"" + join(baseDir, mapName + '.png') + "\""
print(cmd)
system(cmd)
