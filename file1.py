import folder.file2
import folder.file2 as file2Alias
from folder.file2 import File2Class, File2Class2 as Pepino

file2Alias.File2Class.print_file2_class()
Pepino.print_file2_class()

folder.file2.File2Class.print_file2_class()

File2Class.print_file2_class()

file2Alias.outside_call()

class File1Class:

    file2Alias.File2Class.print_file2_class()

    def file1method():
        File2Class.print_file2_class()
        file2Alias.outside_call()
        file2Alias.File2Class.print_file2_class()


    file2Alias.outside_call()
    File2Class.print_file2_class()

    