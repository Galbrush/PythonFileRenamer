
import os

def file_renamer(directory, newName, fileExtension = None):

    files = os.listdir(directory)
    global counter
    counter = 0


    for file in files:
        if fileExtension == None:
            try:
                fileType = file.split('.')[-1] 
                os.rename(directory + '/' + file, directory + '/' + newName + str(counter) + '.' + fileType)
                print("Renaming " + file + " to " + newName + str(counter) + "." + fileType)
                counter += 1
            except: 
                print("Couldn't rename file")
        else: 

            try:
                if file.endswith(fileExtension):
                    fileType = file.split('.')[-1] 
                    os.rename(directory + '/' + file, directory + '/' + newName + str(counter) + '.' + fileType)
                    print("Renaming " + file + " to " + newName + str(counter) + "." + fileType)
                    counter += 1
            except: 
                print("Couldn't rename file")


    