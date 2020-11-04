import folder.file2 as file2Alias
from folder.file2 import File2Class

file2Alias.File2Class.print_file2_class()


File2Class.print_file2_class()

class File1Class:

    def file1method():
        File2Class.print_file2_class()


if __name__ == '__main__':
    File1Class.file1method()
    