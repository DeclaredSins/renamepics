import os

# get input
filename = input('Filename?\n')

filelist=os.listdir()
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)

i = 0
for files in filelist:
    files.join('./')
    i = i + 1
    os.rename(files, filename + str(i) + ".png")