import folder
import folder.file2 as file2Alias
from folder.file2 import File2Class, File2Class2 as Pepino
from folder import file2
from folder.file2 import outside_call
from folder.file2 import outside_call as outsidecallalias
import test2.folder1.filetest1 as test1

test1.fileTest1()


outside_call()
outsidecallalias()




file2Alias.File2Class.print_file2_class()
# file3Alias.File2Class.print_file2_class()
Pepino.print_file2_class()

folder.file2.File2Class.print_file2_class()

File2Class.print_file2_class()

file2Alias.outside_call()
# file3Alias.outside_call()

class File1Class:

    outside_call()
    outsidecallalias()
    file2Alias.File2Class.print_file2_class()
    file2Alias.outside_call()
    # file3Alias.File2Class.print_file2_class()
    # file3Alias.outside_call()
    File2Class.print_file2_class()

    def file1method():
        
        outside_call()
        outsidecallalias()
        File2Class.print_file2_class()
        file2Alias.outside_call()
        file2Alias.File2Class.print_file2_class()
        # file3Alias.outside_call()
        # file3Alias.File2Class.print_file2_class()


class File1Class2(folder.file2.File2Class):
    def file1class2method():
        print("hi")

    

class File1Class3(Pepino):
    def file1class2method():
        print("hi")