import os 

path = 'yt_dlp/version.py'

isFile = os.path.isfile(path)
#print(isFile)

if isFile == True:
    f = open('yt_dlp/version.py')
    content = f.readlines()
    versionNumber = content[2].split('=')
    #check = versionNumber.split('=')
    version = versionNumber[1]
    print(version)

else:
    pass