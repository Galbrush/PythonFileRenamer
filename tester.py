from buldRenamer import *

path = "C:\\Users\\cathr\\OneDrive\\42\\0. Projects\\python_BuldRenamer\\PythonFileRenamer\\TestDocuments"
testName = "myNewName"
test_re_pattern = "test.*"
def create_new_file(path, file):
    with open(os.path.join(path, file), 'w') as fp: 
        pass


# 1. Rename files and log what happened
# 2. Delete the files
# 3. Create new files with "test" as name

file_renamer(path, testName, test_re_pattern)

create_new_file(path, "test.txt")
create_new_file(path, "test.docx")
create_new_file(path, "test.xlsx")

print("Test is Completed")


