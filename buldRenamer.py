
import os

def file_renamer(directory, newName):

    files = os.listdir(directory)
    counter = 0

    for file in files:
        fileType = file.split('.')[-1] 
        os.rename(directory + '/' + file, directory + '/' + newName + str(counter) + '.' + fileType)
        print("Renaming " + file + " to " + newName + str(counter) + "." + fileType)
        counter += 1
    
    

    