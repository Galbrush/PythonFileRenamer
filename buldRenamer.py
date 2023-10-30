
import os
import re

def file_renamer(directory, newName, re_pattern = None):

    files = os.listdir(directory)
    global counter
    counter = 0


    for file in files:
        if re_pattern == None:
            print("renaming ALL files")
            try:
                fileType = file.split('.')[-1] 
                os.rename(directory + '/' + file, directory + '/' + newName + str(counter) + '.' + fileType)
                print("Renaming " + file + " to " + newName + str(counter) + "." + fileType)
                counter += 1
            except: 
                print("Couldn't rename file")
        else: 
            print("renaming SOME files")

            try:
                if re.match(re_pattern, file):
                    fileType = file.split('.')[-1] 
                    os.rename(directory + '/' + file, directory + '/' + newName + str(counter) + '.' + fileType)
                    print("Renaming " + file + " to " + newName + str(counter) + "." + fileType)
                    counter += 1
            except: 
                print("Couldn't rename file")


    