from glob import glob as ls
from os.path import join
from re import match
from os import rename
from os import system


baseDir = '/tmp/trekbuddy/01-SubMap/'
setDir = '/tmp/trekbuddy/01-SubMap/set/'

listOfFiles = ls(join(setDir, '*.png'))
renamePattern = join(setDir, r'SubMap01_(\d+)_(\d+).png')

firstNumList = []
for item in listOfFiles:
    filePath = join(setDir, item)
    r = match(renamePattern, item)

    if not(r is None):
        firstNum = '%05d' % int(r.group(1))
        secondNum = '%05d' % int(r.group(2))

        firstNumList.append(firstNum)

        newFileName = 'SubMap01_' + firstNum + '_' + secondNum + '.png'
        newFilePath = join(setDir, newFileName)
        print newFileName
        rename(filePath, newFilePath)

firstNumList = unique(firstNumList)
for item in firstNumList:
    listOfFiles = ls(join(baseDir, 'SubMap01_' + item + '*'))
    numOfFiles = len(listOfFiles)
    cmd = "montage " + join(setDir,"SubMap01_" + item + "_*.png") + " -mode Concatenate -tile 1x " + join(baseDir, "SubMap01_"+item+".png")
    print cmd
    system(cmd)


cmd = 'montage ' + join(baseDir, "SubMap01_*.png") + " -mode Concatenate -tile x1 " + join(baseDir, 'SubMap.png')
print cmd
system(cmd)