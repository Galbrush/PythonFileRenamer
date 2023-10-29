
import os

def file_renamer(directory, newName):

    files = os.listdir(directory)
    global counter
    counter = 0

    for file in files:
        try:
            fileType = file.split('.')[-1] 
            os.rename(directory + '/' + file, directory + '/' + newName + str(counter) + '.' + fileType)
            print("Renaming " + file + " to " + newName + str(counter) + "." + fileType)
            counter += 1
        except: 
            print("Couldn't rename file")


    